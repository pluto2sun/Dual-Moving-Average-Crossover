import re
import requests
from loguru import logger

# ======== log ========
logger.add("log/debug.log", level="DEBUG", rotation="10 MB", format="{time} {level} {message}")

# ======== proxies ========
proxies = {
    "http": "http://127.0.0.1:7890",
    "socks5": "https://127.0.0.1:7890",
}

if __name__ == '__main__':
    # I want to track a website every 5 seconds 
    website = "https://www.iflow.work/steam?platform=buff-igxe-c5&game=csgo-dota2&order=safe_buy&pagenum=1&min_price=1.0&max_price=5000.0&min_volume=10"
    try:
        response = requests.get(website, proxies = proxies, timeout = 5)
        response.raise_for_status()
        logger.debug(f"response: {response.text}")
    except Exception as e:
        logger.exception(f"Error occurred when requesting {website}: {e}", website=website, e=str(e))

   
    
#     2023-04-05T14:35:41.981829+0800 DEBUG iflow_response: 
# <!doctype html>
# <html>

# <head>
#     <meta charset="utf-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
#     <meta name="baidu-site-verification" content="code-HTysLCGUIJ" />
#     <meta name="referrer" content="strict-origin-when-cross-origin">

#     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.6.1/css/bootstrap.min.css">
#     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css">

#     <!-- <script src="https://kit.fontawesome.com/c8c7730203.js" crossorigin="anonymous"></script> -->
#     <!-- <script defer src="fontawesome-free-6.2.1-web/js/brands.js"></script> -->
#     <!-- <script defer src="fontawesome-free-6.2.1-web/js/solid.js"></script>
#     <script defer src="fontawesome-free-6.2.1-web/js/fontawesome.js"></script> -->

#     <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
#     <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.6.1/js/bootstrap.min.js"></script>

    
#     <script src="/static/scripts/main.js"></script>
#     <script defer src="/static/fontawesome-free-6.2.1-web/js/solid.js"></script>
#     <script defer src="/static/fontawesome-free-6.2.1-web/js/brands.js"></script>
#     <script defer src="/static/fontawesome-free-6.2.1-web/js/regular.js"></script>
#     <script defer src="/static/fontawesome-free-6.2.1-web/js/fontawesome.js"></script>

#     <title>Steam Trading Site Tracker | Steam 挂刀行情站</title>

#     <script>
#         var _hmt = _hmt || [];
#         (function () {
#             var hm = document.createElement("script");
#             hm.src = "https://hm.baidu.com/hm.js?a5301d501cd73accbee89775308fdd5e";
#             var s = document.getElementsByTagName("script")[0];
#             s.parentNode.insertBefore(hm, s);
#         })();
#     </script>

# </head>

# <body>
#     <div class="container-fluid">
#         <div class="row">
#             <h2 class="h1 my-2 font-weight-light text-center">Steam Trading Site Tracker</h2>
#         </div>
#         <div class="row">
#             <div class="col-1"></div>
#             <div class="col-3">
#                 <h4 class="text-center font-weight-light" style="margin-top: 0.5em;">行情摘要</h4>
#             </div>
#             <div class="col-4">
#                 <h3 class="h2 my-2 font-weight-light text-center">Steam 挂刀行情站</h3>
#             </div>
#             <div class="col-4">
#                 <h4 class="text-center font-weight-light" style="margin-top: 0.5em;">筛选 & 排序设置</h4>
#             </div>
#         </div>
#         <div class="row">
#             <div class="col-1">

#             </div>
#             <div class="col-3">

#                 <!-- <h5 class="card-title">行情分析</h5> -->
#                 <p class="text-center" style="font-size: 18px; margin: 0%;padding-bottom: 0.2em;">当前挂刀指数：<b>0.877</b></p>
#                 <p class="text-center font-weight-light" style="font-size: 16px;"">
#                     优于本月 <span id="30d_percentile">83</span>% 的时间 <span id="30d_stars" style="font-size:16px;color:#CD7F32"></span><br>
#                     优于本季 <span id="90d_percentile">79</span>% 的时间 <span id="90d_stars" style="font-size:16px;color:silver"></span><br>
#                     优于本年 <span id="365d_percentile">36</span>% 的时间 <span id="365d_stars" style="font-size:16px;color:gold"></span>
#                 </p>
#                 <div class="text-center">
#                     <div class="col"></div>
#                     <div class="col">
#                         <button type="button" class="btn btn-outline-primary" style="margin-top: -0.35em"
#                             onclick="location.href='/analysis'">查看行情分析</button>
#                     </div>
#                     <div class="col"></div>
#                 </div>


#             </div>
#             <div class="col-4">
#                 <p class="text-center" style="margin: 0;">更新时间：2023-04-05 14:33:48 UTC+8</p>
#                 <p class="text-center" style="margin: 0;">检测物品数：16089</p>
#                 <p class="text-center" style="margin: 0;"><strong>我们正在寻求 IP 池与代理隧道相关的资源支持，详见<a href="https://www.wolai.com/eZZ1UwWEM9Hawro3cXZjVq">该页面</a></strong></p>
#                 <!-- <p class="text-center" style="margin: 0;"><b>受 C5 服务器异常影响，站点数据更新暂不及时，请见谅</b></p> -->
#                 <p class="text-center" style="margin: 0; color:green">↓↓↓ 看看我们的项目主页与最新进展？ ↓↓↓</p>

#                 <div style="text-align: center; padding-bottom: 0.6em; padding-top: 1em;">
#                     <a href="https://www.wolai.com/eZZ1UwWEM9Hawro3cXZjVq">
#                         <button class="btn btn-outline-secondary">&nbsp;项目主页&nbsp;<i
#                                 class="fa-solid fa-house"></i></button></a>&nbsp;
#                     <a href="https://github.com/EricZhu-42/SteamTradingSiteTracker">
#                         <button class="btn btn-outline-secondary">&nbsp;GitHub 页面&nbsp;<i
#                                 class="fab fa-github"></i></button></a>
#                     <!-- <a href="#" role="button" class="btn btn-outline-secondary" data-target=".sponsorship-modal"
#                         data-toggle="modal">
#                         Support the site <i class="fas fa-heart"></i></a> -->

