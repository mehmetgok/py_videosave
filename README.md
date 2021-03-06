# Python ve OpenCV ile video oluşturma (py_videosave)

###### videosave_cv.py:
Bu örnekte OpenCV ile görüntü aygıtında yakalanan kareler OpenCV tümleşik VideoWriter arabirimi ile diske kaydedilmektedir. Burada hem h264 hem de h265 formatlı kayıt yapılabilmektedir. VideoWriter arabirimi ile düşük seviye CODEC ayarlarına erişim sağlanamadığından H265 formatlı kayıt hem fazla disk alanı almakta hem de performans problemine sebep olmaktadır. Bu programda video 10 saniyelik paketler halinde kaydedilmektedir.

###### videosave_pipe.py:
Bu örnekte OpenCV ile görüntü aygıtında yakalanan kareler ***python PIL kütüphanesi*** ile bellek üzerinde JPEG formatına dönüştürülmekte ve PIPE arayüzü ile ffmpeg video kodlayıcısına aktadırlmaktadır. ffmpeg video kodlayıcı, istenilen codec ayarları ile ***subprocess*** kütüpnahesi yardımı ile başlatılmakta ve PIPE üzerinden akan kare verilerini istenilen formatta diske yazmaktadır.

Bu örneklerin çalışabilmesi için üzerinde çalışılan Linux dağıtımında ffmpeg kütüphanesinin yüklü olması gerekmektedir. Örneğin sistemin H265 kodlayabildiğini test için şu komut satırı kullanılabilir:

> ffmpeg -codecs |grep x265

Bu komut çıktısını son satırı şu şekilde olmalıdır:
```
DEV.L. hevc H.265 / HEVC (High Efficiency Video Coding) (encoders: libx265 nvenc_hevc hevc_nvenc hevc_vaapi )
```
Bu çıktıda ***DE*** ifadesi hem Decode hem de Encode işlemlerinin yapılabildiğini göstermektedir.
