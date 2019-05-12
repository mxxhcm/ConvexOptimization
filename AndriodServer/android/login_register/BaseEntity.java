package com.bit.isport.model;

import java.io.Serializable;

/**
 * Created by DongBaishun on 2017/8/10.
 */


public class BaseEntity<E> implements Serializable {
  private int code;
  private String res;
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

  public String getDetail()
  {
    return detail;
  }
  private void setDetail(String detail)
  {
    this.detail = detail;
  }
}