#                 </div>
#             </div>
#             <div class="col-4">
#                 <div class="row">
#                     <div class="col">
#                         <p style="margin: 0%;padding-left: 1em;padding-bottom: 0.2em;"><strong>平台筛选</strong></p>
#                         <div class="form-check">
                            
#                             <input class="form-check-input" type="checkbox" id="buffCheck" checked>
                            
#                             <label class="form-check-label" for="buffCheck">BUFF</label>
#                         </div>
#                         <div class="form-check">
                            
#                             <input class="form-check-input" type="checkbox" id="igxeCheck" checked>
                            
#                             <label class="form-check-label" for="igxeCheck">IGXE</label>
#                         </div>
#                         <div class="form-check">
                            
#                             <input class="form-check-input" type="checkbox" id="c5Check" checked>
                            
#                             <label class="form-check-label" for="c5Check">C5</label>
#                         </div>
#                         <div class="form-check">
                            
#                             <input class="form-check-input" type="checkbox" id="uuypCheck" checked>
                            
#                             <label class="form-check-label" for="uuypCheck">UUYP</label>
#                         </div>
#                     </div>

#                     <div class="col">
#                         <p style="margin: 0%;padding-left: 1em;padding-bottom: 0.2em;"><strong>游戏筛选</strong></p>
#                         <div class="form-check">
                            
#                             <input class="form-check-input" type="checkbox" id="dota2Check" checked>
                            
#                             <label class="form-check-label" for="dota2Check">Dota 2</label>
#                         </div>
#                         <div class="form-check">
                            
#                             <input class="form-check-input" type="checkbox" id="csgoCheck" checked>
                            
#                             <label class="form-check-label" for="csgoCheck">CS: GO</label>
#                         </div>
#                     </div>

#                     <div class="col">
#                         <p style="margin: 0%;padding-left: 1em;padding-bottom: 0.2em;"><strong>排序依据</strong></p>
#                         <div class="form-check">
#                             <input class="form-check-input" type="radio" name="flexRadioDefault" id="buyRadio"
                            
#                             checked
                            
#                             >
#                             <label class="form-check-label" for="buyRadio">最优求购</label>
#                         </div>
#                         <div class="form-check">
#                             <input class="form-check-input" type="radio" name="flexRadioDefault" id="safebuyRadio"
                            
#                             >
#                             <label class="form-check-label" for="safebuyRadio">稳定求购</label>
#                         </div>
#                         <div class="form-check">
#                             <input class="form-check-input" type="radio" name="flexRadioDefault" id="sellRadio"
                            
#                             >
#                             <label class="form-check-label" for="sellRadio">最优寄售</label>
#                         </div>   
                        
#                     </div>

#                     <div class="col pl-0">
#                         <p class="text-center" style="margin: 0%;padding-bottom: 0.2em;"><strong>交易筛选</strong></p>
#                         <div class="input-group input-group-sm">
#                             <div class="input-group-prepend">
#                                 <span class="input-group-text">≥</span>
#                             </div>
#                             <input type="text" class="form-control" id="minPrice" value="1.0">
#                             <div class="input-group-append">
#                                 <span class="input-group-text">￥</span>
#                             </div>
#                         </div>

#                         <div class="input-group input-group-sm">
#                             <div class="input-group-prepend">
#                                 <span class="input-group-text">≤</span>
#                             </div>
#                             <input type="text" class="form-control" id="maxPrice" value="5000.0">
#                             <div class="input-group-append">
#                                 <span class="input-group-text">￥</span>
#                             </div>
#                         </div>

#                         <div class="input-group input-group-sm">
#                             <div class="input-group-prepend">
#                                 <span class="input-group-text">成交量 ≥</span>
#                             </div>
#                             <input type="text" class="form-control" id="minVolume" value="10">
#                             <!-- <div class="input-group-append">
#                                     <span class="input-group-text"></span>
#                                 </div> -->
#                         </div>
#                     </div>
#                 </div>

#                 <div class="row justify-content-mb-center pb-2">
#                     <div class="col"></div>
#                     <div class="col">
#                         <button type="submit" class="btn btn-outline-primary" style="margin-top: -1.2em"
#                             id="applySortBtn">应用筛选 & 排序</button>
#                     </div>
#                     <div class="col"></div>
#                 </div>
#             </div>

#         </div>

        


# <div class="table-container">
    
#         <table class="table table-hover align-middle" style="table-layout:auto;">
            
            
#                 <thead style="position: sticky;top: 0;" bgcolor="#fcfcfc">
#                 <tr>
                
#                     <th data-bs-toggle="tooltip" data-bs-placement="bottom">
                        
#                             #
                        
#                     </th>
                
#                     <th data-bs-toggle="tooltip" data-bs-placement="bottom">
                        
#                             饰品名称
                        
#                     </th>
                
#                     <th title="Steam Market 当日成交量">
                        
#                             日成交量
                        
#                     </th>
                
#                     <th data-bs-toggle="tooltip" data-bs-placement="bottom">
                        
#                             平台最低售价
                        
#                     </th>
                
#                     <th title="从平台最低售价卖家购入
# 以 Steam Market 最低寄售价卖出">
                        
#                             最优寄售比例
                        
#                     </th>
                
#                     <th title="从平台最低售价卖家购入
# 以 Steam Market 最高求购价价卖出">
                        
#                             最优求购比例
                        
#                     </th>
                
#                     <th title="从平台价格最低三位卖家中发货最快的购入
# 以 Steam Market 最高求购价第三名价格卖出">
                        
#                             稳定求购比例
                        
#                     </th>
                
#                     <th data-bs-toggle="tooltip" data-bs-placement="bottom">
                        
#                             交易平台链接
                        
#                     </th>
                
