# 2022-PHM-Conference-Data-Challenge
### 介紹[數據](https://data.phmsociety.org/2022-phm-conference-data-challenge/)
* 2022 PHM Conference Data Challenge 的數據，液壓鑿岩機的故障數據。
* 內容包含15個檔案，分別為三個感應器以及五個操作者互相配對產生。
* 每一個檔案分別為單一使用者於單一感應器上的反應波段。


### 資料預處理
* 標準化
* 添加高斯雜訊
* 擷取前571連續時間序樣本點。
    * padding 將較短的樣本點補齊
    * splitting 切割較長的樣本點

### 預計實驗比較
* 高斯雜訊
* 時間序樣本點。
