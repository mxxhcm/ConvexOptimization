
import UploadEntity;

import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

/**
 * Created by mxx on 2017/9/7.
 */

public class UploadFile {
    public void uploadSingleFile()
    {

        //先声明一个singleFileService的对象
        Retrofit retrofit = new Retrofit.Builder()
                .addConverterFactory(GsonConverterFactory.create())
                .baseUrl("http://106.14.166.21:8888")
                .build();
        SingleFileService singleFileService = retrofit.create(SingleFileService.class);

        //创建文件内容
        RequestBody fileRequestBody = RequestBody.create(MediaType.parse("application/octet-stream"),"mxxhcm");
        MultipartBody.Part uploadFile =
                MultipartBody.Part.createFormData("file","test1.txt",fileRequestBody);
        //写入文件内容
        Call<UploadEntity> call = singleFileService.uploadSingleFile(uploadFile);
        call.enqueue(new Callback<UploadEntity>() {
            @Override
            public void onResponse(Call<UploadEntity> call, Response<UploadEntity> response) {
                if(response.code() == 200)
                {
                    UploadEntity uploadEntity = response.body();
                    //uploadEntity中存放的是服务器的返回的body内容。。
                    Log.v("upload!","success");
                }
                else
                {
                    Log.v("code:",""+response.code());
                }

            }

            @Override
            public void onFailure(Call<UploadEntity> call, Throwable t) {
                Log.v("upload!",t.toString());
            }
        });

    }
}