#                     <th data-bs-toggle="tooltip" data-bs-placement="bottom">
                        
#                             Steam 链接
                        
#                     </th>
                
#                     <th data-bs-toggle="tooltip" data-bs-placement="bottom">
                        
#                             更新时间
                        
#                     </th>
                
#                 </tr>
#                 </thead>
            
            
            
#                 <tbody >
                
                    
#                     <tr data-id="871615" class="item-row even">
                        
#                             <td >1</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> M4A4（StatTrak™） | 彼岸花 (略有磨损)
        
#     </td>
                        
#                             <td >37</td>
                        
#                             <td >80.00</td>
                        
#                             <td style="color:#738c00">0.717</td>
                        
#                             <td style="color:#738c00">0.741</td>
                        
#                             <td style="color:#ff0000">0.850</td>
                        
#                             <td >
        
#         <a href="https://www.igxe.cn/product/730/664174" target="_blank"><button type="button" class="btn btn-outline-success btn-sm text-monospace"><i class="fas fa-italic"></i> IGXE</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/StatTrak™ M4A4 | Spider Lily (Minimal Wear)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >15m 59s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="894099" class="item-row odd">
                        
#                             <td >2</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 印花 | Outsiders | 2022年安特卫普锦标赛
        
#     </td>
                        
#                             <td >6312</td>
                        
#                             <td >1.87</td>
                        
#                             <td style="color:#996600">0.752</td>
                        
#                             <td style="color:#8c7300">0.764</td>
                        
#                             <td style="color:#996600">0.770</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/894099" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Sticker | Outsiders | Antwerp 2022" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >37m 55s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="911114" class="item-row even">
                        
#                             <td >3</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 印花 | Outsiders | 2022年里约热内卢锦标赛
        
#     </td>
                        
#                             <td >8203</td>
                        
#                             <td >1.11</td>
                        
#                             <td style="color:#a65900">0.760</td>
                        
#                             <td style="color:#996600">0.770</td>
                        
#                             <td style="color:#a65900">0.776</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/911114" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Sticker | Outsiders | Rio 2022" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >22m 1s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="876011" class="item-row odd">
                        
#                             <td >4</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 印花 | Movistar Riders | 2021年斯德哥尔摩锦标赛
        
#     </td>
                        
#                             <td >1124</td>
                        
#                             <td >2.20</td>
                        
#                             <td style="color:#a65900">0.761</td>
                        
#                             <td style="color:#996600">0.772</td>
                        
#                             <td style="color:#996600">0.772</td>
                        
#                             <td >
        
#         <a href="https://www.youpin898.com/goodInfo?id=100243" target="_blank"><button type="button" class="btn btn-outline-warning btn-sm text-monospace"><i class="fas fa-underline"></i> UUYP</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Sticker | Movistar Riders | Stockholm 2021" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >39m 37s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="33813" class="item-row even">
                        
#                             <td >5</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 幻彩武器箱
        
#     </td>
                        
#                             <td >5355</td>
                        
#                             <td >14.74</td>
                        
#                             <td style="color:#b24d00">0.774</td>
                        
#                             <td style="color:#a65900">0.778</td>
                        
#                             <td style="color:#b24d00">0.784</td>
                        
#                             <td >
        
#         <a href="https://www.youpin898.com/goodInfo?id=45444" target="_blank"><button type="button" class="btn btn-outline-warning btn-sm text-monospace"><i class="fas fa-underline"></i> UUYP</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Chroma Case" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >25m 14s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="45381" class="item-row odd">
                        
#                             <td >6</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> AWP | 死神 (战痕累累)
        
#     </td>
                        
#                             <td >305</td>
                        
#                             <td >12.17</td>
                        
#                             <td style="color:#738c00">0.717</td>
                        
#                             <td style="color:#a65900">0.778</td>
                        
#                             <td style="color:#cc3300">0.803</td>
                        
#                             <td >
        
#         <a href="https://www.youpin898.com/goodInfo?id=44617" target="_blank"><button type="button" class="btn btn-outline-warning btn-sm text-monospace"><i class="fas fa-underline"></i> UUYP</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/AWP | Mortis (Battle-Scarred)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >6m 2s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="39990" class="item-row even">
                        
#                             <td >7</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 印花 | Counter Logic Gaming | 2016年 MLG 哥伦布锦标赛
        
#     </td>
                        
#                             <td >21</td>
                        
#                             <td >38.00</td>
                        
#                             <td style="color:#b24d00">0.776</td>
                        
#                             <td style="color:#a65900">0.780</td>
                        
#                             <td style="color:#ff0000">1.064</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/39990" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Sticker | Counter Logic Gaming | MLG Columbus 2016" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >8m 52s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="36525" class="item-row odd">
                        
#                             <td >8</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> SSG 08 | 无尽深海 (破损不堪)
        
#     </td>
                        
#                             <td >559</td>
                        
#                             <td >1.04</td>
                        
#                             <td style="color:#b24d00">0.775</td>
                        
#                             <td style="color:#a65900">0.781</td>
                        
#                             <td style="color:#a65900">0.781</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/36525" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/SSG 08 | Abyss (Well-Worn)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >22m 15s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="921379" class="item-row even">
                        
#                             <td >9</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> Revolution Case
        
#     </td>
                        
#                             <td >84407</td>
                        
#                             <td >14.50</td>
                        
#                             <td style="color:#bf4000">0.780</td>
                        
#                             <td style="color:#a65900">0.782</td>
                        
#                             <td style="color:#a65900">0.782</td>
                        
#                             <td >
        
#         <a href="https://www.c5game.com/dota2/1097999762394030080/Revolution Case/sell" target="_blank"><button type="button" class="btn btn-outline-danger btn-sm text-monospace"><i class="fab fa-cuttlefish"></i> &nbsp;C5&nbsp;</button></a>        
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Revolution Case" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >142h 21m 35s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="911259" class="item-row odd">
                        
#                             <td >10</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 印花 | dgt（闪耀）| 2022年里约热内卢锦标赛
        
