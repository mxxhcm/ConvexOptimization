package com.bit.isport.service;

import com.bit.isport.model.UploadEntity;

import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.http.Multipart;
import retrofit2.http.POST;
import retrofit2.http.Part;

/**
 * Created by mxx on 2017/9/7.
 */

public interface SingleFileService {

    @Multipart
    @POST("files")
    Call<UploadEntity> uploadSingleFile(@Part MultipartBody.Part file);
    //Call<UploadEntity> uploadSingleFile(@Part("file\";filename=\"test.jpg\"") RequestBody file);

}
