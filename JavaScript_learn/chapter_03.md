[TOC]

# 1.语法

## a.区分大小写
所有变量，函数名和操作符都区分大小写。

## b.标识符
1.第一个字符必须是一个字母，下划线或者一个美元符号；
2.其他字符可以是字母、下划线、美元符号或者数字。
3.驼峰命名法

## c.注释
C风格注释，包括单行或者多行。
//
/*
 *这是一个多行（块级注释），加上中间两行的star是为了提高可读性
 *
 */

## d.严格模式
在脚本中启用严格模式，可以在顶部添加如下代码：
"use strict";
这是一个编译指示。

## e.语句
ECMAScript语句以分号结尾。
推荐在条件控制语句中使用代码块，即使代码中只有一条语句
```code
if (test)
{
  alert(test);
}
```

# 2.关键字和保留字
## a.关键字
break do instanceof typeof case else new var catch else new var catch finally return void continue for switch while debugger* function this with default if throw delete in try

## b.保留字
不能用作标识符，还没有任何特定用处，但是他们在将来有可能被用作关键字
abstract enum int short boolean export interface static byte extends long super char final native synchronized class float package throws const goto  private transient debugger implements protected volatile double import public

# 3.变量
ECMAScript变量是松散类型的，就是可以保存任何类型的数据。每个变量仅仅是一个保存值的占位符。
a.定义变量如下
var message;
b.可以用来保存任何值，未初始化的变量，保存undefined。
c.支持直接初始化，
var message = "hi";
d.并不会把变量标记为字符串类型；就是简单的赋值。可以在修改变量的值得同时修改值得类型，如下：
var messgae = "hi";
message = 199;
e.var 定义的为局部变量，退出对应的作用域就会被销毁。
f.可以省略var，声明一个全局变量，但是不推荐，很难维护。
g.一条语句定义多个变量
var a = 1, name = "hello", age = 23;

# 4.数据类型
见文件types.js
Undefined, Null,Boolean,Number和String.还有一种复杂数据类型Object.
## a.typeof操作符
typeof是操作符，不是函数，返回变量的类型。
var message = "hello"
alert(typeof message);
alert(typeof(message));
alert(typeof 23);

## b. Undefined类型
var message；
alert(message==undefined); //true
引入这个值是为了区分空对象指针与未经初始化的变量。
对于未初始化和未声明的变量，执行typeof操作符都返回了undefined值。

## c.Null类型
null值表示一个空对象指针。使用typeof操作符检测null值时会返回"object"。
var message = null;
alert(typeof message);  //object

## d.Bollean类型
有两个字面值:true和false
var huihui = true;
var mxx = false;
可以调用函数Boolean()将其他值转换为boolean.
控制流语句会自动将相应的变量值执行Boolean()函数进行转换操作。
|type|true|false|
|----|----|-----|
|boolean|ture|false|
|string|非空字符串|""（空字符串）|
|number|非零数值（含无穷大）|0和NaN|
|object|任何对象|null|
|undefined|不适用|undefined|

## e.Number类型
var inMum = 31;

浮点数值
浮点数最高经度是17位小数，精确度很差
var floatNum1 = 1.34;
var floatNum2 = 3.4e32;

数值范围
ECMAScript能够表示的
最小值Number.MIN_VALUE,一般是5e-324;
最大值Number.MAX_VALUE,一般是1.7976931348623157e+308
如果超出JavaScript表示范围的话，将被转换成特殊的Infinity，负数的话转化为-Infinity，正数的话转换成Infinity

NaN
NaN，非数值（Not a Number）是一个特殊的数值，用于本来要返回数值的操作数未返回数值的情况。任何涉及NaN的值都会返回NaN.NaN和任何值都不同，包括他自己。
alert(NaN==NaN);
isNaN()函数，接受一个任何类型的参数，返回该参数是否“不是数值”。不是数值但可以被转换为数值的值直接被转换成数值。任何不能被转换成数值的值返回true.
alert(isNaN("blue")); //true
alert(isNan("10")); //false