#     </td>
                        
#                             <td >18</td>
                        
#                             <td >1.07</td>
                        
#                             <td style="color:#a65900">0.765</td>
                        
#                             <td style="color:#a65900">0.782</td>
                        
#                             <td style="color:#f20d00">0.837</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/911259" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Sticker | dgt (Glitter) | Rio 2022" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >46m 30s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="34369" class="item-row even">
                        
#                             <td >11</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 幻彩 2 号武器箱
        
#     </td>
                        
#                             <td >22900</td>
                        
#                             <td >11.62</td>
                        
#                             <td style="color:#b24d00">0.778</td>
                        
#                             <td style="color:#b24d00">0.784</td>
                        
#                             <td style="color:#cc3300">0.803</td>
                        
#                             <td >
        
#         <a href="https://www.c5game.com/dota2/22698/幻彩 2 号武器箱/sell" target="_blank"><button type="button" class="btn btn-outline-danger btn-sm text-monospace"><i class="fab fa-cuttlefish"></i> &nbsp;C5&nbsp;</button></a>        
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Chroma 2 Case" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >44m 58s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="769121" class="item-row odd">
                        
#                             <td >12</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 棱彩武器箱
        
#     </td>
                        
#                             <td >64066</td>
                        
#                             <td >3.30</td>
                        
#                             <td style="color:#bf4000">0.783</td>
                        
#                             <td style="color:#b24d00">0.785</td>
                        
#                             <td style="color:#b24d00">0.785</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/769121" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Prisma Case" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >28m 44s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="894425" class="item-row even">
                        
#                             <td >13</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 印花 | fer（闪耀） | 2022年安特卫普锦标赛
        
#     </td>
                        
#                             <td >162</td>
                        
#                             <td >1.68</td>
                        
#                             <td style="color:#b24d00">0.771</td>
                        
#                             <td style="color:#b24d00">0.785</td>
                        
#                             <td style="color:#b24d00">0.785</td>
                        
#                             <td >
        
#         <a href="https://www.igxe.cn/product/730/668087" target="_blank"><button type="button" class="btn btn-outline-success btn-sm text-monospace"><i class="fas fa-italic"></i> IGXE</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Sticker | fer (Glitter) | Antwerp 2022" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >25h 11m 42s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="759175" class="item-row odd">
                        
#                             <td >14</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 地平线武器箱
        
#     </td>
                        
#                             <td >32836</td>
                        
#                             <td >3.79</td>
                        
#                             <td style="color:#bf4000">0.779</td>
                        
#                             <td style="color:#b24d00">0.785</td>
                        
#                             <td style="color:#b24d00">0.785</td>
                        
#                             <td >
        
#         <a href="https://www.igxe.cn/product/730/613648" target="_blank"><button type="button" class="btn btn-outline-success btn-sm text-monospace"><i class="fas fa-italic"></i> IGXE</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Horizon Case" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >21m 36s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="781534" class="item-row even">
                        
#                             <td >15</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 裂空武器箱
        
#     </td>
                        
#                             <td >182184</td>
                        
#                             <td >3.36</td>
                        
#                             <td style="color:#bf4000">0.785</td>
                        
#                             <td style="color:#b24d00">0.787</td>
                        
#                             <td style="color:#b24d00">0.787</td>
                        
#                             <td >
        
#         <a href="https://www.igxe.cn/product/730/657095" target="_blank"><button type="button" class="btn btn-outline-success btn-sm text-monospace"><i class="fas fa-italic"></i> IGXE</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Fracture Case" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >24m 33s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="911574" class="item-row odd">
                        
#                             <td >16</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 印花 | torzsi（闪耀）| 2022年里约热内卢锦标赛
        
#     </td>
                        
#                             <td >126</td>
                        
#                             <td >2.94</td>
                        
#                             <td style="color:#00ff00">0.535</td>
                        
#                             <td style="color:#b24d00">0.788</td>
                        
#                             <td style="color:#b24d00">0.788</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/911574" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Sticker | torzsi (Glitter) | Rio 2022" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >38m 20s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="763236" class="item-row even">
                        
#                             <td >17</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> “头号特训”武器箱
        
#     </td>
                        
#                             <td >108322</td>
                        
#                             <td >3.30</td>
                        
#                             <td style="color:#bf4000">0.784</td>
                        
#                             <td style="color:#b24d00">0.788</td>
                        
#                             <td style="color:#b24d00">0.788</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/763236" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Danger Zone Case" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >39m 23s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="857622" class="item-row odd">
                        
#                             <td >18</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> SG 553（StatTrak™） | 重金属摇滚 (破损不堪)
        
#     </td>
                        
#                             <td >408</td>
                        
#                             <td >1.88</td>
                        
#                             <td style="color:#bf4000">0.786</td>
                        
#                             <td style="color:#b24d00">0.789</td>
                        
#                             <td style="color:#b24d00">0.789</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/857622" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/StatTrak™ SG 553 | Heavy Metal (Well-Worn)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >41m 56s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="771988" class="item-row even">
                        
#                             <td >19</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 印花 | Natus Vincere | 2019年柏林锦标赛
        
#     </td>
                        
#                             <td >94</td>
                        
#                             <td >2.95</td>
                        
#                             <td style="color:#a65900">0.762</td>
                        
#                             <td style="color:#b24d00">0.791</td>
                        
#                             <td style="color:#b24d00">0.791</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/771988" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Sticker | Natus Vincere | Berlin 2019" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >38m 44s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="911674" class="item-row odd">
                        
#                             <td >20</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 印花 | coldzera（闪耀）| 2022年里约热内卢锦标赛
        
#     </td>
                        
#                             <td >16</td>
                        
#                             <td >3.19</td>
                        
#                             <td style="color:#bf4000">0.782</td>
                        
#                             <td style="color:#b24d00">0.792</td>
                        
#                             <td style="color:#b24d00">0.792</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/911674" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Sticker | coldzera (Glitter) | Rio 2022" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >21m 49s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="33825" class="item-row even">
                        
