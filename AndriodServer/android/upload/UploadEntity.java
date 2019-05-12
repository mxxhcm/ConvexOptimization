/**
 * Created by mxx on 2017/9/7.
 * 这个类主要是从服务器返回的数据中，获得请求体中的内容
 */
public class UploadEntity {

    private int code;
    private String detail;

    public void setCode(int code)
    {
        this.code = code;
    }

    public int getCode()
    {
        return this.code;
    }

    public void setDetail(String detail)
    {
        this.detail = detail;
    }

    public String getDetail()
    {
        return this.detail;
    }
}
