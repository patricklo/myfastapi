from typing import List

#PYTHON类型提示


#1. 嵌套类型提示
datas: List[str] = ["a", "b", "c", "d"]
datas.get(reversed=True)
print(datas)


from typing import Optional, Union
#2 变量可以为空
def example1(var: Union[float, None]):
    pass
def example2(var: Optional[float]):
    pass
def example3(var: float | None):
    pass


from typing import Annotated

#使用Annotated 为一个整数类型添加元数据
Age = Annotated[int, "This is an aga value"]
def set_age(age: Age):
    print(f"Age is {age}")