#                             <td >21</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 弯曲猎手武器箱
        
#     </td>
                        
#                             <td >11507</td>
                        
#                             <td >5.20</td>
                        
#                             <td style="color:#bf4000">0.789</td>
                        
#                             <td style="color:#bf4000">0.795</td>
                        
#                             <td style="color:#bf4000">0.802</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/33825" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Falchion Case" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >9m 29s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="35890" class="item-row odd">
                        
#                             <td >22</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> “凤凰大行动”武器箱
        
#     </td>
                        
#                             <td >5928</td>
                        
#                             <td >15.44</td>
                        
#                             <td style="color:#cc3300">0.795</td>
                        
#                             <td style="color:#bf4000">0.797</td>
                        
#                             <td style="color:#bf4000">0.797</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/35890" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Operation Phoenix Weapon Case" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >37m 8s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="39294" class="item-row even">
                        
#                             <td >23</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> P250（StatTrak™） | 元素轮廓 (战痕累累)
        
#     </td>
                        
#                             <td >95</td>
                        
#                             <td >2.04</td>
                        
#                             <td style="color:#bf4000">0.784</td>
                        
#                             <td style="color:#bf4000">0.799</td>
                        
#                             <td style="color:#bf4000">0.799</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/39294" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/StatTrak™ P250 | Valence (Battle-Scarred)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >2m 11s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="857699" class="item-row odd">
                        
#                             <td >24</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> R8 左轮手枪（StatTrak™） | 废物王 (崭新出厂)
        
#     </td>
                        
#                             <td >40</td>
                        
#                             <td >9.00</td>
                        
#                             <td style="color:#996600">0.746</td>
                        
#                             <td style="color:#bf4000">0.799</td>
                        
#                             <td style="color:#bf4000">0.799</td>
                        
#                             <td >
        
#         <a href="https://www.youpin898.com/goodInfo?id=54596" target="_blank"><button type="button" class="btn btn-outline-warning btn-sm text-monospace"><i class="fas fa-underline"></i> UUYP</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/StatTrak™ R8 Revolver | Junk Yard (Factory New)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >39m 35s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="763361" class="item-row even">
                        
#                             <td >25</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> G3SG1（StatTrak™） | 净化者 (略有磨损)
        
#     </td>
                        
#                             <td >70</td>
                        
#                             <td >9.68</td>
                        
#                             <td style="color:#bf4000">0.780</td>
                        
#                             <td style="color:#cc3300">0.803</td>
                        
#                             <td style="color:#ff0000">0.918</td>
                        
#                             <td >
        
#         <a href="https://www.c5game.com/dota2/553480880/G3SG1（StatTrak™） | 净化者/sell" target="_blank"><button type="button" class="btn btn-outline-danger btn-sm text-monospace"><i class="fab fa-cuttlefish"></i> &nbsp;C5&nbsp;</button></a>        
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/StatTrak™ G3SG1 | Scavenger (Minimal Wear)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >15m 19s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="911587" class="item-row odd">
                        
#                             <td >26</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 印花 | BUDA（闪耀）| 2022年里约热内卢锦标赛
        
#     </td>
                        
#                             <td >41</td>
                        
#                             <td >1.15</td>
                        
#                             <td style="color:#996600">0.751</td>
                        
#                             <td style="color:#cc3300">0.803</td>
                        
#                             <td style="color:#cc3300">0.803</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/911587" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Sticker | BUDA (Glitter) | Rio 2022" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >28m 17s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="40590" class="item-row even">
                        
#                             <td >27</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 印花 | 内卢熊
        
#     </td>
                        
#                             <td >19</td>
                        
#                             <td >5.92</td>
                        
#                             <td style="color:#00ff00">0.579</td>
                        
#                             <td style="color:#cc3300">0.805</td>
                        
#                             <td style="color:#ff0000">0.897</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/40590" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Sticker | Nelu the Bear" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >25m 0s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="36490" class="item-row odd">
                        
#                             <td >28</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> SG 553 | 豹灯蛾 (破损不堪)
        
#     </td>
                        
#                             <td >84</td>
                        
#                             <td >3.88</td>
                        
#                             <td style="color:#cc3300">0.802</td>
                        
#                             <td style="color:#cc3300">0.806</td>
                        
#                             <td style="color:#cc3300">0.806</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/36490" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/SG 553 | Tiger Moth (Well-Worn)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >3m 2s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="769171" class="item-row even">
                        
#                             <td >29</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 沙漠之鹰 | 轻轨 (崭新出厂)
        
#     </td>
                        
#                             <td >119</td>
                        
#                             <td >32.91</td>
                        
#                             <td style="color:#bf4000">0.783</td>
                        
#                             <td style="color:#cc3300">0.807</td>
                        
#                             <td style="color:#cc3300">0.807</td>
                        
#                             <td >
        
#         <a href="https://www.igxe.cn/product/730/621537" target="_blank"><button type="button" class="btn btn-outline-success btn-sm text-monospace"><i class="fas fa-italic"></i> IGXE</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Desert Eagle | Light Rail (Factory New)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >9m 16s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="45658" class="item-row odd">
                        
#                             <td >30</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 驾驶手套（★） | 超越 (战痕累累)
        
#     </td>
                        
#                             <td >11</td>
                        
#                             <td >450.00</td>
                        
#                             <td style="color:#b24d00">0.767</td>
                        
#                             <td style="color:#cc3300">0.807</td>
                        
#                             <td style="color:#ff0000">0.873</td>
                        
#                             <td >
        
#         <a href="https://www.igxe.cn/product/730/611082" target="_blank"><button type="button" class="btn btn-outline-success btn-sm text-monospace"><i class="fas fa-italic"></i> IGXE</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/★ Driver Gloves | Overtake (Battle-Scarred)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >24m 19s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="37387" class="item-row even">
                        
#                             <td >31</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 封装的涂鸦 | 中华美食·百发百粽
        
#     </td>
                        
#                             <td >15</td>
                        
