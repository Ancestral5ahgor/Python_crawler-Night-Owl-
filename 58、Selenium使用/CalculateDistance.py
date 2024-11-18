# opencv的使用
import cv2 
import numpy as np

class CalculateDistance:
    # 获取需要滑动的距离
    # 将验证码背景大图和需要滑动的小图进行处理，先在大图中找到相似的小图的位置，再获取对应的像素偏移量

    def __init__(self,background_path,slide_path,offset_px,offset_py,display):
        """
        : background_path 验证码背景大图地址
        : slide_path 需要滑动的验证码小图地址
        : offset_px 小图距离再大图上的左边边距（像素偏移量）
        : offset_py 小图距离再大图上的顶部边距（像素偏移量）
        """

        # 读入图片
        self.background_img = cv2.imread(background_path)
        self.offset_px = offset_px
        self.offset_py = offset_py
        self.slide_img = cv2.imread(slide_path,cv2.IMREAD_UNCHANGED)
        # 计算X轴缩放因子，已50px为基准
        scale_x = 50 / self.slide_img.shape[1]
        # 使用最近邻插值法缩放图片，得到缩放后50×50的图片
        self.slide_scale_img = cv2.resize(self.slide_img, (0, 0), fx=scale_x, fy=scale_x)
        self.background_cut_img = None
        self.dispaly = display

    def get_distance(self):
        # 将小图转化为灰色
        slide_gray_img = cv2.cvtColor(self.slide_scale_img, cv2.COLOR_BGR2GRAY)
        # 使用canny算子，提取图片边缘特征
        # 特征值可以调试：100，200，细节特征比较明显，数字增大后特征较为粗略
        slide_edge_img = cv2.Canny(slide_gray_img, 5, 10)
        # self.cv_show('canny',slide_edge_img)
        # 将背景图转化为灰色
        background_grey_img = cv2.cvtColor(self.background_cut_img, cv2.COLOR_BGR2GRAY)
        # 使用canny算子，提取图片边缘特征
        background_edge_img = cv2.Canny(background_grey_img, 10, 20)
        # self.cv_show('bg_canny',background_edge_img)
        # 取小图的高和宽
        h,w = slide_edge_img.shape
        

        # 将滑块与背景进行模板匹配，找到缺口对应的位置
        result = cv2.matchTemplate(background_edge_img, slide_edge_img, cv2.TM_CCOEFF)
        # print(result)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # 获取缺口左上角的位置
        top_left = (max_loc[0],max_loc[1])
        print(top_left[0])
        print(f'左上角坐标为：{top_left}')
        # 右下角位置
        bottom_right = (top_left[0] + w, top_left[1] + h)
        print(f'右下角坐标为：{bottom_right}')

        # 再切割后背景图片中画出需要移动的终点位置
        # rectangle（图片源数据，左上角，右下角，颜色，画笔厚度）
        if self.dispaly:
            print(top_left)
            print(bottom_right)
            after_img = cv2.rectangle(self.background_cut_img, top_left, bottom_right, (0, 0, 255), 2)
            
            # 画图
            self.cv_show('after',after_img)
        # 计算移动距离
        slide_distance = top_left[0] + w + 10
        return slide_distance

    def cut_background(self):
        # 切割图片的上下狂
        height = self.slide_scale_img.shape[0]
        # if self.background_img is None:
        #     print("图像加载失败")
        # else:
        #     height = self.background_img.shape[0]
            # 将背景贴图中上下多余部分以及滑块图片部分去除，如：backgroud_img[y1:y2.x1:]
        self.background_cut_img = self.background_img[self.offset_py - 10 : self.offset_py + height + 10,
                                                      self.offset_px + height + 10 : ]
        # self.cv_show('background_cut_img',self.background_cut_img)

    def cv_show(self,name,img):
        cv2.imshow(name,img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def run(self):
        self.cut_background()
        return self.get_distance()
    
if __name__ == '__main__':
    path = r'D:\Code\DarkCatPython\WebCrawler\pic'
    # 路径D:\Code\DarkCatPython\WebCrawler\pic\BG-1726037465.png
    background_path = path + r'\BG-1726056895.png'
    slide_path = path + r'\SD-1726056895.png'
    
    distance_px = 28
    main = CalculateDistance(background_path, slide_path, 25, 119,display=True)
    distance = main.run()
    print(f'Slide distance: {distance}')
