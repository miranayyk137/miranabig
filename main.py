import src.Python.core.ndim as miranayykbig
import json

if __name__ == "__main__":
    print("请输入一个数组，并且可以调用方法miranayykbig导入此第三方库，来计算这个数组的维度。")
    print("\n")
    print("如输入a = miranayykbig([[1,2,3,4],[2,3])")
    print("\n")
    a = miranayykbig.array([[1,2,3,4],[2,3]]) 
    print("输出：", a.ndim)
    print("\n")
    print("又输入如：s = miranayykbig([1,2,3])")
    print("\n")
    s = miranayykbig.array([1,2,3])
    print("输出为：",s.ndim)
    print("\n")
    print("现在请你们输入一个数组：")
    print("\n")
    a1 =input()#[1,2]
    a2= json.loads(a1)  
    a3 = miranayykbig.array(a2)
    print(a3.ndim)
    print("程序结束。。。。。。")