#                             <td >5.12</td>
                        
#                             <td style="color:#b24d00">0.779</td>
                        
#                             <td style="color:#cc3300">0.808</td>
                        
#                             <td style="color:#e61900">0.825</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/37387" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Sealed Graffiti | Terror Rice" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >18m 7s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="39120" class="item-row odd">
                        
#                             <td >32</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 内格夫（StatTrak™） | *哒哒哒* (久经沙场)
        
#     </td>
                        
#                             <td >10</td>
                        
#                             <td >10.42</td>
                        
#                             <td style="color:#59a600">0.693</td>
                        
#                             <td style="color:#cc3300">0.808</td>
                        
#                             <td style="color:#ff0000">0.845</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/39120" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/StatTrak™ Negev | Bratatat (Field-Tested)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >8m 52s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="894286" class="item-row even">
                        
#                             <td >33</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 印花 | rox | 2022年安特卫普锦标赛
        
#     </td>
                        
#                             <td >592</td>
                        
#                             <td >2.12</td>
                        
#                             <td style="color:#a65900">0.759</td>
                        
#                             <td style="color:#cc3300">0.808</td>
                        
#                             <td style="color:#cc3300">0.808</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/894286" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Sticker | rox | Antwerp 2022" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >37m 42s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="876881" class="item-row odd">
                        
#                             <td >34</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> PP-野牛（纪念品） | 开关箱 (久经沙场)
        
#     </td>
                        
#                             <td >15</td>
                        
#                             <td >1.56</td>
                        
#                             <td style="color:#996600">0.747</td>
                        
#                             <td style="color:#cc3300">0.809</td>
                        
#                             <td style="color:#cc3300">0.809</td>
                        
#                             <td >
        
#         <a href="https://www.c5game.com/dota2/927535178977808384/PP-野牛（纪念品） | 开关箱/sell" target="_blank"><button type="button" class="btn btn-outline-danger btn-sm text-monospace"><i class="fab fa-cuttlefish"></i> &nbsp;C5&nbsp;</button></a>        
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Souvenir PP-Bizon | Breaker Box (Field-Tested)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >5m 48s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="37880" class="item-row even">
                        
#                             <td >35</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> P250（纪念品） | 骸骨外罩 (久经沙场)
        
#     </td>
                        
#                             <td >27</td>
                        
#                             <td >1.10</td>
                        
#                             <td style="color:#669900">0.701</td>
                        
#                             <td style="color:#cc3300">0.809</td>
                        
#                             <td style="color:#cc3300">0.809</td>
                        
#                             <td >
        
#         <a href="https://www.igxe.cn/product/730/5104" target="_blank"><button type="button" class="btn btn-outline-success btn-sm text-monospace"><i class="fas fa-italic"></i> IGXE</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Souvenir P250 | Bone Mask (Field-Tested)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >42m 18s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="770329" class="item-row odd">
                        
#                             <td >36</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/fluency-systems-regular/24/000000/dota.png"/> 嘲讽：巨岩滚滚！
        
#     </td>
                        
#                             <td >329</td>
                        
#                             <td >1.31</td>
                        
#                             <td style="color:#a65900">0.758</td>
                        
#                             <td style="color:#cc3300">0.809</td>
                        
#                             <td style="color:#e61900">0.830</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/770329" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/570/Taunt: Rolling Stone!" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >23m 29s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="903842" class="item-row even">
                        
#                             <td >37</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 印花 | 烟中饿鬼（全息）
        
#     </td>
                        
#                             <td >521</td>
                        
#                             <td >5.19</td>
                        
#                             <td style="color:#d92600">0.806</td>
                        
#                             <td style="color:#cc3300">0.810</td>
                        
#                             <td style="color:#cc3300">0.810</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/903842" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Sticker | Get Smoked (Holo)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >32m 27s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="895324" class="item-row odd">
                        
#                             <td >38</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 印花 | FalleN（闪耀） | 2022年安特卫普锦标赛
        
#     </td>
                        
#                             <td >110</td>
                        
#                             <td >4.41</td>
                        
#                             <td style="color:#a65900">0.760</td>
                        
#                             <td style="color:#cc3300">0.810</td>
                        
#                             <td style="color:#cc3300">0.810</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/895324" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Sticker | FalleN (Glitter) | Antwerp 2022" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >34m 38s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="779175" class="item-row even">
                        
#                             <td >39</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 棱彩2号武器箱
        
#     </td>
                        
#                             <td >90929</td>
                        
#                             <td >3.35</td>
                        
#                             <td style="color:#d92600">0.808</td>
                        
#                             <td style="color:#cc3300">0.810</td>
                        
#                             <td style="color:#d92600">0.820</td>
                        
#                             <td >
        
#         <a href="https://www.igxe.cn/product/730/654984" target="_blank"><button type="button" class="btn btn-outline-success btn-sm text-monospace"><i class="fas fa-italic"></i> IGXE</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Prisma 2 Case" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >15m 32s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="36051" class="item-row odd">
                        
#                             <td >40</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> P250 | 死亡轮回 (战痕累累)
        
#     </td>
                        
#                             <td >10</td>
                        
#                             <td >25.36</td>
                        
#                             <td style="color:#a65900">0.765</td>
                        
#                             <td style="color:#cc3300">0.810</td>
                        
#                             <td style="color:#cc3300">0.810</td>
                        
#                             <td >
        
#         <a href="https://www.c5game.com/dota2/24556/P250 | 死亡轮回 (战痕累累)/sell" target="_blank"><button type="button" class="btn btn-outline-danger btn-sm text-monospace"><i class="fab fa-cuttlefish"></i> &nbsp;C5&nbsp;</button></a>        
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/P250 | Muertos (Battle-Scarred)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >6m 13s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="769245" class="item-row even">
                        
#                             <td >41</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 沙漠之鹰 | 轻轨 (战痕累累)
        
#     </td>
                        
#                             <td >479</td>
                        
#                             <td >5.53</td>
                        
