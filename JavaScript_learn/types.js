/*
var message1;
alert(typeof message1) //Undefined
var message2 = null;
alert(typeof message2) //object
alert(NaN==NaN);
alert(Number(-0.0004893))
*/
alert(Number("null"))
alert(Number("undefined"))
var v1 = 4.3;
var v2 = true;
var v3 = null;
var v4;
alert(String(v1));
alert(v1.toString());
alert(String(v2));
alert(v2.toString());
alert(String(v3));
alert(v3.toString()); //error null和undefined值没有这个方法
alert(String(v4));
alert(v4.toString());
