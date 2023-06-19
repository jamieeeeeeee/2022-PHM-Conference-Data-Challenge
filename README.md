# 2022-PHM-Conference-Data-Challenge

### 介紹數據
![](https://hackmd.io/_uploads/HybM7KpDn.png)

* [2022 PHM Conference Data Challenge](https://data.phmsociety.org/2022-phm-conference-data-challenge/) 的數據，液壓鑿岩機的故障數據。
* 內容包含15個檔案，分別為三個感應器以及五個操作者互相配對產生。
    * 三個感應器(pdmp, pin, po)
    * 五個操作者(1, 2, 4, 5, 6)
* 每一個檔案分別為單一使用者於單一感應器上的反應波段。
* 通過移除或修改零件來誘發各種故障。故障觸發器對應的位置在圖中用紅色大寫字母表示。該數據集包含 11 個類別，包括一個無故障 (NF) 類別和 10 個不同的故障類別。
* 訓練集中的樣本點數在 571 到 748 之間。


### 資料預處理
* 標準化
* 添加高斯雜訊
* 統一樣本長度


### 預計實驗比較
* 高斯雜訊
    * 10 dB、20 dB、30 dB、40 dB、50 dB 和無噪聲
* 時間序樣本點(padding, splitting)
    * 300(padding)、500(padding)、571(splitting)、748(splitting)

### 評估指標
$$ 𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦 = \frac {𝐶𝑜𝑟𝑟𝑒𝑐𝑡𝑙𝑦 𝑐𝑙𝑎𝑠𝑠𝑖𝑓𝑖𝑒𝑑} {𝑇𝑜𝑡𝑎𝑙𝑛𝑢𝑚𝑏𝑒𝑟}  $$