#                             <td style="color:#cc3300">0.800</td>
                        
#                             <td style="color:#cc3300">0.811</td>
                        
#                             <td style="color:#e61900">0.828</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/769245" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Desert Eagle | Light Rail (Battle-Scarred)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >2m 0s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="35153" class="item-row odd">
                        
#                             <td >42</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> M249 | 鬼影 (略有磨损)
        
#     </td>
                        
#                             <td >242</td>
                        
#                             <td >1.01</td>
                        
#                             <td style="color:#bf4000">0.787</td>
                        
#                             <td style="color:#d92600">0.812</td>
                        
#                             <td style="color:#d92600">0.812</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/35153" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/M249 | Spectre (Minimal Wear)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >37m 54s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="42234" class="item-row even">
                        
#                             <td >43</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> USP 消音版 | 力矩 (久经沙场)
        
#     </td>
                        
#                             <td >964</td>
                        
#                             <td >4.98</td>
                        
#                             <td style="color:#cc3300">0.802</td>
                        
#                             <td style="color:#d92600">0.813</td>
                        
#                             <td style="color:#d92600">0.813</td>
                        
#                             <td >
        
#         <a href="https://www.youpin898.com/goodInfo?id=2659" target="_blank"><button type="button" class="btn btn-outline-warning btn-sm text-monospace"><i class="fas fa-underline"></i> UUYP</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/USP-S | Torque (Field-Tested)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >14m 55s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="911235" class="item-row odd">
                        
#                             <td >44</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 2022年里约热内卢锦标赛竞争组印花胶囊
        
#     </td>
                        
#                             <td >14673</td>
                        
#                             <td >5.00</td>
                        
#                             <td style="color:#cc3300">0.801</td>
                        
#                             <td style="color:#d92600">0.813</td>
                        
#                             <td style="color:#d92600">0.813</td>
                        
#                             <td >
        
#         <a href="https://www.youpin898.com/goodInfo?id=102770" target="_blank"><button type="button" class="btn btn-outline-warning btn-sm text-monospace"><i class="fas fa-underline"></i> UUYP</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Rio 2022 Contenders Sticker Capsule" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >13m 57s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="876053" class="item-row even">
                        
#                             <td >45</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 布章 | Team Liquid | 2021年斯德哥尔摩锦标赛
        
#     </td>
                        
#                             <td >19</td>
                        
#                             <td >13.65</td>
                        
#                             <td style="color:#cc3300">0.801</td>
                        
#                             <td style="color:#d92600">0.814</td>
                        
#                             <td style="color:#ff0000">0.872</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/876053" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Patch | Team Liquid | Stockholm 2021" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >38m 58s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="39394" class="item-row odd">
                        
#                             <td >46</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> PP-野牛（StatTrak™） | 买定离手 (战痕累累)
        
#     </td>
                        
#                             <td >12</td>
                        
#                             <td >17.00</td>
                        
#                             <td style="color:#738c00">0.709</td>
                        
#                             <td style="color:#d92600">0.814</td>
                        
#                             <td style="color:#d92600">0.814</td>
                        
#                             <td >
        
#         <a href="https://www.igxe.cn/product/730/606173" target="_blank"><button type="button" class="btn btn-outline-success btn-sm text-monospace"><i class="fas fa-italic"></i> IGXE</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/StatTrak™ PP-Bizon | High Roller (Battle-Scarred)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >34m 11s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="34900" class="item-row even">
                        
#                             <td >47</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 加利尔 AR | 蓝钛 (崭新出厂)
        
#     </td>
                        
#                             <td >87</td>
                        
#                             <td >11.47</td>
                        
#                             <td style="color:#bf4000">0.780</td>
                        
#                             <td style="color:#d92600">0.816</td>
                        
#                             <td style="color:#d92600">0.816</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/34900" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Galil AR | Blue Titanium (Factory New)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >32m 53s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="847286" class="item-row odd">
                        
#                             <td >48</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> 印花 | 100 Thieves（全息）| 2020 RMR
        
#     </td>
                        
#                             <td >3899</td>
                        
#                             <td >1.07</td>
                        
#                             <td style="color:#cc3300">0.798</td>
                        
#                             <td style="color:#d92600">0.816</td>
                        
#                             <td style="color:#d92600">0.816</td>
                        
#                             <td >
        
#         <a href="https://buff.163.com/goods/847286" target="_blank"><button type="button" class="btn btn-outline-primary btn-sm text-monospace"><i class="fas fa-bold"></i> BUFF</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/Sticker | 100 Thieves (Holo) | 2020 RMR" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >29m 48s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="871326" class="item-row even">
                        
#                             <td >49</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> CZ75 | 辛迪加 (久经沙场)
        
#     </td>
                        
#                             <td >108</td>
                        
#                             <td >9.67</td>
                        
#                             <td style="color:#e61900">0.815</td>
                        
#                             <td style="color:#d92600">0.816</td>
                        
#                             <td style="color:#d92600">0.816</td>
                        
#                             <td >
        
#         <a href="https://www.youpin898.com/goodInfo?id=61678" target="_blank"><button type="button" class="btn btn-outline-warning btn-sm text-monospace"><i class="fas fa-underline"></i> UUYP</button></a>
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/CZ75-Auto | Syndicate (Field-Tested)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >34m 50s</td>
                        
#                     </tr>
                    
                
                    
#                     <tr data-id="871706" class="item-row odd">
                        
#                             <td >50</td>
                        
#                             <td >
        
#         <img src="https://img.icons8.com/ios/24/000000/counter-strike-source.png"/> M4A4（StatTrak™） | 彼岸花 (久经沙场)
        
#     </td>
                        
#                             <td >88</td>
                        
#                             <td >30.20</td>
                        
#                             <td style="color:#669900">0.702</td>
                        
#                             <td style="color:#d92600">0.817</td>
                        
#                             <td style="color:#d92600">0.817</td>
                        
#                             <td >
        