数值转换
将非数值转换为数值：Number(),parseInt(),parseFloat().Number()可以用于任何数据类型，另两个则将字符串转换为数值。
Number()规则，将true和flase转换为1和0;将数字简单的传入和返回;将null返回0;将undefined返回NaN;将字符串前导0忽略，空字符串转换为0，其余转换为NaN;object的话，调用valueOf()方法，按照前面的规则转换，如果转换为NaN，调用对象toString()方法，然后按照前面的规则转换。
parseInt()和parseFloat()都是解析字符串的，从第一个字符开始解析，一直解析到字符串末尾，或者解析到一个无效位截止。


## f.String类型
字符字面值
|字面值|含义|
|------|----|
|\n|换行|
|\t|制表|
|\b|空格|
|\r|回车|
|\f|进纸|
|\\|转义"\"|
|\'|转义单引号|
|\"|转义双引号|
|\xnn|十六进制表示字符
|\将unnn|十六进制表示的Unicode字符|


转换为字符串
toString()方法
数值，布尔值，对象和字符串值都有一个toString()方法，null和undefined值没有这个方法。
String()方法
如果值有toString()方法，则调用该方法；如果是null，则返回null，如果是undefined，则返回“undefined”

## g.Object类型
var o = new Object(); //可以省略圆括号，但是不推荐
所有object都有以下属性和方法
constructor：保存用于创建当前对象的函数
hasOwnProperty(propertyName):检查给定的属性是否存在当前对象实例中
isPrototypeOf(object):用于检查传入的对象是否是传入对象的原型
propertyIsEnumerable(propertyName):用于检查给定的属性能否使用for-in语句来枚举
toLocaleString():返回对象的字符串表示
toString():返回对象的字符串表示
valueOf():返回对象的字符串，数值或布尔值表示，通常与toString()方法返回值相同

# 5.操作符
算术操作符，未操作符，关系操作符和相等操作符

## a.一元操作符

递增和递减操作符
借鉴于C语言，前置和后置。前置和语句的优先级相同，后置要低于语句的优先级

一元加和减操作符
对于数值不会产生任何的影响；对于非数值，会像使用Number()样对这个值执行转换。

## b.位操作符
按位非(NOT)~
按位与(AND)&
按位或(OR)|
按位亦或(XOR)^
左移(<<)
有符号右移(>>)
无符号右移(>>>)

## c.布尔操作符
逻辑非!
逻辑与&&
如果有一个是null，返回null；如果有一个是undefined，返回undefined
逻辑或||
如果有两个都是null，返回null；如果两个都是undefined，返回undefined

## d.乘性操作符
乘法
如果有一个操作数是NaN，则结果是NaN；如果Infinity与0相乘，结果是NaN；如果Infinity与非0相乘，结果是Infinity或-Infinity；如果Infinity与Infinity相乘，结果是Infinity

除法
如果有一个操作数是NaN，则结果是NaN；如果是Infinity 被Infinity 除，则结果是NaN；如果是零被零除，则结果是NaN；如果是非零的有限数被零除，则结果是Infinity 或-Infinity，取决于有符号操作数的符号；如果是Infinity 被任何非零数值除，则结果是Infinity 或-Infinity，取决于有符号操作数的符号；

求模
如果操作数都是数值，执行常规的除法计算，返回除得的余数；如果被除数是无穷大值而除数是有限大的数值，则结果是NaN；如果被除数是有限大的数值而除数是零，则结果是NaN；如果是Infinity 被Infinity 除，则结果是NaN；如果被除数是有限大的数值而除数是无穷大的数值，则结果是被除数；如果被除数是零，则结果是零；

## e.加性操作符
加法
如果有一个操作数是NaN，则结果是NaN；
如果是Infinity 加Infinity，则结果是Infinity；如果是-Infinity 加-Infinity，则结果是-Infinity；如果是Infinity 加-Infinity，则结果是NaN；

减法
如果有一个操作数是NaN，则结果是NaN；
如果是Infinity 减Infinity，则结果是NaN；如果是-Infinity 减-Infinity，则结果是NaN；如果是Infinity 减-Infinity，则结果是Infinity；如果是-Infinity 减Infinity，则结果是-Infinity；

