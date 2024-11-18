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



            # 在你的代码中使用
        result = cv2.matchTemplate(background_edge_img, slide_edge_img, cv2.TM_CCOEFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # 获取第二高匹配值及其位置
        second_best_value, second_best_loc = get_second_best_match(result)

        if second_best_loc is not None:
            second_best_top_left = (second_best_loc[1], second_best_loc[0])
            second_best_bottom_right = (second_best_top_left[0] + w, second_best_top_left[1] + h)
            
            print(f'第二高匹配值为：{second_best_value}')
            print(f'第二高匹配的左上角坐标为：{second_best_top_left}')
            print(f'第二高匹配的右下角坐标为：{second_best_bottom_right}')
            
            if self.dispaly:
                after_img = cv2.rectangle(self.background_cut_img, second_best_top_left, second_best_bottom_right, (0, 255, 0), 2)
                self.cv_show('after', after_img)


    
    def get_second_best_match(result):
    # 将result矩阵展平为一维数组
        flat_result = result.flatten()
        
        # 获取排序后的索引
        sorted_indices = np.argsort(flat_result)[::-1]  # 从大到小排序
        
        # 获取第二高的值及其索引
        if len(sorted_indices) > 1:
            second_best_index = sorted_indices[1]  # 第二高的值的索引
            second_best_value = flat_result[second_best_index]  # 第二高的值
            
            # 将展平的索引转换为二维坐标
            height, width = result.shape
            second_best_loc = np.unravel_index(second_best_index, (height, width))
            return second_best_value, second_best_loc
        else:
            return None, None  # 如果没有第二高的值