#         <a href="https://www.c5game.com/dota2/914719626702221312/M4A4（StatTrak™） | 彼岸花/sell" target="_blank"><button type="button" class="btn btn-outline-danger btn-sm text-monospace"><i class="fab fa-cuttlefish"></i> &nbsp;C5&nbsp;</button></a>        
        
#     </td>
                        
#                             <td ><a href="https://steamcommunity.com/market/listings/730/StatTrak™ M4A4 | Spider Lily (Field-Tested)" target="_blank"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fab fa-steam"></i> Steam</button></a></td>
                        
#                             <td >3h 55m 45s</td>
                        
#                     </tr>
                    
                
#                 </tbody>
            
            
            
            
#         </table>
    

    
        
    
# </div>



#         <nav aria-label="page navigation" ,>
#             <ul class="pagination justify-content-center">

                
#                 <li class="page-item disabled">
#                     <a class="page-link" tabindex="-1">上一页</a>
#                 </li>
                

                

                

                

#                 <li class="page-item active">
#                     <a class="page-link">1<span class="sr-only">(current)</span></a>
#                 </li>

#                 <li class="page-item">
#                     <a class="page-link" to_page="2" href="#">2</a>
#                 </li>

#                 <li class="page-item">
#                     <a class="page-link">...</a>
#                 </li>

#                 <li class="page-item">
#                     <a class="page-link" to_page="2" href="#">下一页</a>
#                 </li>

#             </ul>
#         </nav>

#         <div style="text-align:center;">
#             <a href="https://icons8.com/icon/j8xFPlBO2rTI/dota-2">Dota 2 icon by Icons8</a><br>
#             <a href="https://icons8.com/icon/vdR6yRFDgGix/counter-strike-source">Counter Strike Source icon
#                 byIcons8</a>
#         </div>

#         <!-- Sponsorship Modal -->
#         <div class="modal fade sponsorship-modal" id="sponsorshipModal" tabindex="-1" role="dialog">
#             <div class="modal-dialog modal-lg" role="document">
#                 <div class="modal-content">

#                     <div class="modal-header">
#                         <h5 class="modal-title">赞助站点</h5>
#                         <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
#                                 aria-hidden="true">&times;</span></button>
#                     </div>

#                     <div class="modal-body">

#                         <p class="lead">本项目致力于提供即时、便捷的 Steam 余额兑换解决方案</p>

#                         <p>如果想支持站点的维护与后续开发，您可以选择赞助站点。</p>

#                         <p>这将帮助我们应对开发过程中产生的必要支出（包括服务器费用、流量费用等），让我们走得更远。</p>

#                         <div class="row mb-2">
#                             <div class="col" align="center">
#                                 <h5 class="text-center font-weight-light">支付宝</h5>
#                                 <img src="" class="lazy_load" data-src="/static/user/zfb.jpg" height="160">
#                             </div>
#                             <div class="col" align="center">
#                                 <h5 class="text-center font-weight-light">微信</h5>
#                                 <img src="" class="lazy_load" data-src="/static/user/wx.jpg" height="160">
#                             </div>
#                         </div>
#                     </div>

#                 </div>
#             </div>
#         </div>

#     </div>
# </body>

# </html>

 # I want to use re to give me a dict like this
    '''
    nested_dict[0] = {
    'chn_name': '印花 | Outsiders | 2022年里约热内卢锦标赛',
    'eng_name': 'Sticker | Outsiders | Rio 2022',
    'time': 37m 55s,
    'ratio': {
        'first_ratio': 0.760,
        'first_ratio': 0.770,
        'first_ratio': 0.776
    }
    }
    '''
    def parse_html(text:str):
        # match chinese name and eng name
        name_pattern = re.compile(r'<td class="text-left"><a href=".*?">(.*?)</a></td>')
        chn_name, eng_name = re.findall(name_pattern, text)[0]

        # match time
        time_pattern = re.compile(r'<td class="text-left"><a href=".*?">(.*?)</a></td>')
        time = re.findall(time_pattern, text)[0]

        # match ratio
        ratio_pattern = re.compile(r'<td class="text-left"><a href=".*?">(.*?)</a></td>')



    # I want to use re to let a html that contains 50 different good to become a dict
    # buff_soup = BeautifulSoup(buff_response.text, "html.parser")
    # c5_soup = BeautifulSoup(c5_response.text, "html.parser")
    # # 在解析网页内容后，需要使用特定的选择器来获取需要的信息。例如，可以使用以下代码来获取所有商品的名称和价格：
    # items = soup.select(".item")
    # for item in items:
    #     name = item.select_one(".item-name").text
    #     price = item.select_one(".item-price").text
    #     print(name, price)
    
    # # 接着，可以使用selenium库来打开buff和c5网站，并自动搜索并购买商�?,打开浏览器并登录buff和c5网站
    # browser = webdriver.Chrome()
    # browser.get("https://www.buff.com/")
    # # 进行登录操作
    
    # # 在buff中搜索需要购买的商品
    # search_box = browser.find_element_by_name("search")
    # search_box.send_keys(name)
    # search_box.send_keys(Keys.RETURN)
    
    # # 在搜索结果中购买商品
    # item = browser.find_element_by_class_name("item")
    # buy_button = item.find_element_by_class_name("buy-button")
    # buy_button.click()
    
    # # 在c5中搜索需要购买的商品
    # browser.get("https://www.c5game.com/")
    # # 进行登录操作
    # # ...
    
    # search_box = browser.find_element_by_id("search-input")
    # search_box.send_keys(name)
    # search_box.send_keys(Keys.RETURN)
    
    # # 在搜索结果中购买商品
    # item = browser.find_element_by_class_name("item")
    # buy_button = item.find_element_by_class_name("buy-button")
    # buy_button.click()
    
    # # 最后，可以使用steam库来登录Steam账号，并在Steam市场中出售购买的商品。可以使用以下代码：
    # # 登录Steam账户
    # username = "your_username"
    # password = "your_password"
    # steam.login(username, password)
    
    # # 定义要购买的商品名称和价�?