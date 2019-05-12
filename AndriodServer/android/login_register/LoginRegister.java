package com.bit.isport.service;

import android.content.Intent;
import android.content.SharedPreferences;
import android.util.Log;
import android.view.View;

import com.bit.isport.model.BaseEntity;
import com.bit.isport.model.LoginData;
import com.bit.isport.model.LoginEntity;
import com.bit.isport.model.RegisterData;
import com.bit.isport.util.MyAPI;
import com.bit.isport.util.SlideFromBottomPopup;
import com.bit.isport.view.activity.LoginActivity;
import com.bit.isport.view.activity.MainActivity;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

/**
 * Created by mxx on 2017/9/7.
 */

public class LoginRegister {

    public void login(String username,String password)
    {
        Retrofit retrofit = new Retrofit.Builder()
                .addConverterFactory(GsonConverterFactory.create())
                .baseUrl("https://106.14.166.21:8888")
                .build();
        UserService service = retrofit.create(UserService.class);

        String command = "login";
        LoginData loginData = new LoginData();
        loginData.setCommand(command);
        loginData.setUsername(username);
        loginData.setPassword(password);

        Call<LoginEntity> call = service.login(loginData);
        call.enqueue(new Callback<LoginEntity>() {
            @Override
            public void onResponse(Call<LoginEntity> call, Response<LoginEntity> response) {
                //请求成功操作
                if (response.code() == 200) {

                    LoginEntity res = response.body();
                    Log.v("login",res.getDetail());
                }
                else
                {
                    Log.v("login failed","");
                }
            }

            @Override
            public void onFailure(Call<LoginEntity> call, Throwable t) {

                Log.v("login failed",""+t.toString());
            }
        });
    }

    public void register(String username,String password,String email)
    {

        Retrofit retrofit = new Retrofit.Builder()
                .addConverterFactory(GsonConverterFactory.create())
                .baseUrl(MyAPI.baseURL)
                .build();
        UserService service = retrofit.create(UserService.class);

        String command = "register";
        final RegisterData registerData = new RegisterData();
        registerData.setCommand(command);
        registerData.setUsername(username);
        registerData.setPassword(password);
        registerData.setEmail(email);

        Call<BaseEntity> call = service.register(registerData);
        call.enqueue(new Callback<BaseEntity>() {
            @Override
            public void onResponse(Call<BaseEntity> call, Response<BaseEntity> response) {

                if(response.code()==200)
                {
                    BaseEntity res = response.body();
                    Log.v("resister",res.getDetail());
                }
                else
                {
                    Log.v("register","failed");
                }
            }

            @Override
            public void onFailure(Call<BaseEntity> call, Throwable t) {
                Log.v("register failed",t.toString());
            }
        });
    }
}
