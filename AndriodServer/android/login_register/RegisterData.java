package com.bit.isport.model;

/**
 * Created by DongBaishun on 2017/8/12.
 */

public class RegisterData extends LoginData {
  private String password_confirm;
  private String email;

  public String getPassword_confirm() {
    return password_confirm;
  }

  public void setPassword_confirm(String password_confirm) {
    this.password_confirm = password_confirm;
  }

  public String getEmail()
  {
    return email;
  }

  public void setEmail(String email)
  {
    this.email = email;
  }
}
