// 面向对象
// 构造器创建实例对象

function Teacher(name,age,major){
    this.name = name;
    this.age = age;
    this.major = major;
    this.teache = function(){
        console.log(`${this.name}老师教${this.major}课`)
    }
}

//添加新的功能到Teacher的原型对象中
Teacher.prototype.sport = function(hobby){
    this.hobby = hobby;
    console.log(`${this.name}老师喜欢${this.hobby}`)
}


perry = new Teacher('perry',20,'python');
Lily = new Teacher('Lily',20,'java');
// perry.teache();
Lily.teache();
Lily.sport('basketball')


