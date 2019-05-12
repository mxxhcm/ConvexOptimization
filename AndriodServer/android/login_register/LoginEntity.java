package com.bit.isport.model;

/**
 * Created by DongBaishun on 2017/8/12.
 */

//这个是从服务器的网页中取回的数据
public class LoginEntity {
    private int code;
    private String res;
    private String token;
    private String detail;

    public int getCode() {
    return code;
  }

    public void setCode(int code) {
    this.code = code;
  }

    public String getRes() {
    return res;
  }

    public void setRes(String res) {
    this.res = res;
  }

    public String getToken() {
    return token;
  }

    public void setToken(String token) {
    this.token = token;
  }

    public String getDetail()
    {
        return detail;
    }
    private void setDetail(String detail)
    {
        this.detail = detail;
    }
}
