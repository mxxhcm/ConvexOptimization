package com.bit.isport.model;

import java.io.Serializable;

/**
 * Created by DongBaishun on 2017/8/10.
 */

public class LoginData {
  private String command;
  private String username;
  private String password;

  public String getCommand() {
    return command;
  }

  public void setCommand(String command) {
    this.command = command;
  }

  public String getUsername() {
    return username;
  }

  public void setUsername(String username) {
    this.username = username;
  }

  public String getPassword() {
    return password;
  }

  public void setPassword(String password) {
    this.password = password;
  }
}