## f.关系操作符
大于，小于，大于等于，小于等于，返回一个布尔值

## g.相等操作符
相等和不相等
null和undefined是相等的
如果有一个操作数是NaN，则相等操作符返回false，而不相等操作符返回true；即使两个操作数都是NaN，相等操作符也返回false；因为按照规则，NaN 不等于NaN。如果两个操作数都是对象，则比较它们是不是同一个对象。如果两个操作数都指向同一个对象，则相等操作符返回true；否则，返回false。

全等和不相等
===，全等，只在两个操作数不经类型转换就相等的情况下返回true.
null == undefined 返回true
但是null===undefined,返回false

## h.条件操作符
var max = (num1 > num2) ? num1 : num2;

## i.赋值操作符
简单复赋值=
乘赋值 *=
除赋值 /=
模赋值 %=
加赋值 +=
减赋值 -=
左移赋值  <<=
有符号右移赋值 >>=
无符号右移赋值 >>>=

## j.逗号操作符
逗号声明多个变量
var num1 = 2,num2 = 5,num3 = 8;
逗号赋值
var num = (4,5,29,0); 赋值时，逗号操作符总会返回表达式中的最后一项，此时num为0.

# 6.语句
## a.if语句
```code
var mxx = "hello";
if(mxx)
{
  alert("mxxhcm");
}
else
{
  alert("mhhhpl");
}
```
## b.do-while语句
```code
var i = 0;
do{
  i += 2;
}while(i < 10);
alert(i);
```
这种后测试循环语句最常用于循环体中的代码至少要被执行一次的
情形。

## c.while语句
```code
var i = 0
while(i < 10)
{
    i+=2;
    alert(i);
}
```
## d.for语句
```code
var count = 10;
for(var i = 0; i < count; i++)
{
  alert(i);
}
```
## e.for-in语句
```code
for (var property in window):
{
  document.write(property);
}
```
如果表示要迭代的对象的变量值为null 或undefined，for-in 语句会抛出错误。ECMAScript 5 更正了这一行为；对这种情况不再抛出错误，而只是不执行循环体

## f.label语句
```code
mxx: for (var i = 0 ; i < 10; i++)
{
  alert(i);
}
```
## g.break和continue语句
都可以与label语句联合使用，返回代码中特定的位置。多发生在循环嵌套中。
```code
outside:
for (var i = 0; i < 10 ; i++)
{
  for (var j = 0  ; j < 10; j++)
  {
    if(i==5 && j == 5)
    {
      break outsize;
    }
  }
}
```
## h.with语句
with 将代码的作用域设置到一个特定的对象中

严格模式下不允许使用with语句。
## i.switch语句
```code
switch(grades)
{
  case 90:
    alert("A");
    break;
  case 80:
    alert("B");
    break;
  case 70:
    alert("C");
    break;
  case 60:
    alert("D");
    break;
  default:
    alert("N");
}
```
switch 语句中可以使用任何数据类型，无论是字符串还是对象，都是可以的。

# 7.函数
```code
function loveyou()
{
  alert("mxx love mhh");
  return "yes"; //可跟返回值
}
```
## a.理解参数
ECMAScript函数不介意传递进来多少个参数，也不介意是什么数据类型，即使定义函数只接受两个参数，在调用函数的时候也不一定要传递两个参数，可以传递一个，三个，甚至不传递。在ECMAScript函数中的参数在内部是用一个数组表示的。函数接收到的永远都是这个数组，而不关心数组中有哪些的参数。在函数体内可以通过arguments对象来访问这个参数数组。
第一个元素是arguments[0],第二个是arguments[1],类推等等,通过arguments.length属性判断传入了多少个参数。
```code
function hello(num1,num2,num3)
{
  sum = arguments[0] + arguments[1] +arguments[2];
  alert(sum);
}
hello(0); //
hello();  //
hello(1,2,3,4,5,6); //
```
都是可以的，如果传递的参数少了，默认赋值为undefined。

所有参数传递的都是值，不能通过引用传递参数。

## b.没有重载
不支持重载，如果有两个名字相同的函数，该名字只属于后定义的函数。
