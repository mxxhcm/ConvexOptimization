package com.bit.isport.service;

import com.bit.isport.model.BaseEntity;
import com.bit.isport.model.LoginData;

import com.bit.isport.model.LoginEntity;
import com.bit.isport.model.RegisterData;
import com.google.gson.JsonObject;

import org.json.JSONObject;

import okhttp3.Response;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.HEAD;
import retrofit2.http.Headers;
import retrofit2.http.POST;

/**
 * Created by DongBaishun on 2017/8/8.
 */

//登录注册接口
public interface UserService {
  //登录
  @Headers("Content-Type: application/json")
  @POST("login")
  Call<LoginEntity> login(@Body LoginData loginData);

  // 注册
  @Headers("Content-Type: application/json")
  @POST("login")
  Call<BaseEntity> register(@Body RegisterData registerData);

}
