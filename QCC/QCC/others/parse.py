#!/usr/bin/env python
# __*__ coding: utf-8 __*__
"""
__author__: lazy
@file: 
@time: 2019/4/2 15:31
@func:
"""
html = '''
<!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge,Chrome=1"> <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no"> <meta name="renderer" content="webkit"> <meta name="author" content="leslie"> <title>百度的搜索结果-企查查</title> <meta name="keywords" content="企查查,企业查询,公司查询,工商查询,企业信用信息查询系统,企业工商信息查询平台,企业财务信息查询,企业信用评价查询,企业纠纷查询,企业现金流查询,企业股权查询,企业负债查询,企业资产查询,企业财报查询,企业失信信息查询,启信宝,天眼查,天眼通"> <meta name="description" content="企查查信息来自国家企业信用信息公示系统，提供企业信息查询,工商查询,企业信用评价查询，企业纠纷查询，企业现金流查询，企业股权查询，企业负债查询，企业资产查询，企业财报查询,公司查询等相关信息查询；帮您快速了解企业信息,企业工商信息,企业信用信息等经营和人员投资状况！"> <link rel="icon" href="/material/theme/chacha/cms/v2/images/favicon.png"> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/bootstrap.css" type="text/css" /> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/font-awesome.min.css" type="text/css" /> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/icon.css" type="text/css" /> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/font.css" type="text/css" /> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/app.css?time=20190326" type="text/css" /> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/common.css?time=20190326" type="text/css" /> <link rel="stylesheet" href="/material/theme/chacha/cms/pro/css/simple-line-icons.css" type="text/css" /> <!--[if lt IE 9]>
    <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/app_ie8.css?time=1508428800" type="text/css" />
    <script src="/material/theme/chacha/cms/v2/js/html5shiv.js"></script>
    <script src="/material/theme/chacha/cms/v2/js/respond.js"></script>
    <![endif]--> <script type="text/javascript" src="/material/js/siteconfig.js?time=20190326"></script> <script src="/material/theme/chacha/cms/v2/js/jquery.min.js"></script> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/qrcode.min.js"></script> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/jquery.scrollTo.js"></script> <script src="/material/theme/chacha/cms/v2/js/bootstrap.js"></script> <script type="text/javascript" src="/material/js/echarts.min.js"></script> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/china.js?time=1508428800"></script> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/chartsUtil.js?time=20190326"></script> <script src="/material/theme/chacha/cms/v2/js/slimscroll/jquery.slimscroll.min.js"></script> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/toastr.css?time=20190326" /> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/moment.js"></script> <script src="/material/theme/chacha/cms/v2/js/toastr.js" type="text/javascript"></script> <script src="/material/theme/chacha/cms/v2/js/custom.js?time=20190326"></script> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/zhuge.js?time=20190326"></script> <script type="text/javascript">
        var userId = '';
    var userGroupid = '';
</script> <script type="text/javascript">
        var qrcodePolling = false;
    </script> </head> <body> <div style="width: 100%;height: 56px;background: transparent;"></div> <header class="header navi-header box-shadow navi-header-fixed"> <div class="container "> <div class="navi-brand"> <a onclick="zhugeTrack('主页-顶部-logo');" href="/" > <img src="/material/theme/chacha/cms/v2/images/logo4.png" class="m-r-sm" alt="企查查"> </a> </div> <form class="navi-form" role="search" action="/search"> <div class="form-group"> <div class="input-group"> <a onclick="clearSearchkey()" id="clearSearchkey" class="clear-searchkey"></a> <input id="headerKey" name="key" onkeydown="searchKeydown(event,2);" class="form-control headerKey" style="font-size: 14px;" type="text" placeholder="请输入企业名称、人名，产品名等，多关键词用空格隔开，如“小米 雷军”" value="百度" autocomplete="off"> <span class="input-group-btn" style="float: left"> <button onclick="" type="submit" class="btn btn-primary top-searchbtn"></button> </span> </div> </div> <section class="panel headerKey header-section" id="header-search-list"></section> </form> <script type="text/javascript">
                    if($('#headerKey').val()){
                        $('#clearSearchkey').show();
                    }
                </script> <script type="text/javascript">
                var pathname_ = window.location.pathname; 
                if(pathname_ == '/search_riskinfo' || pathname_ == '/search_intellectualinfo'){
                    $('#tpsearch').attr('action', pathname_);
                }
            </script> <ul class="navi-nav pull-right"> <li> <a onclick="zhugeTrack('主页-顶部-APP下载');" href="/app" class="dropdown-toggle header-qrcode">
                    APP下载
                  </a> <section class="dropdown-menu qrcode-box"> <img src="/material/theme/chacha/cms/v2/images/header_qrcode@2x.png?t=2"> </section> </li> <li class="head-line">|</li> <li class=""> <a onclick="zhugeTrack('主页-顶部-VIP服务');" href="/vip">VIP服务</a> </li> <li class="head-line">|</li> <li><a onclick="" href="/user_login?back=%2Fsearch%3Fkey%3D%25E7%2599%25BE%25E5%25BA%25A6">登录</a></li> <li  class="head-line">|</li> <li><a onclick="" href="/user_register">免费注册</a></li> </ul> </div> </header> <script type="text/javascript" src="/material/js/jquery.cookie.js"></script> <script type="text/javascript" src="/material/js/jquery.validate.min.js"></script> <script type="text/javascript" src="/material/js/jquery.form.min.js"></script> <script type="text/javascript" src="/material/js/global.js?t=20190326"></script> <style>
    #excelTipsModal .modal-dialog,#filtrationModal .modal-dialog{
        width: 400px;
        margin: 30px auto;
    }
    #excelTipsModalBody{
        width: 100%;
        height: 60px;
    }

    .clearSpan{display: none;}
    
    .navi-header{
        
    }

</style> <div id="V3_SL" class="container"> <div class="row"> <div class="col-md-9 no-padding"> <div style="padding-left: 15px;position: relative;"> <section class="panel b-a  no-shadow m-b"> <div class="panel-heading panel-heading-m b-b"> <span class="font-15 text-dark">
                  小查为你找到&nbsp;<span class="text-danger">13</span>&nbsp;个投资机构/品牌产品
            </span> </div> <div class="clear m-t m-l m-r-lg"> <a class="proinv-scroll-btn prev disable" onclick="proinvScroll(0,this)"> </a> <div class="proinv-scroll" style="width: 4984px;"> <div class="proinv-wrap"> <a onclick="zhugeTrack('查企业-搜索列表页-查看投资机构/品牌产品',{'投资机构/品牌产品名称':'<em>百度</em>投资部'});" href="/company_investor?id=9773d3352e206fef3df91b8757d63b67&from=search&searchkey=%E7%99%BE%E5%BA%A6"> <div class="clearfix"> <div class="col-xs-2"> <div class="proinv-head"> <img src="https://qichacha.oss-cn-qingdao.aliyuncs.com/Investment/logo/9773d3352e206fef3df91b8757d63b67.jpg" onerror="this.src='/material/theme/chacha/cms/v2/images/no_image.png'"> </div> </div> <div class="col-xs-10"> <div class="proinv-name m-l-sm"><span class="name"><em>百度</em>投资部</span> <span class="proinv-status">投资机构</span></div> <div class="m-l-sm"> <span style="width: 155px;display: inline-block;"><span class="text-gray">投资事件：</span>229</span> <span class="text-gray">管理基金：</span>2
                                </div> </div> </div> <div class="m-t proinv-desc"> <span class="text-gray">简介：</span>
                            百度投资部是百度旗下的战略投资部门。
                        </div> </a> </div> <div class="proinv-wrap"> <a onclick="zhugeTrack('查企业-搜索列表页-查看投资机构/项目',{'投资机构/项目名称':'<em>百度</em>'});" href="/product_eba6af68-439d-431e-8698-1393f249bcf5.html"> <div class="clearfix"> <div class="col-xs-2"> <div class="proinv-head"> <img src="https://img.qichacha.com/Product/eba6af68-439d-431e-8698-1393f249bcf5.jpg"> </div> </div> <div class="col-xs-10"> <div class="proinv-name m-l-sm"><span class="name"><em>百度</em></span> <span class="proinv-status">品牌产品</span></div> <div class="m-l-sm"> <span style="min-width: 140px;display: inline-block;"><span class="text-gray">融资信息：</span>债权融资</span> <span class="text-gray">竞品信息：</span>18                                </div> </div> </div> <div class="m-t proinv-desc"> <span class="text-gray">简介：</span>
                            百度是中文搜索引擎、中文网站。百度旗下产品包括：网页搜索、垂直搜索、百度快照、社区产品、框计算、百度云、开发者中心、百度移动、百度推广品牌营销、百度联盟等。
                        </div> </a> </div> <div class="proinv-wrap"> <a onclick="zhugeTrack('查企业-搜索列表页-查看投资机构/项目',{'投资机构/项目名称':'<em>百度</em>视频'});" href="/product_cfa5e9bc-bf2e-436c-af40-b87b7d0c311a.html"> <div class="clearfix"> <div class="col-xs-2"> <div class="proinv-head"> <img src="https://img.qichacha.com/Product/cfa5e9bc-bf2e-436c-af40-b87b7d0c311a.jpg"> </div> </div> <div class="col-xs-10"> <div class="proinv-name m-l-sm"><span class="name"><em>百度</em>视频</span> <span class="proinv-status">品牌产品</span></div> <div class="m-l-sm"> <span style="min-width: 140px;display: inline-block;"><span class="text-gray">融资信息：</span>B轮</span> <span class="text-gray">竞品信息：</span>20                                </div> </div> </div> <div class="m-t proinv-desc"> <span class="text-gray">简介：</span>
                            百度视频是百度旗下视频业务，已收录超过5.8亿条视频内容，覆盖上千家PGC制作机构， 移动端覆盖用户量超过3亿。2016年4月拆分独立发展，专注于PGC内容平台建设。
                        </div> </a> </div> <div class="proinv-wrap"> <a onclick="zhugeTrack('查企业-搜索列表页-查看投资机构/项目',{'投资机构/项目名称':'<em>百度</em>金融'});" href="/product_e2578b82-7d9c-476a-b19e-ad3b3176f768.html"> <div class="clearfix"> <div class="col-xs-2"> <div class="proinv-head"> <img src="https://img.qichacha.com/Product/e2578b82-7d9c-476a-b19e-ad3b3176f768.jpg"> </div> </div> <div class="col-xs-10"> <div class="proinv-name m-l-sm"><span class="name"><em>百度</em>金融</span> <span class="proinv-status">品牌产品</span></div> <div class="m-l-sm"> <span style="min-width: 140px;display: inline-block;"><span class="text-gray">融资信息：</span>-</span> <span class="text-gray">竞品信息：</span>20                                </div> </div> </div> <div class="m-t proinv-desc"> <span class="text-gray">简介：</span>
                            百度金融是一个综合金融服务平台，业务覆盖范围从支付、消费信贷、征信到基金、证券、保险、银行。百度金融已包括百度钱包（支付业务），百度有钱花（消费信贷），百度有钱贷、联盟贷（企业贷款），百度信用分（征信业务），百度理财（理财业务），百信银行（银行业务），百安保险、百度太平洋互联网车险（保险业务），以及百金互联网金融资产交易中心（交易所业务，下称“百金交”）等几大板块。
                        </div> </a> </div> <div class="proinv-wrap"> <a onclick="zhugeTrack('查企业-搜索列表页-查看投资机构/项目',{'投资机构/项目名称':'<em>百度</em>云'});" href="/product_47576360-0530-416f-b9ec-bad9dd06a665.html"> <div class="clearfix"> <div class="col-xs-2"> <div class="proinv-head"> <img src="https://img.qichacha.com/Product/47576360-0530-416f-b9ec-bad9dd06a665.jpg"> </div> </div> <div class="col-xs-10"> <div class="proinv-name m-l-sm"><span class="name"><em>百度</em>云</span> <span class="proinv-status">品牌产品</span></div> <div class="m-l-sm"> <span style="min-width: 140px;display: inline-block;"><span class="text-gray">融资信息：</span>-</span> <span class="text-gray">竞品信息：</span>20                                </div> </div> </div> <div class="m-t proinv-desc"> <span class="text-gray">简介：</span>
                            百度云是百度提供的公有云平台，不断将百度在云计算、大数据、人工智能的技术能力向社会输出。百度云推出了40余款高性能云计算产品，天算、天像、天工三大智能平台，分别提供智能大数据、智能多媒体、智能物联网服务。为社会各个行业提供最安全、高性能、智能的计算和数据处理服务，让智能的云计算成为社会发展的新引擎。
                        </div> </a> </div> <div class="proinv-wrap"> <a onclick="zhugeTrack('查企业-搜索列表页-查看投资机构/项目',{'投资机构/项目名称':'<em>百度</em> CarLife'});" href="/product_2fe85504-936b-439a-b037-bfb153332388.html"> <div class="clearfix"> <div class="col-xs-2"> <div class="proinv-head"> <img src="https://img.qichacha.com/Product/2fe85504-936b-439a-b037-bfb153332388.jpg"> </div> </div> <div class="col-xs-10"> <div class="proinv-name m-l-sm"><span class="name"><em>百度</em> CarLife</span> <span class="proinv-status">品牌产品</span></div> <div class="m-l-sm"> <span style="min-width: 140px;display: inline-block;"><span class="text-gray">融资信息：</span>-</span> <span class="text-gray">竞品信息：</span>20                                </div> </div> </div> <div class="m-t proinv-desc"> <span class="text-gray">简介：</span>
                            百度 CarLife是一个汇集车主在汽车内常用服务的一个手机应用。
                        </div> </a> </div> <div class="proinv-wrap"> <a onclick="zhugeTrack('查企业-搜索列表页-查看投资机构/项目',{'投资机构/项目名称':'<em>百度</em>DuerOS'});" href="/product_963edcd3-ee02-451a-a1e2-7ba1068223db.html"> <div class="clearfix"> <div class="col-xs-2"> <div class="proinv-head"> <img src="https://img.qichacha.com/Product/963edcd3-ee02-451a-a1e2-7ba1068223db.jpg"> </div> </div> <div class="col-xs-10"> <div class="proinv-name m-l-sm"><span class="name"><em>百度</em>DuerOS</span> <span class="proinv-status">品牌产品</span></div> <div class="m-l-sm"> <span style="min-width: 140px;display: inline-block;"><span class="text-gray">融资信息：</span>-</span> <span class="text-gray">竞品信息：</span>20                                </div> </div> </div> <div class="m-t proinv-desc"> <span class="text-gray">简介：</span>
                            DuerOS是一款开放式的操作系统，强调通过自然语言进行语音对话的交互方式，同时借助云端度秘大脑，可不断学习进化，变得更聪明。目前DuerOS已经具备10大垂类、100余项功能，可以为不同行业的合作伙伴赋能，广泛支持手机、电视、音箱、汽车、机器人等多种硬件设备，实现语音控制、日常聊天、直接提供多种O2O服务等的智能化转变。
                        </div> </a> </div> <div class="proinv-wrap"> <a onclick="zhugeTrack('查企业-搜索列表页-查看投资机构/项目',{'投资机构/项目名称':'<em>百度</em>糯米'});" href="/product_e3c75ba2-8923-4d48-a2b3-5bb5bfd78f1d.html"> <div class="clearfix"> <div class="col-xs-2"> <div class="proinv-head"> <img src="https://img.qichacha.com/Product/e3c75ba2-8923-4d48-a2b3-5bb5bfd78f1d.jpg"> </div> </div> <div class="col-xs-10"> <div class="proinv-name m-l-sm"><span class="name"><em>百度</em>糯米</span> <span class="proinv-status">品牌产品</span></div> <div class="m-l-sm"> <span style="min-width: 140px;display: inline-block;"><span class="text-gray">融资信息：</span>被收购</span> <span class="text-gray">竞品信息：</span>10                                </div> </div> </div> <div class="m-t proinv-desc"> <span class="text-gray">简介：</span>
                            百度糯米是一款移动团购软件，集美食、电影、酒店、KTV、外卖、到家、到店付、储值卡等一系列本地生活服务，给用户提供优质、便捷的优惠服务。同时通过团购的方式向消费者推荐高折扣的本地精品生活服务。
                        </div> </a> </div> <div class="proinv-wrap"> <a onclick="zhugeTrack('查企业-搜索列表页-查看投资机构/项目',{'投资机构/项目名称':'<em>百度</em>派'});" href="/product_dc6b9d1a-eabf-40b9-ba67-0d33e5e49b6a.html"> <div class="clearfix"> <div class="col-xs-2"> <div class="proinv-head"> <img src="https://img.qichacha.com/Product/dc6b9d1a-eabf-40b9-ba67-0d33e5e49b6a.jpg"> </div> </div> <div class="col-xs-10"> <div class="proinv-name m-l-sm"><span class="name"><em>百度</em>派</span> <span class="proinv-status">品牌产品</span></div> <div class="m-l-sm"> <span style="min-width: 140px;display: inline-block;"><span class="text-gray">融资信息：</span>-</span> <span class="text-gray">竞品信息：</span>15                                </div> </div> </div> <div class="m-t proinv-desc"> <span class="text-gray">简介：</span>
                            百度派是一个话题讨论社区新平台，将知识的提供者与知识的获取人紧密联系在一起，搭建一个汇集不同观点分享各类知识的平台，可以提自己关心的各类问题，得到想要的答案；也可以选择站内问题，表达自己的观点，为其他用户答疑解惑。
                        </div> </a> </div> <div class="proinv-wrap"> <a onclick="zhugeTrack('查企业-搜索列表页-查看投资机构/项目',{'投资机构/项目名称':'<em>百度</em>魔图'});" href="/product_1713ca12-a07e-4bce-ace6-d09f5932abed.html"> <div class="clearfix"> <div class="col-xs-2"> <div class="proinv-head"> <img src="https://img.qichacha.com/Product/1713ca12-a07e-4bce-ace6-d09f5932abed.jpg"> </div> </div> <div class="col-xs-10"> <div class="proinv-name m-l-sm"><span class="name"><em>百度</em>魔图</span> <span class="proinv-status">品牌产品</span></div> <div class="m-l-sm"> <span style="min-width: 140px;display: inline-block;"><span class="text-gray">融资信息：</span>被收购</span> <span class="text-gray">竞品信息：</span>8                                </div> </div> </div> <div class="m-t proinv-desc"> <span class="text-gray">简介：</span>
                            百度魔图是一款掌上美图工具。魔图致力于在移动互联网领域为用户提供最完美最贴心的图片编辑和分享软件。
                        </div> </a> </div> <div class="proinv-wrap"> <a onclick="zhugeTrack('查企业-搜索列表页-查看投资机构/项目',{'投资机构/项目名称':'<em>百度</em>BaaS'});" href="/product_c3be3b9a-f1b1-4826-bf2a-f140d0e9698f.html"> <div class="clearfix"> <div class="col-xs-2"> <div class="proinv-head"> <img src="https://img.qichacha.com/Product/c3be3b9a-f1b1-4826-bf2a-f140d0e9698f.jpg"> </div> </div> <div class="col-xs-10"> <div class="proinv-name m-l-sm"><span class="name"><em>百度</em>BaaS</span> <span class="proinv-status">品牌产品</span></div> <div class="m-l-sm"> <span style="min-width: 140px;display: inline-block;"><span class="text-gray">融资信息：</span>-</span> <span class="text-gray">竞品信息：</span>6                                </div> </div> </div> <div class="m-t proinv-desc"> <span class="text-gray">简介：</span>
                            百度BaaS是一个区块链开放平台。该平台是百度自研的基于区块链技术的项目，具有“灵活可定制易落地、安全、高性能、开放共建、去中心化、有限信任”六大特点。
百度BaaS的项目名为，百度Trust ，致力于打造最具易用性的区块链工具。以便捷的部署接入、可靠的去中心化信任机制、稳健的服务能力、丰富的运维工具以及过硬的系统性能为目标。依靠底层技术特性，能够安全、高效和低成本的进行追溯和交易，适用于数字货币、支付清算、数字票据、银行征信管理、权益证明和交易所证券交易、保险管理、金融审计等领域。
                        </div> </a> </div> <div class="proinv-wrap"> <a onclick="zhugeTrack('查企业-搜索列表页-查看投资机构/项目',{'投资机构/项目名称':'<em>百度</em>通告平台'});" href="/product_acb3e7fc-e548-425b-8ddd-de8a2008a673.html"> <div class="clearfix"> <div class="col-xs-2"> <div class="proinv-head"> <img src="https://img.qichacha.com/Product/acb3e7fc-e548-425b-8ddd-de8a2008a673.jpg"> </div> </div> <div class="col-xs-10"> <div class="proinv-name m-l-sm"><span class="name"><em>百度</em>通告平台</span> <span class="proinv-status">品牌产品</span></div> <div class="m-l-sm"> <span style="min-width: 140px;display: inline-block;"><span class="text-gray">融资信息：</span>-</span> <span class="text-gray">竞品信息：</span>20                                </div> </div> </div> <div class="m-t proinv-desc"> <span class="text-gray">简介：</span>
                            百度通告平台是一款即时消息推送类产品，它旨在通过语音电话、短信、邮件、百度Hi及第三方社交、通讯类渠道保证对消息及时、准确、无遗漏地传送。并基于多种渠道构建运维事件管理、报警升级、通告群发、轮值和验证码等应用与服务。
                        </div> </a> </div> <div class="proinv-wrap"> <a onclick="zhugeTrack('查企业-搜索列表页-查看投资机构/项目',{'投资机构/项目名称':'太合音乐人'});" href="/product_7f3da51e-1f4e-4270-a3c6-997d57c53ce3.html"> <div class="clearfix"> <div class="col-xs-2"> <div class="proinv-head"> <img src="https://img.qichacha.com/Product/7f3da51e-1f4e-4270-a3c6-997d57c53ce3.jpg"> </div> </div> <div class="col-xs-10"> <div class="proinv-name m-l-sm"><span class="name">太合音乐人</span> <span class="proinv-status">品牌产品</span></div> <div class="m-l-sm"> <span style="min-width: 140px;display: inline-block;"><span class="text-gray">融资信息：</span>-</span> <span class="text-gray">竞品信息：</span>20                                </div> </div> </div> <div class="m-t proinv-desc"> <span class="text-gray">简介：</span>
                            太合音乐人，是一款为音乐人提供作品管理、信息展示、与乐迷互动等服务的音乐产品，平台内聚集了上万优质音乐人，覆盖十几个音乐流派，持续为音乐爱好者发掘最新鲜、独特的音乐人及作品，致力于打造音乐人和音乐爱好者专属的社交平台，形成国内独居特色的音乐文化生态圈。
                        </div> </a> </div> </div> <div class="prvinv-mengban"></div> <a class="proinv-scroll-btn next" onclick="proinvScroll(1,this)"></a> </div> </section> </div> <script type="text/javascript">
    var proinvScrollIndex = 0;
    function proinvScroll(next,dom){
        if($(dom).hasClass('disable')){
            return;
        }
        var width = parseInt($('.proinv-scroll').css('width'));
        if(next){
            proinvScrollIndex++;
        }else{
            proinvScrollIndex--;
        }
        ml = -proinvScrollIndex*368;
        if(proinvScrollIndex>=0&&proinvScrollIndex<=width/368-2){
            $('.proinv-scroll').css('margin-left',ml+'px');
        }
        if(proinvScrollIndex==0){
           $('.proinv-scroll-btn.prev').addClass('disable'); 
        }else{
            $('.proinv-scroll-btn.prev').removeClass('disable');
        }
        if(proinvScrollIndex==parseInt(width/368)-2){
           $('.proinv-scroll-btn.next').addClass('disable'); 
        }else{
            $('.proinv-scroll-btn.next').removeClass('disable');
        }
    }
    var isWebkit = false;
    if (navigator.userAgent.indexOf('Chrome') > -1 || 
     navigator.userAgent.indexOf('Safari') > -1) {
        isWebkit = true;
     }
    var proinvDesc = $('.proinv-desc');
    for(var i=0;i<proinvDesc.length;i++){
        if(proinvDesc[i].scrollHeight>40 && !isWebkit){
            proinvDesc.eq(i).append('<div class="more">…</div>');
        }
        
    }
</script> <div class="col-md-12 search-sidebar hidden-xs no-padding-right" id="smartBox"> <div class="v3_sl_tab"> <a onclick="" href="/search?key=百度" class="active">公司</a> <a onclick="" href="/search_riskinfo?key=百度" class="">风险信息</a> <a onclick="" href="/search_intellectualinfo?key=百度" class="">知识产权</a> <a class="pull-right text-gray" style="padding-right: 25px;" id="hideSearchBox"><span>收起</span> <i class="i i-arrow-up4"></i></a> </div> <section class="panel b-a n-s" id="search-options"> <div id="SearchBox"> <div class="panel panel-default clearfix" id="appendBox" style="padding: 0px 0px 5px 0px;display: none;border:none;border-bottom: 1px dashed #ccc;box-shadow:none;margin-bottom:10px; "> <span class="font-15 text-dark m-l" id="has_condition"></span> <span class="m-l label btn-primary indexChoosen appendSpan clearSpan" data-option="index" style="display:none;padding:5px;cursor:pointer;"></span> <span class="m-l label btn-primary searchTypeChoosen appendSpan clearSpan" data-option="searchType" style="display:none;padding:5px;cursor:pointer;"></span> <span class="m-l label btn-primary coyTypeChoosen appendSpan clearSpan" data-option="coyType" style="display:none;padding:5px;cursor:pointer;"></span> <span class="m-l label btn-primary statusCodeChoosen appendSpan clearSpan" data-option="statusCode" style="display:none;padding:5px;cursor:pointer"></span> <span class="m-l label btn-primary registfundChoosen appendSpan clearSpan" data-option="registfund" style="display:none;padding:5px;cursor:pointer"></span> <span class="m-l label btn-primary startDateChoosen appendSpan clearSpan" data-option="startDate" style="display:none;padding:5px;cursor:pointer"></span> <span class="m-l label btn-primary provinceChoosen appendSpan clearSpan" data-option="province" style="display:none;padding:5px;cursor:pointer"></span> <span class="m-l label btn-primary cityChoosen appendSpan clearSpan" data-option="city" style="display:none;padding:5px;cursor:pointer"></span> <span class="m-l label btn-primary countyChoosen appendSpan clearSpan" data-option="county" style="display:none;padding:5px;cursor:pointer"></span> <span class="m-l label btn-primary industrycodeChoosen appendSpan clearSpan" data-option="industrycode" style="display:none;padding:5px;cursor:pointer"></span> <span class="m-l label btn-primary subindustrycodeChoosen appendSpan clearSpan" data-option="subindustrycode" style="display:none;padding:5px;cursor:pointer"></span> <span class="m-l label btn-primary thirdindustrycodeChoosen appendSpan clearSpan" data-option="thirdindustrycode" style="display:none;padding:5px;cursor:pointer"></span> <a href="/search?key=百度" class="m-l clearSpan pull-right" data-option="All" style="padding:5px;cursor:pointer;padding-right:20px;position: relative;top: -5px;">全部清除</a> </div> <dl class="sfilter-tag clearfix indexChoose" id="indexOld"> <div class="pull-left" style="width:76px;"><dt>查找范围</dt></div> <div class="pull-left" style="width:80%;"> <dd> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'查找范围','筛选值':'企业名'});" href="javascript:;" data-option="index" data-value="2" data-append="企业名">
                                        企业名
                                    </a> </dd> <dd> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'查找范围','筛选值':'法人或股东'});" href="javascript:;" data-option="index" data-value="4" data-append="法人或股东">
                                        法人或股东
                                    </a> </dd> <dd> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'查找范围','筛选值':'高管'});" href="javascript:;" data-option="index" data-value="6" data-append="高管">
                                        高管
                                    </a> </dd> <dd> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'查找范围','筛选值':'品牌/产品'});" href="javascript:;" data-option="index" data-value="8" data-append="品牌/产品">
                                        品牌/产品
                                    </a> </dd> <dd> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'查找范围','筛选值':'联系方式'});" href="javascript:;" data-option="index" data-value="10" data-append="联系方式">
                                        联系方式
                                    </a> </dd> <dd> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'查找范围','筛选值':'经营范围'});" href="javascript:;" data-option="index" data-value="12" data-append="经营范围">
                                        经营范围
                                    </a> </dd> </div> </dl> <dl class="sfilter-tag clearfix provinceChoose" id="provinceOld"> <div class="pull-left" style="width:76px;"><dt>省份地区</dt></div> <div class="pull-left" style="width:80%;"> <dd class="province-dd" style="display:none;" > </dd> <dd > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'安徽'});" href="javascript:;" data-option="province" data-value="AH" data-append="安徽" class="showCity">
                                        安徽 (<span class="text-gray">564</span>)
                                    </a> </dd> <dd > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'北京'});" href="javascript:;" data-option="province" data-value="BJ" data-append="北京" class="showCity">
                                        北京 (<span class="text-gray">222</span>)
                                    </a> </dd> <dd > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'重庆'});" href="javascript:;" data-option="province" data-value="CQ" data-append="重庆" class="showCity">
                                        重庆 (<span class="text-gray">116</span>)
                                    </a> </dd> <dd > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'福建'});" href="javascript:;" data-option="province" data-value="FJ" data-append="福建" class="showCity">
                                        福建 (<span class="text-gray">724</span>)
                                    </a> </dd> <dd > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'广东'});" href="javascript:;" data-option="province" data-value="GD" data-append="广东" class="showCity">
                                        广东 (<span class="text-gray">1289</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'甘肃'});" href="javascript:;" data-option="province" data-value="GS" data-append="甘肃" class="showCity">
                                        甘肃 (<span class="text-gray">275</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'广西'});" href="javascript:;" data-option="province" data-value="GX" data-append="广西" class="showCity">
                                        广西 (<span class="text-gray">519</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'贵州'});" href="javascript:;" data-option="province" data-value="GZ" data-append="贵州" class="showCity">
                                        贵州 (<span class="text-gray">434</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'海南'});" href="javascript:;" data-option="province" data-value="HAIN" data-append="海南" class="showCity">
                                        海南 (<span class="text-gray">123</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'河北'});" href="javascript:;" data-option="province" data-value="HB" data-append="河北" class="showCity">
                                        河北 (<span class="text-gray">1236</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'河南'});" href="javascript:;" data-option="province" data-value="HEN" data-append="河南" class="showCity">
                                        河南 (<span class="text-gray">1326</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'香港特别行政区'});" href="javascript:;" data-option="province" data-value="HK" data-append="香港特别行政区" class="showCity">
                                        香港特别行政区 (<span class="text-gray">83</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'黑龙江'});" href="javascript:;" data-option="province" data-value="HLJ" data-append="黑龙江" class="showCity">
                                        黑龙江 (<span class="text-gray">563</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'湖北'});" href="javascript:;" data-option="province" data-value="HUB" data-append="湖北" class="showCity">
                                        湖北 (<span class="text-gray">387</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'湖南'});" href="javascript:;" data-option="province" data-value="HUN" data-append="湖南" class="showCity">
                                        湖南 (<span class="text-gray">596</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'吉林'});" href="javascript:;" data-option="province" data-value="JL" data-append="吉林" class="showCity">
                                        吉林 (<span class="text-gray">598</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'江苏'});" href="javascript:;" data-option="province" data-value="JS" data-append="江苏" class="showCity">
                                        江苏 (<span class="text-gray">1119</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'江西'});" href="javascript:;" data-option="province" data-value="JX" data-append="江西" class="showCity">
                                        江西 (<span class="text-gray">307</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'辽宁'});" href="javascript:;" data-option="province" data-value="LN" data-append="辽宁" class="showCity">
                                        辽宁 (<span class="text-gray">750</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'内蒙古'});" href="javascript:;" data-option="province" data-value="NMG" data-append="内蒙古" class="showCity">
                                        内蒙古 (<span class="text-gray">533</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'宁夏'});" href="javascript:;" data-option="province" data-value="NX" data-append="宁夏" class="showCity">
                                        宁夏 (<span class="text-gray">143</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'青海'});" href="javascript:;" data-option="province" data-value="QH" data-append="青海" class="showCity">
                                        青海 (<span class="text-gray">67</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'陕西'});" href="javascript:;" data-option="province" data-value="SAX" data-append="陕西" class="showCity">
                                        陕西 (<span class="text-gray">726</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'四川'});" href="javascript:;" data-option="province" data-value="SC" data-append="四川" class="showCity">
                                        四川 (<span class="text-gray">909</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'山东'});" href="javascript:;" data-option="province" data-value="SD" data-append="山东" class="showCity">
                                        山东 (<span class="text-gray">5860</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'上海'});" href="javascript:;" data-option="province" data-value="SH" data-append="上海" class="showCity">
                                        上海 (<span class="text-gray">68</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'山西'});" href="javascript:;" data-option="province" data-value="SX" data-append="山西" class="showCity">
                                        山西 (<span class="text-gray">399</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'天津'});" href="javascript:;" data-option="province" data-value="TJ" data-append="天津" class="showCity">
                                        天津 (<span class="text-gray">110</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'台湾省'});" href="javascript:;" data-option="province" data-value="TW" data-append="台湾省" class="showCity">
                                        台湾省 (<span class="text-gray">19</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'新疆'});" href="javascript:;" data-option="province" data-value="XJ" data-append="新疆" class="showCity">
                                        新疆 (<span class="text-gray">294</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'西藏'});" href="javascript:;" data-option="province" data-value="XZ" data-append="西藏" class="showCity">
                                        西藏 (<span class="text-gray">25</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'云南'});" href="javascript:;" data-option="province" data-value="YN" data-append="云南" class="showCity">
                                        云南 (<span class="text-gray">734</span>)
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'省份地区','筛选值':'浙江'});" href="javascript:;" data-option="province" data-value="ZJ" data-append="浙江" class="showCity">
                                        浙江 (<span class="text-gray">983</span>)
                                    </a> </dd> </div> <a class="btn btn-link btn-sm pull-right v3_a_more" id="show-province" style="margin-top:-4px;"><span>更多</span> <i class="i i-arrow-down4"></i></a> </dl> <dl class="sfilter-tag clearfix cityChoose" id="cityOld" style="display: none"> <div class="pull-left" style="width:76px;"><dt>城市</dt></div> <div class="pull-left" style="width:80%;" id="city_show"> </div> </dl> <dl class="sfilter-tag clearfix countyChoose" id="countyOld" style="display: none"> <div class="pull-left" style="width:76px;"><dt>区县</dt></div> <div class="pull-left" style="width:80%;" id="county_show"> </div> </dl> <dl class="sfilter-tag clearfix industrycodeChoose" id="industrycodeOld"> <div class="pull-left" style="width:76px;"><dt>行业门类</dt></div> <div class="pull-left" style="width:80%;"> <dd > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'农、林、牧、渔业'});" href="javascript:;" data-option="industrycode" data-value="A" data-append="农、林、牧、渔业">
                                        农、林、牧、渔业 (<span class="text-gray">91</span>)
                                    </a> </dd> <dd > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'采矿业'});" href="javascript:;" data-option="industrycode" data-value="B" data-append="采矿业">
                                        采矿业 (<span class="text-gray">3</span>)
                                    </a> </dd> <dd > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'制造业'});" href="javascript:;" data-option="industrycode" data-value="C" data-append="制造业">
                                        制造业 (<span class="text-gray">764</span>)
                                    </a> </dd> <dd > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'电力、热力、燃气及水生产和供应业'});" href="javascript:;" data-option="industrycode" data-value="D" data-append="电力、热力、燃气及水生产和供应业">
                                        电力、热力、燃气及水生产和供应业 (<span class="text-gray">1</span>)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'建筑业'});" href="javascript:;" data-option="industrycode" data-value="E" data-append="建筑业">
                                        建筑业 (<span class="text-gray">286</span>)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'批发和零售业'});" href="javascript:;" data-option="industrycode" data-value="F" data-append="批发和零售业">
                                        批发和零售业 (<span class="text-gray">12470</span>)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'交通运输、仓储和邮政业'});" href="javascript:;" data-option="industrycode" data-value="G" data-append="交通运输、仓储和邮政业">
                                        交通运输、仓储和邮政业 (<span class="text-gray">59</span>)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'住宿和餐饮业'});" href="javascript:;" data-option="industrycode" data-value="H" data-append="住宿和餐饮业">
                                        住宿和餐饮业 (<span class="text-gray">3183</span>)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'信息传输、软件和信息技术服务业'});" href="javascript:;" data-option="industrycode" data-value="I" data-append="信息传输、软件和信息技术服务业">
                                        信息传输、软件和信息技术服务业 (<span class="text-gray">498</span>)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'金融业'});" href="javascript:;" data-option="industrycode" data-value="J" data-append="金融业">
                                        金融业 (<span class="text-gray">59</span>)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'房地产业'});" href="javascript:;" data-option="industrycode" data-value="K" data-append="房地产业">
                                        房地产业 (<span class="text-gray">257</span>)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'租赁和商务服务业'});" href="javascript:;" data-option="industrycode" data-value="L" data-append="租赁和商务服务业">
                                        租赁和商务服务业 (<span class="text-gray">968</span>)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'科学研究和技术服务业'});" href="javascript:;" data-option="industrycode" data-value="M" data-append="科学研究和技术服务业">
                                        科学研究和技术服务业 (<span class="text-gray">400</span>)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'水利、环境和公共设施管理业'});" href="javascript:;" data-option="industrycode" data-value="N" data-append="水利、环境和公共设施管理业">
                                        水利、环境和公共设施管理业 (<span class="text-gray">17</span>)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'居民服务、修理和其他服务业'});" href="javascript:;" data-option="industrycode" data-value="O" data-append="居民服务、修理和其他服务业">
                                        居民服务、修理和其他服务业 (<span class="text-gray">2199</span>)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'教育'});" href="javascript:;" data-option="industrycode" data-value="P" data-append="教育">
                                        教育 (<span class="text-gray">26</span>)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'卫生和社会工作'});" href="javascript:;" data-option="industrycode" data-value="Q" data-append="卫生和社会工作">
                                        卫生和社会工作 (<span class="text-gray">16</span>)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'文化、体育和娱乐业'});" href="javascript:;" data-option="industrycode" data-value="R" data-append="文化、体育和娱乐业">
                                        文化、体育和娱乐业 (<span class="text-gray">564</span>)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'公共管理、社会保障和社会组织'});" href="javascript:;" data-option="industrycode" data-value="S" data-append="公共管理、社会保障和社会组织">
                                        公共管理、社会保障和社会组织 (<span class="text-gray">4</span>)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'国际组织'});" href="javascript:;" data-option="industrycode" data-value="T" data-append="国际组织">
                                        国际组织 (<span class="text-gray">34</span>)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'行业门类','筛选值':'其他行业'});" href="javascript:;" data-option="industrycode" data-value="0" data-append="其他行业">
                                        其他行业 (<span class="text-gray">307</span>)
                                    </a> </dd> </div> <a class="btn btn-link btn-sm pull-right v3_a_more" id="show-industrycode" style="margin-top:-4px;"><span>更多</span> <i class="i i-arrow-down4"></i></a> </dl> <dl class="sfilter-tag clearfix subindustrycodeChoose" id="subindustrycodeOld" style="display: none"> <div class="pull-left" style="width:76px;"><dt>行业大类</dt></div> <div class="pull-left" style="width:80%;" id="subindustrycode_show"> </div> </dl> <dl class="sfilter-tag clearfix thirdindustrycodeChoose" id="thirdindustrycodeOld" style="display: none"> <div class="pull-left" style="width:76px;"><dt>行业</dt></div> <div class="pull-left" style="width:80%;" id="thirdindustrycode_show"> </div> </dl> <dl class="sfilter-tag clearfix" id="sotherOld"> <div class="pull-left" style="width:76px;"><dt>更多筛选</dt> </div> <dd class="startDateChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" data-toggle="dropdown"><span class="x">成立日期</span> <span class="caret"></span></span> <ul class="dropdown-menu" style="width: 155px;"> <div class="drop-scroll" id="nstartdateOld"> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2019'});" href="javascript:;" data-option="startDate" data-value="2019" data-append="2019">2019 (<span class="text-gray">603</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2018'});" href="javascript:;" data-option="startDate" data-value="2018" data-append="2018">2018 (<span class="text-gray">2443</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2017'});" href="javascript:;" data-option="startDate" data-value="2017" data-append="2017">2017 (<span class="text-gray">2044</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2016'});" href="javascript:;" data-option="startDate" data-value="2016" data-append="2016">2016 (<span class="text-gray">1965</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2015'});" href="javascript:;" data-option="startDate" data-value="2015" data-append="2015">2015 (<span class="text-gray">2104</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2014'});" href="javascript:;" data-option="startDate" data-value="2014" data-append="2014">2014 (<span class="text-gray">1448</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2013'});" href="javascript:;" data-option="startDate" data-value="2013" data-append="2013">2013 (<span class="text-gray">1483</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2012'});" href="javascript:;" data-option="startDate" data-value="2012" data-append="2012">2012 (<span class="text-gray">1366</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2011'});" href="javascript:;" data-option="startDate" data-value="2011" data-append="2011">2011 (<span class="text-gray">1401</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2010'});" href="javascript:;" data-option="startDate" data-value="2010" data-append="2010">2010 (<span class="text-gray">1227</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2009'});" href="javascript:;" data-option="startDate" data-value="2009" data-append="2009">2009 (<span class="text-gray">1287</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2008'});" href="javascript:;" data-option="startDate" data-value="2008" data-append="2008">2008 (<span class="text-gray">1002</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2007'});" href="javascript:;" data-option="startDate" data-value="2007" data-append="2007">2007 (<span class="text-gray">1021</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2006'});" href="javascript:;" data-option="startDate" data-value="2006" data-append="2006">2006 (<span class="text-gray">778</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2005'});" href="javascript:;" data-option="startDate" data-value="2005" data-append="2005">2005 (<span class="text-gray">505</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2004'});" href="javascript:;" data-option="startDate" data-value="2004" data-append="2004">2004 (<span class="text-gray">446</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2003'});" href="javascript:;" data-option="startDate" data-value="2003" data-append="2003">2003 (<span class="text-gray">263</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2002'});" href="javascript:;" data-option="startDate" data-value="2002" data-append="2002">2002 (<span class="text-gray">134</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2001'});" href="javascript:;" data-option="startDate" data-value="2001" data-append="2001">2001 (<span class="text-gray">132</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'2000'});" href="javascript:;" data-option="startDate" data-value="2000" data-append="2000">2000 (<span class="text-gray">115</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'1999'});" href="javascript:;" data-option="startDate" data-value="1999" data-append="1999">1999 (<span class="text-gray">65</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'1998'});" href="javascript:;" data-option="startDate" data-value="1998" data-append="1998">1998 (<span class="text-gray">43</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'1997'});" href="javascript:;" data-option="startDate" data-value="1997" data-append="1997">1997 (<span class="text-gray">34</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'1996'});" href="javascript:;" data-option="startDate" data-value="1996" data-append="1996">1996 (<span class="text-gray">32</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'1995'});" href="javascript:;" data-option="startDate" data-value="1995" data-append="1995">1995 (<span class="text-gray">22</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'1994'});" href="javascript:;" data-option="startDate" data-value="1994" data-append="1994">1994 (<span class="text-gray">21</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'1993'});" href="javascript:;" data-option="startDate" data-value="1993" data-append="1993">1993 (<span class="text-gray">20</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'1992'});" href="javascript:;" data-option="startDate" data-value="1992" data-append="1992">1992 (<span class="text-gray">12</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'1991'});" href="javascript:;" data-option="startDate" data-value="1991" data-append="1991">1991 (<span class="text-gray">5</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'1990'});" href="javascript:;" data-option="startDate" data-value="1990" data-append="1990">1990 (<span class="text-gray">8</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'1989'});" href="javascript:;" data-option="startDate" data-value="1989" data-append="1989">1989 (<span class="text-gray">51</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'1987'});" href="javascript:;" data-option="startDate" data-value="1987" data-append="1987">1987 (<span class="text-gray">3</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'1986'});" href="javascript:;" data-option="startDate" data-value="1986" data-append="1986">1986 (<span class="text-gray">3</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'1985'});" href="javascript:;" data-option="startDate" data-value="1985" data-append="1985">1985 (<span class="text-gray">3</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'1984'});" href="javascript:;" data-option="startDate" data-value="1984" data-append="1984">1984 (<span class="text-gray">1</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'1983'});" href="javascript:;" data-option="startDate" data-value="1983" data-append="1983">1983 (<span class="text-gray">3</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'1982'});" href="javascript:;" data-option="startDate" data-value="1982" data-append="1982">1982 (<span class="text-gray">3</span>)</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'1981'});" href="javascript:;" data-option="startDate" data-value="1981" data-append="1981">1981 (<span class="text-gray">1</span>)</a></li> </div> <li> <a data-option="x" class="fundrange-dropdown" onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'成立日期','筛选值':'自定义'});"> <span id="registDate" class="dropdown-toggle i-s" data-toggle="dropdown"><span class="x">自定义</span> <span class="fa fa-caret-right"></span></span> <section class="dropdown-menu fundrange registdate"> <div><span>从</span> <input id="registDateStart" class="form-control" type="text"/></div> <div><span>至</span> <input id="registDateEnd" class="form-control" type="text"/></div> <span id="registDateBtn">确定</span> </section> </a> </li> </ul> </span> </dd> <dd class="statusCodeChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" data-toggle="dropdown"><span class="x">企业状态</span> <span class="caret"></span></span> <ul class="dropdown-menu" style="padding-top: 0px;padding-bottom: 0px;"> <div class="drop-scroll" id="nstatuscodeOld"> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'企业状态','筛选值':'在业'});" href="javascript:;" data-option="statusCode" data-value="10" data-append="在业">在业</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'企业状态','筛选值':'存续'});" href="javascript:;" data-option="statusCode" data-value="20" data-append="存续">存续</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'企业状态','筛选值':'筹建'});" href="javascript:;" data-option="statusCode" data-value="30" data-append="筹建">筹建</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'企业状态','筛选值':'清算'});" href="javascript:;" data-option="statusCode" data-value="40" data-append="清算">清算</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'企业状态','筛选值':'迁入'});" href="javascript:;" data-option="statusCode" data-value="50" data-append="迁入">迁入</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'企业状态','筛选值':'迁出'});" href="javascript:;" data-option="statusCode" data-value="60" data-append="迁出">迁出</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'企业状态','筛选值':'停业'});" href="javascript:;" data-option="statusCode" data-value="70" data-append="停业">停业</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'企业状态','筛选值':'撤销'});" href="javascript:;" data-option="statusCode" data-value="80" data-append="撤销">撤销</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'企业状态','筛选值':'吊销'});" href="javascript:;" data-option="statusCode" data-value="90" data-append="吊销">吊销</a></li> <li><a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'企业状态','筛选值':'注销'});" href="javascript:;" data-option="statusCode" data-value="99" data-append="注销">注销</a></li> </div> </ul> </span> </dd> <dd class="registfundChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" data-toggle="dropdown"><span class="x">注册资本</span> <span class="caret"></span></span> <ul class="dropdown-menu" style="width: 155px;"> <div class="drop-scroll"> <li> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'注册资本','筛选值':'500万以下'});" href="javascript:;" data-option="registfund" data-value="0-500" data-append="500万以下">500万以下</a> </li> <li> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'注册资本','筛选值':'500~1000万'});" href="javascript:;" data-option="registfund" data-value="500-1000" data-append="500~1000万">500~1000万</a> </li> <li> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'注册资本','筛选值':'1000~5000万'});" href="javascript:;" data-option="registfund" data-value="1000-5000" data-append="1000~5000万">1000~5000万</a> </li> <li> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'注册资本','筛选值':'5000万以上'});" href="javascript:;" data-option="registfund" data-value="5000-0" data-append="5000万以上">5000万以上</a> </li> </div> <li> <a data-option="x" class="fundrange-dropdown" onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'注册资本','筛选值':'自定义'});"> <span id="registfundRange" class="dropdown-toggle i-s" data-toggle="dropdown"><span class="x">自定义</span> <span class="fa fa-caret-right"></span></span> <section class="dropdown-menu fundrange"> <div><span>从</span> <input id="fundStart" class="form-control" type="text"/></div> <div><span>至</span> <input id="fundEnd" class="form-control" type="text"/></div> <span id="fundBtn">确定</span> </section> </a> </li> </ul> </span> </dd> <dd class="searchTypeChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" data-toggle="dropdown"><span class="x">机构类型</span> <span class="caret"></span></span> <ul class="dropdown-menu"> <li> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'机构类型','筛选值':'企业'});" href="javascript:;" data-option="searchType" data-value="0" data-append="企业">
                                                企业
                                            </a> </li> <li> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'机构类型','筛选值':'社会组织'});" href="javascript:;" data-option="searchType" data-value="1" data-append="社会组织">
                                                社会组织
                                            </a> </li> <li> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'机构类型','筛选值':'香港公司'});" href="javascript:;" data-option="searchType" data-value="3" data-append="香港公司">
                                                香港公司
                                            </a> </li> <li> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'机构类型','筛选值':'台湾公司'});" href="javascript:;" data-option="searchType" data-value="5" data-append="台湾公司">
                                                台湾公司
                                            </a> </li> </ul> </span> </dd> <dd class="coyTypeChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" data-toggle="dropdown"><span class="x">企业类型</span> <span class="caret"></span></span> <ul class="dropdown-menu"> <li> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'企业类型','筛选值':'有限责任公司'});" href="javascript:;" data-option="coyType" data-value="10" data-append="有限责任公司">
                                                有限责任公司
                                            </a> </li> <li> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'企业类型','筛选值':'股份有限公司'});" href="javascript:;" data-option="coyType" data-value="20" data-append="股份有限公司">
                                                股份有限公司
                                            </a> </li> <li> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'企业类型','筛选值':'国企'});" href="javascript:;" data-option="coyType" data-value="30" data-append="国企">
                                                国企
                                            </a> </li> <li> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'企业类型','筛选值':'外商投资企业'});" href="javascript:;" data-option="coyType" data-value="40" data-append="外商投资企业">
                                                外商投资企业
                                            </a> </li> <li> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'企业类型','筛选值':'独资企业'});" href="javascript:;" data-option="coyType" data-value="50" data-append="独资企业">
                                                独资企业
                                            </a> </li> <li> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'企业类型','筛选值':'合伙制企业'});" href="javascript:;" data-option="coyType" data-value="60" data-append="合伙制企业">
                                                合伙制企业
                                            </a> </li> <li> <a onclick="zhugeTrack('查企业-搜索列表页-筛选项',{'筛选项':'企业类型','筛选值':'个体工商户'});" href="javascript:;" data-option="coyType" data-value="70" data-append="个体工商户">
                                                个体工商户
                                            </a> </li> </ul> </span> </dd> </dl> <div class="sfilter-tag clearfix"> <div class="pull-left" style="width:76px;"><dt class="text-vip">VIP筛选</dt> </div> <div class="pull-left" style="width:80%;"> <dd class="telChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" onclick="showVipModal('高级筛选功能','成为VIP会员 即可查询企业状态、电话、邮箱、商标、专利、融资、上市等高级筛选','gjsx',null,null,null);zhugeTrack('查企业-搜索列表页-高级筛选-开通VIP');"><span class="x">联系电话</span> <span class="caret"></span></span> </span> </dd> <dd class="phoneChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" onclick="showVipModal('高级筛选功能','成为VIP会员 即可查询企业状态、电话、邮箱、商标、专利、融资、上市等高级筛选','gjsx',null,null,null);zhugeTrack('查企业-搜索列表页-高级筛选-开通VIP');"><span class="x">手机号码</span> <span class="caret"></span></span> </span> </dd> <dd class="emailChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" onclick="showVipModal('高级筛选功能','成为VIP会员 即可查询企业状态、电话、邮箱、商标、专利、融资、上市等高级筛选','gjsx',null,null,null);zhugeTrack('查企业-搜索列表页-高级筛选-开通VIP');"><span class="x">联系邮箱</span> <span class="caret"></span></span> </span> </dd> <dd class="websiteChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" onclick="showVipModal('高级筛选功能','成为VIP会员 即可查询企业状态、电话、邮箱、商标、专利、融资、上市等高级筛选','gjsx',null,null,null);zhugeTrack('查企业-搜索列表页-高级筛选-开通VIP');"><span class="x">网站信息</span> <span class="caret"></span></span> </span> </dd> <dd class="gwebsiteChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" onclick="showVipModal('高级筛选功能','成为VIP会员 即可查询企业状态、电话、邮箱、商标、专利、融资、上市等高级筛选','gjsx',null,null,null);zhugeTrack('查企业-搜索列表页-高级筛选-开通VIP');"><span class="x">网址信息</span> <span class="caret"></span></span> </span> </dd> <dd class="markChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" onclick="showVipModal('高级筛选功能','成为VIP会员 即可查询企业状态、电话、邮箱、商标、专利、融资、上市等高级筛选','gjsx',null,null,null);zhugeTrack('查企业-搜索列表页-高级筛选-开通VIP');"><span class="x">商标信息</span> <span class="caret"></span></span> </span> </dd> <dd class="patentChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" onclick="showVipModal('高级筛选功能','成为VIP会员 即可查询企业状态、电话、邮箱、商标、专利、融资、上市等高级筛选','gjsx',null,null,null);zhugeTrack('查企业-搜索列表页-高级筛选-开通VIP');"><span class="x">专利信息</span> <span class="caret"></span></span> </span> </dd> <dd class="financeChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" onclick="showVipModal('高级筛选功能','成为VIP会员 即可查询企业状态、电话、邮箱、商标、专利、融资、上市等高级筛选','gjsx',null,null,null);zhugeTrack('查企业-搜索列表页-高级筛选-开通VIP');"><span class="x">融资信息</span> <span class="caret"></span></span> </span> </dd> <dd class="listedChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" onclick="showVipModal('高级筛选功能','成为VIP会员 即可查询企业状态、电话、邮箱、商标、专利、融资、上市等高级筛选','gjsx',null,null,null);zhugeTrack('查企业-搜索列表页-高级筛选-开通VIP');"><span class="x">上市状态</span> <span class="caret"></span></span> </span> </dd> <dd class="listedChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" onclick="showVipModal('高级筛选功能','成为VIP会员 即可查询企业状态、电话、邮箱、商标、专利、融资、上市等高级筛选','gjsx',null,null,null);zhugeTrack('查企业-搜索列表页-高级筛选-开通VIP');"><span class="x">失信信息</span> <span class="caret"></span></span> </span> </dd> <dd class="zzqChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" onclick="showVipModal('高级筛选功能','成为VIP会员 即可查询企业状态、电话、邮箱、商标、专利、融资、上市等高级筛选','gjsx',null,null,null);zhugeTrack('查企业-搜索列表页-高级筛选-开通VIP');"><span class="x">著作权</span> <span class="caret"></span></span> </span> </dd> <dd class="rjzzqChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" onclick="showVipModal('高级筛选功能','成为VIP会员 即可查询企业状态、电话、邮箱、商标、专利、融资、上市等高级筛选','gjsx',null,null,null);zhugeTrack('查企业-搜索列表页-高级筛选-开通VIP');"><span class="x">软件著作权</span> <span class="caret"></span></span> </span> </dd> <dd class="insuredChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" onclick="showVipModal('高级筛选功能','成为VIP会员 即可查询企业状态、电话、邮箱、商标、专利、融资、上市等高级筛选','gjsx',null,null,null);zhugeTrack('查企业-搜索列表页-高级筛选-开通VIP');"><span class="x">参保人数</span> <span class="caret"></span></span> </span> </dd> </div> </div> </div> </section> <div class="hideSearchBoxWrap"> </div> </div> <div class="col-md-12 no-padding" id="load_data" style="display: none"> <section class="text-center" style="padding:100px 0;"> <img src="/material/theme/chacha/cms/v2/images/preloader.gif" style="width:70px;margin-top:50px;"/> </section> </div> <div class="col-md-12 no-padding-right" id="ajaxlist"> <div class="panel panel-default m_search_head n-s"> <span class="font-15 text-dark-dk pull-left m-l" id="countOld">
						                                小查为您找到
                                <span class="text-danger">
                                    22206
                                </span>
                            家符合条件的企业
							 
                       </span> </div> <section class="panel b-a n-s" id="searchlist" style="border-top: none;margin-bottom: 0px;"> <div id="srchcheck" class="m_srchcheck"> <a onclick="batchPostcardCancel();zhugeTrack('查企业-搜索列表页-批量联系-取消');" class="btn m-r-sm btn-default">
                            取消
                        </a> <a onclick="batchPostcardSearchAll();zhugeTrack('查企业-搜索列表页-批量联系-全选当页');" class="btn m-r-sm btn-outline-primary"> <span id="srchcheckText">全选当页</span> </a> <a onclick="batchPost();zhugeTrack('查企业-搜索列表页-批量联系-发送');" class="btn m-r-sm btn-primary">
                            发送(<span id="srchcheckNum">0</span>)
                        </a> </div> <iframe id="cxjgIframe" class="vip-iframe" style="display: none;" data-src="/company_vipinsert?type=cxjg" src=""></iframe> <table class="m_srchList"> <tbody id="search-result"> <tr> <td class="checktd" width="20"> <label class="text-dark-lter"> <input type="checkbox" name="batchPostcard" onclick="batchPostcardClick()" value="3f603703d59a04cbe427e5825099a565" data-name="<em><em>百度</em></em>在线网络技术(北京)有限公司" data-email="service-center@baidu.com"> </label> </td> <td class="imgtd" width="110"> <img src="https://co-image.qichacha.com/CompanyImage/3f603703d59a04cbe427e5825099a565.jpg?x-oss-process=style/qcc_cmp" onerror="this.src='https://co-image.qichacha.com/CompanyImage/default.jpg'"> </td> <td> <a onclick="zhugeTrack('查企业-搜索列表页-查看企业',{'企业名称':'<em><em>百度</em></em>在线网络技术(北京)有限公司'});addSearchIndex('百度',1);" href="/firm_3f603703d59a04cbe427e5825099a565.html" target="_blank" class="ma_h1"><em><em>百度</em></em>在线网络技术(北京)有限公司</a> <div class="search-tags"> <span class="ntag text-primary" data-type="108" data-short="" data-extend="GR201411002540">高新技术企业</span> <span class="ntag text-primary" data-type="7" data-short="百度" data-extend="BIDU.NASDAQ">中概股</span> </div> <p class="m-t-xs">
                                                                                                                                                                法定代表人：
                                                                                                                                                                                                        <a onclick="zhugeTrack('查企业-搜索列表页-查看法定代表人',{'人物名称':'向海龙'});" class="text-primary" href="/people?name=%E5%90%91%E6%B5%B7%E9%BE%99&keyno=3f603703d59a04cbe427e5825099a565">向海龙</a> <span class="m-l">注册资本：4520万美元</span> <span class="m-l">成立时间：2000-01-18</span> </p> <p class="m-t-xs">
                                        邮箱：service-center@baidu.com
                                        <span class="m-l">电话：010-59928888</span> <a class="text-primary" onclick="showVipModal('更多号码','成为VIP会员 即可挖掘企业更多联系方式','gdhm');zhugeTrack('查企业-搜索列表页-更多号码-开通VIP');">更多号码</a> </p> <p class="m-t-xs">
                                        地址：北京市海淀区上地十街10号<em>百度</em>大厦三层
                                    </p> <p> <i class="i   i-search"></i>
                                                                                股票简称：<em>百度</em> </td> <td width="100"> <span class="nstatus text-success-lt m-l-xs">在业</span> </td> </tr> <tr> <td class="checktd" width="20"> <label class="text-dark-lter"> <input type="checkbox" name="batchPostcard" onclick="batchPostcardClick()" value="576c21e3468a6b178bbf291e4820e896" data-name="北京<em><em>百度</em></em>网讯科技有限公司" data-email=""> </label> </td> <td class="imgtd" width="110"> <img src="https://co-image.qichacha.com/CompanyImage/576c21e3468a6b178bbf291e4820e896.jpg?x-oss-process=style/qcc_cmp" onerror="this.src='https://co-image.qichacha.com/CompanyImage/default.jpg'"> </td> <td> <a onclick="zhugeTrack('查企业-搜索列表页-查看企业',{'企业名称':'北京<em><em>百度</em></em>网讯科技有限公司'});addSearchIndex('百度',2);" href="/firm_576c21e3468a6b178bbf291e4820e896.html" target="_blank" class="ma_h1">北京<em><em>百度</em></em>网讯科技有限公司</a> <div class="search-tags"> <span class="ntag text-primary" data-type="108" data-short="" data-extend="GR201611005588">高新技术企业</span> <span class="ntag text-primary" data-type="3" data-short="魔图精灵" data-extend="e2e04e33-13c9-4168-980c-6ac395c434cc">被收购</span> <span class="ntag text-primary" data-type="208" data-short="" data-extend="">投资机构</span> </div> <p class="m-t-xs">
                                                                                                                                                                法定代表人：
                                                                                                                                                                                                        <a onclick="zhugeTrack('查企业-搜索列表页-查看法定代表人',{'人物名称':'梁志祥'});" class="text-primary" href="/people?name=%E6%A2%81%E5%BF%97%E7%A5%A5&keyno=576c21e3468a6b178bbf291e4820e896">梁志祥</a> <span class="m-l">注册资本：642128万元人民币</span> <span class="m-l">成立时间：2001-06-05</span> </p> <p class="m-t-xs">
                                        邮箱：-
                                        <span class="m-l">电话：010-59928888</span> <a class="text-primary" onclick="showVipModal('更多号码','成为VIP会员 即可挖掘企业更多联系方式','gdhm');zhugeTrack('查企业-搜索列表页-更多号码-开通VIP');">更多号码</a> </p> <p class="m-t-xs">
                                        地址：北京市海淀区上地十街10号<em>百度</em>大厦2层
                                    </p> </p> </td> <td width="100"> <span class="nstatus text-success-lt m-l-xs">在业</span> </td> </tr> <tr> <td class="checktd" width="20"> <label class="text-dark-lter"> <input type="checkbox" name="batchPostcard" onclick="batchPostcardClick()" value="040087950737026999780939d6a623e9" data-name="<em><em>百度</em></em>国际科技(深圳)有限公司" data-email="limingzhu@sz.baidu.com"> </label> </td> <td class="imgtd" width="110"> <img src="https://co-image.qichacha.com/CompanyImage/040087950737026999780939d6a623e9.jpg?x-oss-process=style/qcc_cmp" onerror="this.src='https://co-image.qichacha.com/CompanyImage/default.jpg'"> <i class="icon-qccrz110"></i> </td> <td> <a onclick="zhugeTrack('查企业-搜索列表页-查看企业',{'企业名称':'<em><em>百度</em></em>国际科技(深圳)有限公司'});addSearchIndex('百度',3);" href="/firm_040087950737026999780939d6a623e9.html" target="_blank" class="ma_h1"><em><em>百度</em></em>国际科技(深圳)有限公司</a> <div class="search-tags"> <span class="ntag text-primary" data-type="108" data-short="" data-extend="GR201744203553">高新技术企业</span> </div> <p class="m-t-xs">
                                                                                                                                                                法定代表人：
                                                                                                                                                                                                        <a onclick="zhugeTrack('查企业-搜索列表页-查看法定代表人',{'人物名称':'向海龙'});" class="text-primary" href="/people?name=%E5%90%91%E6%B5%B7%E9%BE%99&keyno=040087950737026999780939d6a623e9">向海龙</a> <span class="m-l">注册资本：2000万美元</span> <span class="m-l">成立时间：2010-11-23</span> </p> <p class="m-t-xs">
                                        邮箱：limingzhu@sz.baidu.com
                                        <span class="m-l">电话：0755-32996982</span> <a class="text-primary" onclick="showVipModal('更多号码','成为VIP会员 即可挖掘企业更多联系方式','gdhm');zhugeTrack('查企业-搜索列表页-更多号码-开通VIP');">更多号码</a> </p> <p class="m-t-xs">
                                        地址：深圳市南山区粤海街道滨海社区海天一路6号<em>百度</em>国际大厦东塔楼1层
                                    </p> </p> </td> <td width="100"> <span class="nstatus text-success-lt m-l-xs">存续</span> </td> </tr> <tr> <td class="checktd" width="20"> <label class="text-dark-lter"> <input type="checkbox" name="batchPostcard" onclick="batchPostcardClick()" value="418729d5f42a58f5a3d58a567b5315e8" data-name="无锡壹<em><em>百度</em></em>餐饮管理服务有限公司" data-email="1013373811@qq.com"> </label> </td> <td class="imgtd" width="110"> <img src="https://co-image.qichacha.com/CompanyImage/418729d5f42a58f5a3d58a567b5315e8.jpg?x-oss-process=style/qcc_cmp" onerror="this.src='https://co-image.qichacha.com/CompanyImage/default.jpg'"> </td> <td> <a onclick="zhugeTrack('查企业-搜索列表页-查看企业',{'企业名称':'无锡壹<em><em>百度</em></em>餐饮管理服务有限公司'});addSearchIndex('百度',4);" href="/firm_418729d5f42a58f5a3d58a567b5315e8.html" target="_blank" class="ma_h1">无锡壹<em><em>百度</em></em>餐饮管理服务有限公司</a> <div class="search-tags"> <span class="ntag text-primary" data-type="301" data-short="壹百度" data-extend="691712">新四板</span> </div> <p class="m-t-xs">
                                                                                                                                                                法定代表人：
                                                                                                                                                                                                        <a onclick="zhugeTrack('查企业-搜索列表页-查看法定代表人',{'人物名称':'孙自勇'});" class="text-primary" href="/people?name=%E5%AD%99%E8%87%AA%E5%8B%87&keyno=418729d5f42a58f5a3d58a567b5315e8">孙自勇</a> <span class="m-l">注册资本：3100万元人民币</span> <span class="m-l">成立时间：2011-04-12</span> </p> <p class="m-t-xs">
                                        邮箱：1013373811@qq.com
                                        <span class="m-l">电话：0510-81810078</span> <a class="text-primary" onclick="showVipModal('更多号码','成为VIP会员 即可挖掘企业更多联系方式','gdhm');zhugeTrack('查企业-搜索列表页-更多号码-开通VIP');">更多号码</a> </p> <p class="m-t-xs">
                                        地址：无锡市新吴区硕放工业集中区五期A9号地块(振发路332号)
                                    </p> </p> </td> <td width="100"> <span class="nstatus text-success-lt m-l-xs">在业</span> </td> </tr> <tr> <td class="checktd" width="20"> <label class="text-dark-lter"> <input type="checkbox" name="batchPostcard" onclick="batchPostcardClick()" value="h487ba9f25946f686062decf28a824a7" data-name="千<em><em>百度</em></em>国际控股有限公司" data-email="info@cbanner.com.cn"> </label> </td> <td class="imgtd" width="110"> <img src="https://qccdata.qichacha.com/AutoImage/h487ba9f25946f686062decf28a824a7.jpg?x-oss-process=image/resize,w_120" onerror="this.src='https://co-image.qichacha.com/CompanyImage/default.jpg'"> </td> <td> <a onclick="zhugeTrack('查企业-搜索列表页-查看企业',{'企业名称':'千<em><em>百度</em></em>国际控股有限公司'});addSearchIndex('百度',5);" href="/firm_h487ba9f25946f686062decf28a824a7.html" target="_blank" class="ma_h1">千<em><em>百度</em></em>国际控股有限公司</a> <div class="search-tags"> <span class="ntag text-primary">香港公司</span> <span class="ntag text-primary" data-type="401" data-short="千百度" data-extend="01028.HK">香港公司港股</span> <span class="ntag text-primary" data-type="401" data-short="千百度" data-extend="01028.HK">千百度</span> <span class="ntag text-primary" data-type="401" data-short="千百度" data-extend="01028.HK">01028.HK</span> </div> <p class="m-t-xs">
                                        董事长：<a onclick="zhugeTrack('查企业-搜索列表页-查看法定代表人',{'人物名称':'陈奕熙'});" class="text-primary" href="/people?name=%E9%99%88%E5%A5%95%E7%86%99&keyno=h487ba9f25946f686062decf28a824a7">陈奕熙</a> <span class="m-l">股本：300,000,000 USD</span> <span class="m-l">成立时间：2002-04-26</span> </p> <p class="m-t-xs">
                                        邮箱：info@cbanner.com.cn
                                        <span class="m-l">电话：00852-31506788</span> </p> <p class="m-t-xs">
                                        地址：香港夏悫道16号远东金融中心29楼2904室
                                    </p> </p> </td> <td width="100"> <span style="word-break: keep-all;display: inline-block;" class="nstatus text-success-lt m-l-xs">仍注册</span> </td> </tr> </tbody> </table> </section> <div style="text-align:center;"></div> <div class="company-mengban"> <div class="company-vip-kuang"> <div class="company-vip-title m-t"> <p>亲，小查告诉你个秘密:-D</p> <p>登录后可以查看更多数据，免费获取信用报告哦！</p> </div> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="company-vip-btn btn btn-danger m-t">立即登录</a> <a href="/user_register?back=/search?key=百度" class="company-vip-btn btn btn-primary m-t m-l">免费注册</a> </div> </div> </div> </div> <div class="col-md-3"> <div class="m-b"> <a onclick="zhugeTrack('广告-企查查小程序');" href="https://www.qichacha.com/weixin_xcx" target="_blank"> <img src="https://co-image.qichacha.com/upload/chacha/img/20181204/1543903668669241.png" style="width:280px;" alt="企查查"/> </a> </div> <div class="m-b"> <a onclick="zhugeTrack('广告-企查查APP');" href="https://www.qichacha.com/app" target="_blank"> <img src="https://co-image.qichacha.com/upload/chacha/img/20181220/1545299084736231.png" style="width:280px;" alt="企查查"/> </a> </div> <div class="m-b"> <a onclick="zhugeTrack('广告-个税小程序');" href="javascript:;" target="_blank"> <img src="https://co-image.qichacha.com/upload/chacha/img/20181204/1543903674169312.png" style="width:280px;" alt="企查查"/> </a> </div> <div class="m-b"> <a onclick="zhugeTrack('广告-批量导出开通VIP');" href="https://www.qichacha.com/vip" target="_blank"> <img src="https://co-image.qichacha.com/upload/chacha/img/20181204/1543903652205295.png" style="width:280px;" alt="企查查"/> </a> </div> <div class="m-b"> <a onclick="zhugeTrack('广告-一键查询最终受益人');" href="https://www.qichacha.com/firm_9cce0780ab7644008b73bc2120479d31.html#syrlistpos" target="_blank"> <img src="https://co-image.qichacha.com/upload/chacha/img/20181204/1543903663959111.png" style="width:280px;" alt="企查查"/> </a> </div> <div class="m-b"> <a onclick="zhugeTrack('广告-批量查询');" href="https://www.qichacha.com/more_batchsearch" target="_blank"> <img src="https://co-image.qichacha.com/upload/chacha/img/20181204/15439036593224.png" style="width:280px;" alt="企查查"/> </a> </div> <section class="panel b-a n-s" style="width:280px;margin-top:20px;"> <div class="panel-heading b-b" style="font-size:18px;;"> <span class="font-bold font-15 text-dark" style="color:#5c5c5c;">最近浏览</span> </div> <ul class="list-group no-bg auto v3_lastview"> <a href="/firm_b4836f70c27a174a6fb6f9b59f1fae19" target="_blank" class="list-group-item clearfix"> <span class="font-15 clear">中国工商银行股份有限公司陕西自贸区西安国际港务区支行</span> <span class="text-muted text-xs clear"><i class="i i-clock"></i> 12分钟前</span> </a> <a href="/firm_544e11c6b37980d05247e551890e6666" target="_blank" class="list-group-item clearfix"> <span class="font-15 clear">湖南大成天工水务科技有限公司</span> <span class="text-muted text-xs clear"><i class="i i-clock"></i> 12分钟前</span> </a> <a href="/firm_79bb11c8559ea9970672a00d6ccde644" target="_blank" class="list-group-item clearfix"> <span class="font-15 clear">深圳市广汇源环境水务有限公司</span> <span class="text-muted text-xs clear"><i class="i i-clock"></i> 12分钟前</span> </a> <a href="/firm_0024a3983f83a600f3bdc3d57c258df5" target="_blank" class="list-group-item clearfix"> <span class="font-15 clear">文春林--流动</span> <span class="text-muted text-xs clear"><i class="i i-clock"></i> 12分钟前</span> </a> <a href="/firm_002487ebdc13ea9a98d170e3fc7a8083" target="_blank" class="list-group-item clearfix"> <span class="font-15 clear">龚勇--朝阳西路口</span> <span class="text-muted text-xs clear"><i class="i i-clock"></i> 12分钟前</span> </a> </ul> </section> </div> <div class="modal fade" id="excelTipsModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content"> <div class="modal-header"> <button type="button" id="excelTipsModalClose" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">友情提示</h4> </div> <div class="modal-body"> <div id="excelTipsModalBody">
                            会员用户每天可以免费10次下载企业信息、联系方式等。
                            <a onclick="" href="/vip" target="_blank" class="text-primary">立即开通VIP>></a> </div> </div> </div> </div> </div> <div class="modal fade" id="filtrationModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">友情提示</h4> </div> <div class="modal-body text-center"> <a onclick="" href="/vip" target="_blank" class="text-primary">开通VIP</a>
                        ,尊享高级筛选功能
                    </div> </div> </div> </div> </div> </div> <div class="modal fade in" id="searchTongji" tabindex="-1" role="dialog" data-show="true" aria-labelledby="myModalLabel" aria-hidden="false"> <div class="modal-dialog" style="width: 90%;"> <div class="modal-content" > <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title" id="myModalLabel">数据统计</h4> </div> <div class="modal-body"> <div class="row"> <div class="col-md-6"> <div class="panel no-border"> <div class="panel-heading wrapper b-b b-light"> <h4 class="font-thin m-t-none m-b-none">行业分布图</h4> </div> <div class="panel-body"> <div id="search-industry" style="width: 100%;height:500px;"></div> </div> </div> </div> <div class="col-md-6"> <div class="panel no-border"> <div class="panel-heading wrapper b-b b-light"> <h4 class="font-thin m-t-none m-b-none">状态统计图</h4> </div> <div class="panel-body"> <div id="search-status" style="width: 100%;height:500px;"></div> </div> </div> </div> <div class="col-md-12"> <div class="panel no-border"> <div class="panel-heading wrapper b-b b-light"> <h4 class="font-thin m-t-none m-b-none">区域分布图</h4> </div> <div class="panel-body"> <div id="search-province" style="width: 100%;height:750px;"></div> </div> </div> </div> <div class="col-md-12"> <div class="panel no-border"> <div class="panel-heading wrapper b-b b-light"> <h4 class="font-thin m-t-none m-b-none">年份统计图</h4> </div> <div class="panel-body"> <div id="search-year" style="width: 100%;height:500px;"></div> </div> </div> </div> </div> </div> </div> </div> </div> <div class="modal fade" id="phoneModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal" style="width: 400px"> <div class="modal-content qy-modal"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">更多号码
                <span class="ntag vip m-l-sm" data-trigger="hover" data-html="true" data-toggle="tooltip" data-placement="bottom" data-delay="500" title="尊敬的会员，您正在使用高级特权">功能</span> </h4> </div> <div class="modal-body"> </div> </div> </div> </div> <div class="modal fade" id="postCardModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal sm"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title postcard-tep1">设置名片</h4> <h4 class="modal-title postcard-tep2">发送名片</h4> </div> <form class="form-horizontal pform" role="form" id="postCardForm"> <div class="modal-body postcard-tep1"> <div class="form-group"> <label class="col-pre">选择头像<span class="redstar">*</span></label> <div class="col-after" style="margin-top: 8px;"> <div id="uploadFaceImgArea" class="fileinput"> <div class="img" onclick="fileinput('faceImg')" style="display: block;"> <img src="" onerror="this.src='/material/theme/chacha/cms/v2/images/default_face.png'"> <span>上传头像</span> </div> <input type="hidden" name="faceimg"> <span class="message" msgfor="faceimg"> </span> </div> </div> </div> <div class="form-group"> <label class="col-pre">真实姓名<span class="redstar">*</span></label> <div class="col-after"> <input type="text" class="form-control" name="name" placeholder="请输入真实姓名" value=""> <span msgfor="name"></span> </div> </div> <div class="form-group"> <label class="col-pre">公司<span class="redstar">*</span></label> <div class="col-after"> <input type="hidden" name="my_company_keyno" id="postCardCompanyKey" value=""> <input type="text" class="form-control" name="my_company_name" id="postCardCompanyName" onclick="scompanyList(this.value,'postCardCompanyList','postCardCompanyName','postCardCompanyKey')" onkeyup="scompanyList(this.value,'postCardCompanyList','postCardCompanyName','postCardCompanyKey')" autocomplete="off" placeholder="请输入所属公司" value=""> <section class="scompany-list" id="postCardCompanyList" style="position: absolute;width: 427px"></section> <span msgfor="my_company_name"></span> </div> </div> <div class="form-group"> <label class="col-pre">职位<span class="redstar">*</span></label> <div class="col-after"> <input type="text" class="form-control" name="position" placeholder="请输入公司职位" value=""> <span msgfor="position"></span> </div> </div> <div class="form-group"> <label class="col-pre">电话<span class="redstar">*</span></label> <div class="col-after"> <input type="hidden" name="phone_prefix" value=""> <input type="text" class="form-control" name="phone" value="" placeholder="请输入联系电话" value=""> <span msgfor="phone"></span> </div> </div> <div class="form-group"> <label class="col-pre">邮箱<span class="redstar">*</span></label> <div class="col-after"> <input type="text" class="form-control" name="email" value="" placeholder="请输入联系邮箱" value=""> <span msgfor="email"></span> </div> </div> <div class="form-group"> <div class="col-all"> <p class="ts">发送的名片将以APP通知或邮件形式送达指定企业，禁止发布广告、骚扰等无关信息。如收到举报并核实，企查查有权永久封禁被举报账号。</p> </div> </div> </div> <div class="modal-body postcard-tep2"> <div class="postcard-wrap"> <div class="pcard-content"> <div class="clearfix"> <div class="col-ft"> <div class="img"> <img id="postcardImg" onerror="this.src='/material/theme/chacha/cms/v2/images/default_face.png'"> </div> </div> <div class="col-bd"> <div class="title"> <h4 id="postcardName">雷军</h4> <span id="postCardCompany">小米科技有限责任公司</span> </div> </div> </div> <div class="clearfix m-t-sm"> <span class="des">职位：</span> <span id="postCardPostion" class="value">CEO</span> </div> <div class="clearfix m-t-xs"> <span class="des">电话：</span> <span id="postCardPhone" class="value">13872119231</span> </div> <div class="clearfix m-t-xs"> <span class="des">邮箱：</span> <span id="postCardEmail" class="value">leijun@xiaomi.com</span> </div> </div> </div> <div class="form-group m-t-md"> <div class="col-all"> <textarea style="resize: none;" rows="3" name="cooperation_intention" class="form-control" placeholder="请输入合作意向，详细介绍你的合作意向，有助于推动对方快速联系你"></textarea> <span msgfor="cooperation_intention"></span> </div> </div> <div class="form-group"> <div class="col-all"> <p class="ts">发送的名片将以APP通知或邮件形式送达指定企业，禁止发布广告、骚扰等无关信息。如收到举报并核实，企查查有权永久封禁被举报账号。</p> </div> </div> </div> <div class="modal-footer"> <input type="hidden" id="postCardToOptions" name="to_company_options"> <button type="button" onclick="postcardTep(2)" class="btn btn-primary postcard-tep1">下一步</button> <a href="/user_setting?from=f" class="btn btn-default postcard-tep2">修改信息</a> <button type="submit" class="btn btn-primary postcard-tep2">发送名片</button> </div> </form> <form class="pform-uploadimg" enctype="multipart/form-data" id="uploadFaceImg"> <input type="file" id="faceImg" name="pic"> </form> </div> </div> </div> <div class="modal fade" id="toSettingModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal sm" style="width: 450px;"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">提示</h4> </div> <div class="modal-body"> <div class="pnodata"> <img src="/material/theme/chacha/cms/v2/images/nno_image.png"> <p>投递名片，请确认已绑定手机号、邮箱以及完善个人信息</p> </div> </div> <div class="modal-footer"> <a href="/user_setting?from=f" class="btn btn-primary">去设置</a> </div> </div> </div> </div> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/searchindex.js?time=20190326"></script> <script type="text/javascript">
    var postcardCount = parseInt('');
    var TotalRecords = '22206';
    var requestFlag = '1';
    var dataForChart = JSON.parse('[{"key":"province","items":[{"value":"","count":105,"desc":""},{"value":"AH","count":564,"desc":"\u5b89\u5fbd"},{"value":"BJ","count":222,"desc":"\u5317\u4eac"},{"value":"CQ","count":116,"desc":"\u91cd\u5e86"},{"value":"FJ","count":724,"desc":"\u798f\u5efa"},{"value":"GD","count":1289,"desc":"\u5e7f\u4e1c"},{"value":"GS","count":275,"desc":"\u7518\u8083"},{"value":"GX","count":519,"desc":"\u5e7f\u897f"},{"value":"GZ","count":434,"desc":"\u8d35\u5dde"},{"value":"HAIN","count":123,"desc":"\u6d77\u5357"},{"value":"HB","count":1236,"desc":"\u6cb3\u5317"},{"value":"HEN","count":1326,"desc":"\u6cb3\u5357"},{"value":"HK","count":83,"desc":"\u9999\u6e2f\u7279\u522b\u884c\u653f\u533a"},{"value":"HLJ","count":563,"desc":"\u9ed1\u9f99\u6c5f"},{"value":"HUB","count":387,"desc":"\u6e56\u5317"},{"value":"HUN","count":596,"desc":"\u6e56\u5357"},{"value":"JL","count":598,"desc":"\u5409\u6797"},{"value":"JS","count":1119,"desc":"\u6c5f\u82cf"},{"value":"JX","count":307,"desc":"\u6c5f\u897f"},{"value":"LN","count":750,"desc":"\u8fbd\u5b81"},{"value":"NMG","count":533,"desc":"\u5185\u8499\u53e4"},{"value":"NX","count":143,"desc":"\u5b81\u590f"},{"value":"QH","count":67,"desc":"\u9752\u6d77"},{"value":"SAX","count":726,"desc":"\u9655\u897f"},{"value":"SC","count":909,"desc":"\u56db\u5ddd"},{"value":"SD","count":5860,"desc":"\u5c71\u4e1c"},{"value":"SH","count":68,"desc":"\u4e0a\u6d77"},{"value":"SX","count":399,"desc":"\u5c71\u897f"},{"value":"TJ","count":110,"desc":"\u5929\u6d25"},{"value":"TW","count":19,"desc":"\u53f0\u6e7e\u7701"},{"value":"XJ","count":294,"desc":"\u65b0\u7586"},{"value":"XZ","count":25,"desc":"\u897f\u85cf"},{"value":"YN","count":734,"desc":"\u4e91\u5357"},{"value":"ZJ","count":983,"desc":"\u6d59\u6c5f"}]},{"key":"industrycode","items":[{"value":"","count":307,"desc":""},{"value":"A","count":91,"desc":"\u519c\u3001\u6797\u3001\u7267\u3001\u6e14\u4e1a"},{"value":"B","count":3,"desc":"\u91c7\u77ff\u4e1a"},{"value":"C","count":764,"desc":"\u5236\u9020\u4e1a"},{"value":"D","count":1,"desc":"\u7535\u529b\u3001\u70ed\u529b\u3001\u71c3\u6c14\u53ca\u6c34\u751f\u4ea7\u548c\u4f9b\u5e94\u4e1a"},{"value":"E","count":286,"desc":"\u5efa\u7b51\u4e1a"},{"value":"F","count":12470,"desc":"\u6279\u53d1\u548c\u96f6\u552e\u4e1a"},{"value":"G","count":59,"desc":"\u4ea4\u901a\u8fd0\u8f93\u3001\u4ed3\u50a8\u548c\u90ae\u653f\u4e1a"},{"value":"H","count":3183,"desc":"\u4f4f\u5bbf\u548c\u9910\u996e\u4e1a"},{"value":"I","count":498,"desc":"\u4fe1\u606f\u4f20\u8f93\u3001\u8f6f\u4ef6\u548c\u4fe1\u606f\u6280\u672f\u670d\u52a1\u4e1a"},{"value":"J","count":59,"desc":"\u91d1\u878d\u4e1a"},{"value":"K","count":257,"desc":"\u623f\u5730\u4ea7\u4e1a"},{"value":"L","count":968,"desc":"\u79df\u8d41\u548c\u5546\u52a1\u670d\u52a1\u4e1a"},{"value":"M","count":400,"desc":"\u79d1\u5b66\u7814\u7a76\u548c\u6280\u672f\u670d\u52a1\u4e1a"},{"value":"N","count":17,"desc":"\u6c34\u5229\u3001\u73af\u5883\u548c\u516c\u5171\u8bbe\u65bd\u7ba1\u7406\u4e1a"},{"value":"O","count":2199,"desc":"\u5c45\u6c11\u670d\u52a1\u3001\u4fee\u7406\u548c\u5176\u4ed6\u670d\u52a1\u4e1a"},{"value":"P","count":26,"desc":"\u6559\u80b2"},{"value":"Q","count":16,"desc":"\u536b\u751f\u548c\u793e\u4f1a\u5de5\u4f5c"},{"value":"R","count":564,"desc":"\u6587\u5316\u3001\u4f53\u80b2\u548c\u5a31\u4e50\u4e1a"},{"value":"S","count":4,"desc":"\u516c\u5171\u7ba1\u7406\u3001\u793e\u4f1a\u4fdd\u969c\u548c\u793e\u4f1a\u7ec4\u7ec7"},{"value":"T","count":34,"desc":"\u56fd\u9645\u7ec4\u7ec7"}]},{"key":"statuscode","items":[{"value":"0","count":18,"desc":"\u6682\u65e0"},{"value":"10","count":4104,"desc":"\u6b63\u5e38"},{"value":"100","count":1,"desc":"\u5e9f\u6b62"},{"value":"117","count":8,"desc":"\u6838\u51c6\u8bbe\u7acb"},{"value":"127","count":7,"desc":"\u89e3\u6563"},{"value":"128","count":1,"desc":"\u89e3\u6563\u6e05\u7b97\u5b8c\u7ed3"},{"value":"20","count":10004,"desc":"\u5b58\u7eed"},{"value":"60","count":5,"desc":"\u8fc1\u51fa"},{"value":"80","count":2,"desc":"\u64a4\u9500"},{"value":"90","count":1365,"desc":"\u540a\u9500"},{"value":"92","count":47,"desc":"\u4ecd\u6ce8\u518c"},{"value":"94","count":36,"desc":"\u5df2\u544a\u89e3\u6563"},{"value":"99","count":6608,"desc":"\u6ce8\u9500"}]},{"key":"startdateyear","items":[{"value":"1981","count":1,"desc":"1981"},{"value":"1982","count":3,"desc":"1982"},{"value":"1983","count":3,"desc":"1983"},{"value":"1984","count":1,"desc":"1984"},{"value":"1985","count":3,"desc":"1985"},{"value":"1986","count":3,"desc":"1986"},{"value":"1987","count":3,"desc":"1987"},{"value":"1989","count":51,"desc":"1989"},{"value":"1990","count":8,"desc":"1990"},{"value":"1991","count":5,"desc":"1991"},{"value":"1992","count":12,"desc":"1992"},{"value":"1993","count":20,"desc":"1993"},{"value":"1994","count":21,"desc":"1994"},{"value":"1995","count":22,"desc":"1995"},{"value":"1996","count":32,"desc":"1996"},{"value":"1997","count":34,"desc":"1997"},{"value":"1998","count":43,"desc":"1998"},{"value":"1999","count":65,"desc":"1999"},{"value":"2000","count":115,"desc":"2000"},{"value":"2001","count":132,"desc":"2001"},{"value":"2002","count":134,"desc":"2002"},{"value":"2003","count":263,"desc":"2003"},{"value":"2004","count":446,"desc":"2004"},{"value":"2005","count":505,"desc":"2005"},{"value":"2006","count":778,"desc":"2006"},{"value":"2007","count":1021,"desc":"2007"},{"value":"2008","count":1002,"desc":"2008"},{"value":"2009","count":1287,"desc":"2009"},{"value":"2010","count":1227,"desc":"2010"},{"value":"2011","count":1401,"desc":"2011"},{"value":"2012","count":1366,"desc":"2012"},{"value":"2013","count":1483,"desc":"2013"},{"value":"2014","count":1448,"desc":"2014"},{"value":"2015","count":2104,"desc":"2015"},{"value":"2016","count":1965,"desc":"2016"},{"value":"2017","count":2044,"desc":"2017"},{"value":"2018","count":2443,"desc":"2018"},{"value":"2019","count":603,"desc":"2019"}]}]');
    var isVip = false;
    var isSvip = '';
        $(function(){
        if(requestFlag && window.location.hash){
            updateDesc(1);
            getSearchList();
        }

        if(requestFlag && !window.location.hash){
            $('#appendBox').hide();
        }
        //翻页跳转
        $('body').on('click','#jumpPage',function(){
            var maxPage = parseInt('1');
            var page = $(this).prev().val();
            if(page>maxPage){
                faldia('超出页码');
                return;
            }
            var count = TotalRecords;
            var limit = Math.ceil(parseInt(count)/10);
            var groupId = '';
            var userPageIndex = '5';
            userPageIndex =parseInt(userPageIndex);
            jumpPage2(limit,userPageIndex,page,groupId,1);
        });
        $('#searchTongji').on('shown.bs.modal',function(){
            chartUtil.drawPie(chartUtil.transPieData(dataForChart[1].Items),"search-industry",1,'');
            chartUtil.drawMap(chartUtil.transMapData(dataForChart[0].Items),"search-province",7,'');
            chartUtil.drawPie(chartUtil.transPieData(dataForChart[2].Items),"search-status",1,'');
            chartUtil.drawBar(chartUtil.transBarData(dataForChart[3].Items),"search-year",1,'');
        });
        initFundRange();
        initRegistDate();
        setpostCardForm();
        $(".custom.a>span[data-toggle=dropdown]").removeAttr('data-toggle')
    });



</script> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/footer.css?time=20190326" type="text/css"/> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/animate.css?time=1508428800" type="text/css"/> <footer class="footer"> <div class="container"> <div class="footer-top clearfix"> <div class="about" style=""> <h4>关于我们</h4> <ul class="list-unstyled"> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'联系我们'});" href="/cms?id=13">联系我们</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'用户协议'});" href="/cms?id=14">用户协议</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'用户隐私权'});" href="/cms?id=15">用户隐私权</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'友情链接'});" href="/cms?id=16">友情链接</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'关于我们'});" href="/cms?id=892">关于我们</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'用户帮助'});" href="/cms?id=14578">用户帮助</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'名词百科'});" href="/cms?id=146498">名词百科</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'产品标签'});" href="/cms?id=146499">产品标签</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'更新记录'});" href="/cms?id=146500">更新记录</a></li> </ul> </div> <div class="contact"> <h4>联系方式</h4> <ul class="list-unstyled"> <li>企查查官方电话：400-928-2212</li> <li>官方客服QQ：<a target="_blank" href="http://wpa.b.qq.com/cgi/wpa.php?ln=1&key=XzkzODA0NDMwM180ODcyNjFfNDAwOTk4NTIxMl8yXw">4009985212</a></li> <li>客服邮箱：<a href="mailto:kf@qichacha.com">kf@qichacha.com</a></li> <li>微信客服：qccgf1234</li> <li>微信公众号：qcc365</li> <li>地址：江苏省苏州市工业园区东长路88号2.5产业园C1幢5楼</li> </ul> </div> <div class="service" style=""> <h4>查查服务</h4> <ul class="list-unstyled"> <li> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业问答'});" href="https://www.qichacha.com/more_hotqa" target="_blank" >企业问答</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'500强企业'});" href="https://www.qichacha.com/cms_top500" target="_blank" >500强企业</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'疫苗查查'});" href="http://ai.qichacha.com/" target="_blank" >疫苗查查</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'融资查询'});" href="https://www.qichacha.com/elib_financing" target="_blank" >融资查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业风控'});" href="http://pro.qichacha.com/?source=websiteFoot" target="_blank" >企业风控</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业库'});" href="http://www.qichacha.com/elib" target="_blank" >企业库</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'裁判文书查询'});" href="http://www.qichacha.com/more_wenshus" target="_blank" >裁判文书查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'新三板企业查询'});" href="http://sanban.qichacha.com" target="_blank" >新三板企业查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'上市企业查询'});" href="http://ipo.qichacha.com/" target="_blank" >上市企业查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企查查企业查询'});" href="https://www.qichacha.com/gongsi" target="_blank" >企查查企业查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企查查移动版'});" href="https://m.qichacha.com" target="_blank" >企查查移动版</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企查查社区'});" href="https://www.qichacha.com/dianping" target="_blank" >企查查社区</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业风险搜索'});" href="https://www.qichacha.com/more_shixins" target="_blank" >企业风险搜索</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'商标专利搜索'});" href="https://www.qichacha.com/more_brands" target="_blank" >商标专利搜索</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业网址导航'});" href="https://www.qichacha.com/daohang" target="_blank" >企业网址导航</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业高管查询'});" href="https://www.qichacha.com/boss" target="_blank" >企业高管查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业税号查询'});" href="https://www.qichacha.com/tax" target="_blank" >企业税号查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业新闻头条'});" href="https://www.qichacha.com/news" target="_blank" >企业新闻头条</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业大数据导航'});" href="https://hao.qichacha.com" target="_blank" >企业大数据导航</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企查查下载'});" href="https://www.qichacha.com/weixin" target="_blank" >企查查下载</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业失信查询'});" href="https://www.qichacha.com/more_shixins" target="_blank" >企业失信查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企查查接口平台'});" href="http://openapi.qichacha.com/?source=websiteFoot" target="_blank" rel="nofollow">企查查接口平台</a> <a href="/yellowpage">公司黄页</a> <a href="/cms_dirhot">人员名录</a> <a href="http://open.qichacha.com" target="_blank"> 开放平台</a> </li> </ul> </div> <div class="qrcode"> <div class="qrcode-item"> <img src="/material/theme/chacha/cms/v2/images/v3/code_xcx.png?t=3" alt="企查查APP下载"> <span class="ma_xcx">小程序</span> </div> <div class="qrcode-item"> <img src="/material/theme/chacha/cms/v2/images/v3/code_app.png?t=3" alt="企查查APP下载"> <span class="ma_app">扫码下载APP</span> </div> <div class="qrcode-item"> <img src="/material/theme/chacha/cms/v2/images/v3/code_wx.png?t=3" alt="企查查微信公众号"> <span class="ma_wx">微信公众号</span> </div> </div> </div> <div class="footer-link"> <div class="footer-row clearfix"> <div class="footer-row-head">
                    数据来源：
                </div> <div class="footer-row-content"> <span class="item">全国企业信用信息公示系统</span> <span class="item">中国裁判文书网</span> <span class="item">中国执行信息公开网</span> <span class="item">国家知识产权局</span> <span class="item">商标局</span> <span class="item">版权局</span> </div> </div> <div class="footer-row clearfix"> <div class="footer-row-head">
                    热点省份：
                </div> <div class="footer-row-content"> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'安徽企业'});" href="http://ah.qichacha.com" target="_blank">安徽企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'北京企业'});" href="http://bj.qichacha.com" target="_blank">北京企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'重庆企业'});" href="http://cq.qichacha.com" target="_blank">重庆企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'福建企业'});" href="http://fj.qichacha.com" target="_blank">福建企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'甘肃企业'});" href="http://gs.qichacha.com" target="_blank">甘肃企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'广东企业'});" href="http://gd.qichacha.com" target="_blank">广东企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'广西企业'});" href="http://gx.qichacha.com" target="_blank">广西企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'贵州企业'});" href="http://gz.qichacha.com" target="_blank">贵州企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'海南企业'});" href="http://hain.qichacha.com" target="_blank">海南企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'河北企业'});" href="http://hb.qichacha.com" target="_blank">河北企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'黑龙江企业'});" href="http://hlj.qichacha.com" target="_blank">黑龙江企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'河南企业'});" href="http://hen.qichacha.com" target="_blank">河南企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'湖北企业'});" href="http://hub.qichacha.com" target="_blank">湖北企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'湖南企业'});" href="http://hun.qichacha.com" target="_blank">湖南企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'江苏企业'});" href="http://js.qichacha.com" target="_blank">江苏企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'江西企业'});" href="http://jx.qichacha.com" target="_blank">江西企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'吉林企业'});" href="http://jl.qichacha.com" target="_blank">吉林企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'辽宁企业'});" href="http://ln.qichacha.com" target="_blank">辽宁企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'内蒙古企业'});" href="http://nmg.qichacha.com" target="_blank">内蒙古企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'宁夏企业'});" href="http://nx.qichacha.com" target="_blank">宁夏企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'青海企业'});" href="http://qh.qichacha.com" target="_blank">青海企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'山东企业'});" href="http://sd.qichacha.com" target="_blank">山东企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'上海企业'});" href="http://sh.qichacha.com" target="_blank">上海企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'山西企业'});" href="http://sx.qichacha.com" target="_blank">山西企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'陕西企业'});" href="http://sax.qichacha.com" target="_blank">陕西企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'四川企业'});" href="http://sc.qichacha.com" target="_blank">四川企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'天津企业'});" href="http://tj.qichacha.com" target="_blank">天津企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'新疆企业'});" href="http://xj.qichacha.com" target="_blank">新疆企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'西藏企业'});" href="http://xz.qichacha.com" target="_blank">西藏企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'云南企业'});" href="http://yn.qichacha.com" target="_blank">云南企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'浙江企业'});" href="http://zj.qichacha.com" target="_blank">浙江企业</a> </div> </div> </div> </div> </div> <div class="footer-copy-bg"> <div class="container"> <div class="footer-copy clearfix"> <div class="pull-left"> <div class="m-t-sm">交流QQ群：
                        <span>716516006</span> <span>&nbsp;&nbsp;&nbsp;978339588(已满)</span> <span>&nbsp;823551131(已满)</span> <span>&nbsp;928689619(已满)</span> <span>&nbsp;467569586(已满)</span> <span>&nbsp;369254293(已满)</span> </div> <div class="m-t-xs"> <a href="javascript:void(0)" title="企查查">&copy;2014-2019</a> <a href="http://www.miibeian.gov.cn/" target="_blank"> 苏ICP备15042526号-4</a>
                        版权所有&nbsp;苏州朗动网络科技有限公司
                        &nbsp;增值电信业务经营许可证：<a href="http://jscainfo.miitbeian.gov.cn/state/outPortal/loginPortal.action" rel="nofollow" target="_blank">苏ICP证B2-20180251</a> </div> </div> <div class="auth"> <a href="https://ss.knet.cn/verifyseal.dll?sn=e17091132050068868mhtm000000&comefrom=trust" rel="nofollow" target="_blank"> <img class="m-l-sm" style="width: 98px" src="/material/theme/chacha/cms/v2/images/dependable.png"/> </a> <a href="http://www.jsdsgsxt.gov.cn/mbm/entweb/elec/certView.shtml?siteId=2f2c5b85a5154355a56eb3dee98ad8a3" rel="nofollow" target="_blank"> <img class="m-l-sm" style="width: 30px" src="/material/theme/chacha/cms/v2/images/jsdsgsxt.png"/> </a> <a href="https://v.pinpaibao.com.cn/cert/site/?site=www.qichacha.com&at=official" rel="nofollow" target="_blank"> <img class="m-l-sm" style="width: 106px;" src="https://static.anquan.org/static/outer/image/gw_124x47.png"/> </a> </div> </div> </div> </div> </footer> <div class="modal fade" id="feedModal" tabindex="-1" role="dialog" style="overflow: hidden;" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal sm nmodal-sm"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title" id="myModalLabel">意见反馈</h4> </div> <div class="modal-body"> <form class="form-horizontal" role="form"> <div class="form-group"> <label for="inputEmail3" class="col-sm-2">反馈内容</label> <div class="col-sm-10"> <textarea class="form-control content" rows="5"  name="content" placeholder="亲爱的用户：请在这里直接填写您遇到的问题或意见建议，您的意见是我们前进的动力"></textarea> <span class="contentmsg text-danger"></span> </div> </div> <div class="form-group"> <label for="inputPassword3" class="col-sm-2">联系方式</label> <div class="col-sm-10"> <input type="text" class="form-control email" name="email" placeholder="请输入邮箱，方便我们联系您。"> <span class="emailmsg text-danger"></span> </div> </div> <div class="form-group"> <div class="col-sm-10 col-sm-offset-2"> <label>亲爱的顾客，您也可以直接拨打企查查官方电话：400-928-2212 或者 联系企查查官方客服QQ：4009985212，我们将及时为您解答问题。</label> </div> </div> <div class="form-group m-t-lg"> <label for="inputPassword3" class="col-sm-2"></label> <div class="col-sm-10  text-center"> <span class="btn btn-primary btn-guest btn-block">提交反馈</span> </div> </div> </form> </div> </div> </div> </div> <div style="display:none;"> <script src="https://s4.cnzz.com/z_stat.php?id=1254842228&web_id=1254842228" language="JavaScript"></script> <script>
      var _hmt = _hmt || [];
      (function() {
          var hm = document.createElement("script");
          hm.src = "https://hm.baidu.com/hm.js?3456bee468c83cc63fb5147f119f1075";
          var s = document.getElementsByTagName("script")[0];
          s.parentNode.insertBefore(hm, s);
      })();
  </script> <script>(function(){
          var src = (document.location.protocol == "http:") ? "http://js.passport.qihucdn.com/11.0.1.js?db135ad770b0860a90c3a2ca38cf577c":"https://jspassport.ssl.qhimg.com/11.0.1.js?db135ad770b0860a90c3a2ca38cf577c";
          document.write('<script src="' + src + '" id="sozz"><\/script>');
      })();
  </script> </div> <script type="text/javascript">
    (function(){
        var bp = document.createElement('script');
        var curProtocol = window.location.protocol.split(':')[0];
        if (curProtocol === 'https') {
            bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
        }
        else {
            bp.src = 'http://push.zhanzhang.baidu.com/push.js';
        }
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(bp, s);
    })();
</script> <link rel="stylesheet" type="text/css" href="/material/theme/chacha/cms/v2/css/rnav.css?timestamp=20190326"> <div id="RNav" class="visible-lg i_hide"> <div class="i_menu"> <ul class="i_bts-outer" style="bottom:69px;"> <li class="i_bt_sm i_bt_xcx"><i></i> <label>小程序</label><img src="/material/theme/chacha/cms/v2/images/leftnav/bg_xcx.png?t=2" alt="企查查"></li> <li class="i_bt_sm i_bt_wx"><i></i> <label>公众号</label><img src="/material/theme/chacha/cms/v2/images/leftnav/bg_wx.png?t=2" alt="企查查"></li> <li onclick="zhugeTrack('下载APP悬浮按钮');" class="i_bt_sm i_bt_dow"><i></i> <label>APP</label><img src="/material/theme/chacha/cms/v2/images/leftnav/bg_app.png?t=3" alt="企查查"></li> <script type="text/javascript" src="/material/js/jquery.cookie.js"></script> <script type="text/javascript" src="/material/js/jquery.validate.min.js"></script> <script type="text/javascript" src="/material/js/jquery.form.min.js"></script> <script type="text/javascript" src="/material/js/global.js?t=20190326"></script> <li id="RNBack" class="i_bt_sm i_bt_kf" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><i></i> <label>反馈</label></li> <li class="i_bt_sm i_bt_back" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><i></i> <label>客服</label></li> <li id="RNTop" class="i_bt_sm i_bt_top"><i></i> <label>置顶</label></li> </ul> </div> <div class="i_container"> <div class="i_nodata">暂无数据</div> <div id="RNFoc" class="i_wrap"> <div class="i_title">我的关注</div> <div class="i_com-wrap"> <div style="height:1px;width:240px;"></div> </div> <div class="i_botbt"> <a href="/user_follow">打开全部</a> </div> </div> <div id="RNCom" class="i_wrap"> <div class="i_title">企业对比</div> <div class="i_toast">
				还可以添加<span id="ComLastCount">5</span>家企业 
				<a id="ClearCompares" class="c_a">清空</a> </div> <div class="i_com-wrap"> <div class="i_com i_addcom" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"> <img src="/material/theme/chacha/cms/v2/images/leftnav/icon-add.png" alt="企查查"/> <a class="c_a" href="javascript:;">添加企业</a> </div> <div style="height:1px;width:240px;"></div> </div> <div class="i_botbt"> <a href="javascript:;" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">对比企业</a> </div> </div> <div id="RNRel" class="i_wrap"> <div class="i_title">找关系</div> <div class="i_toast">
				还可以添加<span id="RelLastCount">5</span>家企业 
				<a class="c_a" id="ClearRels">清空</a> </div> <div class="i_com-wrap"> <div class="i_com i_addcom" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"> <img src="/material/theme/chacha/cms/v2/images/leftnav/icon-add.png" alt="企查查"/> <a class="c_a" href="javascript:;">添加企业或个人</a> </div> <div style="height:1px;width:240px;"></div> </div> <div class="i_botbt"> <a href="javascript:;" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">找关系</a> </div> </div> </div> <div class="modal fade" id="qaddComPanel" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content" style="width:600px;"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">添加企业</h4> </div> <div class="modal-body" style="height: 330px"> <form class="form-horizontal" role="form"> <div class="form-group"> <div class="col-sm-12 m-t-md"> <input type="text" id="qcomName" name="comName" class="form-control" value="" placeholder="请输入公司/人" autocomplete="off" oninput="qsearchCom(event,this)"/> <section class="panel hidden-xs" id="qsearchList" style="position: absolute;width: 560px;z-index: 10;display: none;"></section> </div> <div class="col-sm-12 text-center m-t-lg" style="padding-left: 18px;padding-right: 18px;"> <span id="qaddComPanelConfirm" class="btn-primary btn-guest btn-block" style="padding-top: 5px;padding-bottom: 5px;cursor:pointer;">添加企业</span> </div> </div> </form> </div> </div> </div> </div> <div class="modal fade" id="addRelPanel" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content" style="width:600px;"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">添加企业或个人</h4> </div> <div class="modal-body" style="height: 445px"> <form class="form-horizontal" role="form"> <div class="form-group"> <div class="col-sm-12 m-t-md"> <input type="text" id="qrcomName" name="comName" class="form-control" value="" placeholder="请输入公司名称" autocomplete="off" oninput="qrsearchCom(event,this)"/> <section class="panel hidden-xs" id="qrsearchList" style="position: absolute;width: 560px;z-index: 10;display: none;"></section> </div> </div> </form> </div> </div> </div> </div> </div> <script type="text/javascript">
	 /*rightNav.js 使用变量*/
	 var personImg =  "/material/theme/chacha/cms/v2/images/leftnav/person.png";
	 var frimUrl = "";
	 var comDefaultImg = "/material/theme/chacha/cms/v2/images/company.jpg"
          
    function jumpTax(){
        window.location.href=encodeURI(INDEX_URL+"tax");
    }       
</script> <script src="/material/theme/chacha/cms/v2/js/rightNav.js?timestamp=1497542400"></script> <link type="text/css" href="/material/theme/chacha/cms/v2/css/login.css?version=20190326" rel="stylesheet" /> <div class="modal fade" id="loginModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" data-backdrop="static"> <div class="modal-dialog login-madal-dialog"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title" id="myModalLabel">登录企查查</h4> </div> <div class="modal-body"> <div class="login-sao-panel"> <div class="title">扫码登录请使用<br> <a href="/app" target="_blank" class="text-primary">企查查APP</a> > 我的 > 扫一扫</div> <div class="qrcodewrap"> <div class="qrcode" id='qrcodeModalLogin'></div> <img class="qrcodets" src="/material/theme/chacha/cms/v2/images/qrcode_ts.png"> </div> <div class="tip"><span></span> 扫一扫功能支持企查查 APP11.0.6 及以上版本</div> </div> <div class="login-panel" style="display: none;" id="normalLoginPanel"> <div class="login-panel-head clearfix"> <div class="login-tab"> <a href="javascript:;" id="verifyLogin">快捷登录</a> </div> <div class="login-tab"> <a href="javascript:;" class="active">密码登录</a> </div> </div> <div class="login-panel-body"> <form class="form-group login-form" role="form" id="user_login_normal"> <div class="form-group"> <input type='hidden' class='phone_prefix_input' value="+86" name='phone_prefix' /> <div class="phone-select dropdown"> <a class="phone_prefix" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true"> 中国 +86<b class="caret text-primary"></b></a> <div class="phoneline"></div> <ul class="phone_prefix_ul dropdown-menu"></ul> </div> <input id="nameNormal" name="nameNormal" type="text" class="form-control form-control-error" placeholder="请输入手机号码"> <span msgfor="nameNormal"></span> </div> <div class="form-group m-t-md"> <div class="show-pwd"></div> <input id="pwdNormal" name="pwdNormal" type="password" class="form-control form-control-error" placeholder="请输入密码"> <span msgfor="pwdNormal"></span> </div> <div class="form-group m-t-md"> <div id="dom_id_one"></div> </div> <div class="checkbox m-t-md"> <label class="text-dark-lter"> <input type="checkbox" name="keep" checked="checked" value="option1"> 一周内保持登录状态
                                </label> </div> <button type="submit" class="btn btn-primary btn-block m-t-md login-btn"> <strong>立即登录</strong></button> <input type='hidden' id='csessionid_one' name='csessionid_one' /> <input type='hidden' id='sig_one' name='sig_one' /> <input type='hidden' id='token_one' name='token_one' /> <input type='hidden' id='scene_one' name='scene_one' /> <input type='hidden' name='verify_type' value="1" /> </form> <div class="login-other m-t-md"> <div class="clearfix"> <div class="pull-left"> <a href="/user_register" class="text-primary">账号注册</a> </div> <div class="pull-left text-dark-lt m-l-sm"> <a href="/user_forgetpassword">忘记密码？</a> </div> <div class="pull-right"> <a href="https://open.weixin.qq.com/connect/qrconnect?appid=wx9b26295cdfab4175&redirect_uri=http://www.qichacha.com/user_wxloginok?back=&response_type=code&scope=snsapi_login&state=#wechat_redirect" class="btn-wx"></a> <a href="/user_qqlogin?back=&replace=1" class="btn-qq m-l-xs"> </a> <a href="/user_weiboLogin" class="btn-weibo m-l-xs"> </a> </div> </div> </div> </div> </div> <div class="login-panel" id="verifyLoginPanel"> <div class="login-panel-head clearfix"> <div class="login-tab"> <a href="javascript:;" class="active">快捷登录</a> </div> <div class="login-tab"> <a href="javascript:;" id="normalLogin">密码登录</a> </div> </div> <div class="login-panel-body"> <form class="form-group login-form" role="form" id="user_login_verify"> <div class="form-group"> <input type='hidden' class='phone_prefix_input' value="+86" name='phone_prefix' /> <div class="phone-select dropdown"> <a class="phone_prefix" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true"> 中国 +86<b class="caret text-primary"></b></a> <div class="phoneline"></div> <ul class="phone_prefix_ul dropdown-menu"></ul> </div> <input id="nameVerify" name="nameVerify" onkeyup="phoneKeyup()" oninput="phoneKeyup()" type="text" class="form-control form-control-error" placeholder="请输入手机号码"> <span msgfor="nameVerify"></span> </div> <div class="form-group m-t-md"> <div id="dom_id_two"></div> </div> <div class="form-group m-t-md"> <input id="vcodeNormal" maxlength="6" name="codeVerify" type="text" class="form-control form-control-error" placeholder="短信验证码"> <a href="javascript:;" class="text-primary vcode-btn get-mobile-code">
                         获取验证
                      </a> <span msgfor="codeVerify"> </span> </div> <div class="checkbox m-t-md"> <label class="text-dark-lter"> <input type="checkbox" name="keep" checked="checked" value="option1"> 一周内保持登录状态
                                </label> </div> <button type="submit" class="btn btn-primary btn-block m-t-md login-btn"> <strong>立即登录</strong></button> <input type='hidden' id='csessionid_two' name='csessionid_two' /> <input type='hidden' id='sig_two' name='sig_two' /> <input type='hidden' id='token_two' name='token_two' /> <input type='hidden' id='scene_two' name='scene_two' /> </form> <div class="login-other m-t-md"> <div class="clearfix"> <div class="pull-left"> <a onclick="" href="/user_register" class="text-primary">账号注册</a> </div> <div class="pull-left text-dark-lt m-l-sm"> <a onclick="" href="/user_forgetpassword">忘记密码？</a> </div> <div class="pull-right"> <a onclick="" href="https://open.weixin.qq.com/connect/qrconnect?appid=wx9b26295cdfab4175&redirect_uri=http://www.qichacha.com/user_wxloginok?back=&response_type=code&scope=snsapi_login&state=#wechat_redirect" class="btn-wx"></a> <a onclick="" href="/user_qqlogin?back=&replace=1" class="btn-qq m-l-xs"> </a> <a onclick="" routerLink="/user" class="btn-weibo m-l-xs"> </a> </div> </div> </div> </div> </div> </div> </div> </div> </div> <link type="text/css" href="//g.alicdn.com/sd/ncpc/nc.css?t=1520579483" rel="stylesheet" /> <script type="text/javascript" src="//g.alicdn.com/sd/ncpc/nc.js?t=1520579483"></script> <div id="_umfp" style="display:inline;width:1px;height:1px;overflow:hidden"></div> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/login.js?version=20190326"></script> <script>

    //普通登录
    formset({
        "id":"user_login_normal",
        "url":"user_loginaction",
        "rule":{
            "nameNormal":{
                required:true,
            },
            "pwdNormal":{
                required:true,
                minlength:6
            }
        },

        "messages":{
            "nameNormal":{
                required:"请输入手机号",
            },
            "pwdNormal":{
                required:"请输入密码",
                minlength:"密码最少6位"
            }
        },
        "sucfunc":function(rs){
            $('#loginModalClose').click();
            location.reload();
        },
        "falfunc":function(rs){
            faldia({'content':'登录失败：'+rs.msg});
            getAliCaptcha('one');
            document.getElementById('csessionid_one').value = '';
            document.getElementById('sig_one').value = '';
            document.getElementById('token_one').value = '';
            document.getElementById('scene_one').value = '';
        }
    });
    //手机验证码登录
    formset({
        "id":"user_login_verify",
        "url":"user_loginbyverify",
        "rule":{
            "nameVerify":{
                required:true,
            },
            "codeVerify":{
                required:true,
                minlength:6
            }
        },

        "messages":{
            "nameVerify":{
                required:"请输入手机号",
            },
            "codeVerify":{
                required: "请输入手机激活码",
                minlength: "手机激活码最少{0}个字"
            }
        },
        "sucfunc":function(rs){
            $('#loginModalClose').click();
            location.reload();
        },
        "falfunc":function(rs){
            faldia({'content':'登录失败：'+rs.msg});
            getAliCaptcha('two');
            document.getElementById('csessionid_two').value = '';
            document.getElementById('sig_two').value = '';
            document.getElementById('token_two').value = '';
            document.getElementById('scene_two').value = '';
        }
    });

    var codeStatus = true;//状态
    var waitSec = 60; //设置秒数(单位秒)
    var i = 1;
    var clock;

    function sTimer() {
        var r = waitSec - i;
        if (r == 0) {
            clearInterval(clock);
            $(".get-mobile-code").html("重新获取");
            codeStatus = true;
            $(".get-mobile-code").data('clicked', false).removeClass('disabled');
        } else {
            $(".get-mobile-code").html("(" + r + ")秒重新发送");
            i++;
        }
    };
    function startClock(t) {
        codeStatus = false;
        i = parseInt(t);
        clock = setInterval(sTimer, 1000);
    }

    function phoneKeyup(){
      
    }

    

    //获取手机验证码
    function mobileCode() {
        $(".get-mobile-code").bind('click', function () {
            if ($(this).data('clicked')) return false;
            var phone = $("input[name=nameVerify]").val();
            var scene = $("input[name='scene_two']").val();
            var token = $("input[name='token_two']").val();
            var sig = $("input[name='sig_two']").val();
            var csessionid = $("input[name='csessionid_two']").val();
            var phone_prefix = $("input[name='phone_prefix']").val();
            var afsFlag = '';

            if ($("input[name=nameVerify]").hasClass('validate-error')) {
                faldia('请重新输入手机号码！');
                return false;
            }

            if (!phone) {
                faldia('手机号码不能为空！');
                return false;
            }

            if(afsFlag){
                if(!scene || !token || !sig || !csessionid){
                    faldia('请先拖动滑块！');
                    return false;
                }
            }

            $.post(INDEX_URL + '/user_regmobileCode', {
                scene:scene,
                token:token,
                sig:sig,
                csessionid:csessionid,
                phone: phone,
                type: 4,
                verify_type:1,
                phone_prefix:phone_prefix
            }, function (data) {
                if (data.success) {
                    $("input[name=mobilecode]").removeAttr('disabled');
                    startClock(1);
                    $(".get-mobile-code").data('clicked', true).addClass('disabled').html("(" + waitSec + ")秒重新发送");
                } else {
                    faldia(data.msg);
                    getAliCaptcha('two');
                    $("input[name=mobilecode]").removeAttr('disabled');
                    $(".get-mobile-code").html("重新获取").data('clicked', false).removeClass('disabled');
                }
            }, 'json');
            return false;
        });
    }

    mobileCode();
</script> <script>

    function getCaptcha() {
        getAliCaptcha('two');

    }

    function getAliCaptcha(num){
        var renderDom = '#dom_id_'+num;
        var csessionidDom = 'csessionid_'+num;
        var sigDom = 'sig_'+num;
        var tokenDom = 'token_'+num;
        var sceneDom = 'scene_'+num;
        var nc = new noCaptcha();
        var nc_appkey = 'QNYX';  // 应用标识,不可更改
        var nc_scene = 'login';  //场景,不可更改
        var nc_token = [nc_appkey, (new Date()).getTime(), Math.random()].join(':');
        var nc_option = {
            renderTo: renderDom,
            appkey: nc_appkey,
            scene: nc_scene,
            token: nc_token,
            callback: function (data) {
                document.getElementById(csessionidDom).value = data.csessionid;
                document.getElementById(sigDom).value = data.sig;
                document.getElementById(tokenDom).value = nc_token;
                document.getElementById(sceneDom).value = nc_scene;
            }
        };
        nc.init(nc_option);
    }
    
    $('#verifyLogin').on('click',function(){
        getAliCaptcha('two');
        if($("input[name=nameNormal]").val()){
          $("input[name=nameVerify]").val($("input[name=nameNormal]").val());
        }else{
          setTimeout(function() {$("input[name=nameVerify]").focus();}, 10);
        }
        $('#verifyLoginPanel').show();
        $('#normalLoginPanel').hide();
        window.localStorage.setItem('logintype',0);
    });
    $('#normalLogin').on('click',function(){
        getAliCaptcha('one');
        if($("input[name=nameVerify]").val()){
          $("input[name=nameNormal]").val($("input[name=nameVerify]").val());
        }
        $('#normalLoginPanel').show();
        $('#verifyLoginPanel').hide();
        window.localStorage.setItem('logintype',1);
    });

    $.ajax({
        type: "get",
        url: "/material/theme/chacha/cms/v2/images/phoneCode.json",
        dataType: "json",
        success: function(data) {
            $('.phone_prefix_ul').empty();
            $('.phone_prefix_ul').append('<li onclick="pSelect(this)" value="+86"><span> 中国</span>+86</li>');
            $.each(data,function(i,v){
                $('.phone_prefix_ul').append('<li onclick="pSelect(this)" value="+'+v.country_code+'"><span> '+v.country_name_cn+'</span>+'+v.country_code+'</li>');
            })
        }
    });
    function pSelect(dom){
      var tname = $(dom).find('span').text();
      if(tname.length>5){
        tname = tname.substr(0,6)+'…';
      }
      $('.phone_prefix').html(tname+' +'+dom.value+'<b class="caret text-primary"></b>');
      $('.phone_prefix_input').val('+'+dom.value);
      var width = 58;
      if($('#verifyLoginPanel').is(':visible')){
        width = $('#verifyLoginPanel .phone_prefix').width();
      }else{
        width = $('#normalLoginPanel .phone_prefix').width();
      }
      $('.phoneline').css('left',width+18);
      $('.login-panel .phone-select+input').css('padding-left',width+27);
    }
    $('.show-pwd').click(function(){
        if($('.show-pwd').hasClass('active')){
            $('.show-pwd').removeClass('active');
            $('.show-pwd').next().attr('type','password');
        }else{
            $('.show-pwd').addClass('active');
            $('.show-pwd').next().attr('type','text');
        }
    });
    var loginJumpUrl;
    $('#loginModal').on('show.bs.modal', function (e) {
        loginQrcodeGenerate('qrcodeModalLogin');
        loginQrcodePoll('qrcodeModalLogin');
    })
    $('#loginModal').on('hidden.bs.modal', function (e) {
        clearInterval(loginQrcodePollTimer);
    })
    setLoginType();
</script> <style type="text/css">
    #vipModal .modal-dialog{
        width: 780px;
    }
    #vipModal .modal-content{
        padding-bottom: 25px;
        border-radius: 0px;
        text-align: center;

    }
    #vipModal .close{
        color: #FFF;
        font-size: 40px;
        opacity: 0.8;
        font-weight: normal;
        position: absolute;
        right: 10px;
    }

    .step2{display: none;}
</style> <link type="text/css" href="/material/theme/chacha/cms/v2/css/vip-modal.css?version=20190326" rel="stylesheet"/> <div class="modal fade" id="vipModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal"> <div class="modal-content"> <div class="vip-top"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <div class="vip-title"> <h2 class="title">立即成为VIP</h2> <h3 class="sub-title"><span>更多特权 超值服务</span><a href="/vip">全部特权></a></h3> </div> <div class="vip-buy-panel"> <div class="vip-year-list clearfix"> <div data-id="17" data-year="3" data-price="720" class="vip-kuang vip-year active"> <div class="price"> <span>720元</span> <span class="vip-pay">/</span>
                                3年
                            </div> <div class="origin-price">原价：2160元</div> <div class="vip-rec"></div> </div> <div data-id="7" data-year="2" data-price="540" class="vip-kuang vip-year"> <div class="price"> <span>540元</span> <span class="vip-pay">/</span>
                                2年
                            </div> <div class="origin-price">原价：1440元</div> </div> <div data-id="6" data-year="1" data-price="360" class="vip-kuang vip-year"> <div class="price"> <span>360元</span> <span class="vip-pay">/</span>
                                1年
                            </div> <div class="origin-price">原价：720元</div> </div> </div> <div class="step1 m-t-md"> <a onclick="modalJumpVip()" class="vip-btn">立即开通</a> <div class="vip-publicity">支付后可开发票</div> </div> <form id="pay-form" class="vip-pay-info step2" target="aliPayFrame" role="form" method="post" action="/order_pay"> <div class="clearfix"> <span class="pre">购买账号：</span><span class="after"></span> </div> <div class="clearfix coupon-drop" > <span class="pre">优惠券：</span><span  data-toggle="dropdown" class="after drop"><span id="couponText">暂无优惠券</span><span class="caret"></span></span> <ul class="dropdown-menu" id="couponList"> <li> <span class="coupon-type">暂无优惠券</span> </li> </ul> </div> <div class="clearfix  m-b-xs"> <span class="pre">实付金额：</span><span class="after vip-pay" id="payYear">¥720.00</span> </div> <input type="hidden" name="order_type" value="2"/> <input type="hidden" name="goods_id" value="17"/> <input type="hidden" name="pay_type" value="2"/> <input type="hidden" name="coupon_code" value=""/> <input type="submit" class="btn btn-primary packages-btn" value="立即支付" style="display: none"/> </form> </div> </div> <div class="vip-pay-container clearfix"> <div class="step1"> <img class="demo-img" src="/material/theme/chacha/cms/v2/images/vip/fxsm.png"/> <a class="vip-demo-link" href=""></a> </div> <div class="step2"> <div class="vip-payj-left"> <div onclick="checkPay(2)" class="pay-type pay-type-wx active"></div> <div onclick="checkPay(1)" class="pay-type pay-type-ali m-t-xs"></div> <div class="m-t-lg"> <p>1.完成支付后可在我的-我的发票中申请发票</p> <p>2.VIP会员自支付完成之时起5分钟内生效</p> </div> </div> <div class="vip-payj-qrcode"> <div class="wx_pay_box"> <div id="wx_pay_img" class="wx_pay_img"></div> <img class="pay-load" src="/material/theme/chacha/cms/v2/images/preloader.gif"> </div> <div class="ali_pay_box" loading-img="/material/theme/chacha/cms/v2/images/preloader.gif"> <img class="pay-load" src="/material/theme/chacha/cms/v2/images/preloader.gif"> </div> </div> </div> </div> </div> </div> </div> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/pay.js?time=20190326"></script> <script type="text/javascript">
    var vipModalTitle;
    var userid = '';

    function showVipModal(title, subTitle, img, linkName, linkUrl, isStep2){

        if(!userid){
            getCaptcha();
            $('#loginModal').modal('show');
            return;
        }

        $("#vipModal .step1").show();
        $("#vipModal .step2").hide();

        if(title){
            $('#vipModal .vip-title .title').text(title);
            //vipModalTitle = title;
        }
        if(subTitle){
            $('#vipModal .vip-title .sub-title span').text(subTitle);
        }
        if(img){
            if(title == '雷达监控'){
                var imgUrl = "/material/theme/chacha/cms/v2/images/vip/ldjk.png";
                $("#vipModal .demo-img").attr("src",imgUrl);
            } else {
                var imgUrl = "/material/theme/chacha/cms/v2/images/vip/"+img+".png";
                $("#vipModal .demo-img").attr("src",imgUrl);
            }
        } else {
            var imgUrl = "/material/theme/chacha/cms/v2/images/vip/default.png";
            $("#vipModal .demo-img").attr("src",imgUrl);
        }
        if(linkName && linkUrl){
            $("#vipModal .vip-demo-link").show();
            $("#vipModal .vip-demo-link").text(linkName + '>');
            $("#vipModal .vip-demo-link").attr('href',linkUrl);
        } else {
            $("#vipModal .vip-demo-link").hide();
        }

        /*if(isStep2){
            $("#vipModal .step1").hide();
            $("#vipModal .step2").show();
            strartBuy();
        }*/

        $('#vipModal').modal('show');

        // 嵌入的关闭
        $(".vip-insert-wrap .step1").show();
        $(".vip-insert-wrap .step2").hide();
    }

    $('#vipModal').on('hide.bs.modal',function(){
        clearPay();
        isPayShow = false;
    })

    function modalJumpVip(){
        isPayShow = true;

        strartBuy();

        $("#vipModal .step1").hide();
        $("#vipModal .step2").show();

        /*yaojie old
        location.href = INDEX_URL+'/vip?goods_id='+$("input[name='goods_id']").val();
        if(vipModalTitle){
            //zhugeTrack(vipModalTitle.split(' ')[0]+'-开通VIP');
        }else{
            //zhugeTrack('VIP弹框-开通VIP');
        }*/
    }

    var isPayShow = false;
    var wxOrderStatus = 0;
    var wxOrderCode = '';
    var wxpayLoad = false;
    var alipayLoad = false;
    var cPayType = 2;
    var isModalShow = true;
    var cGoods_id = "17";
    var cYear = "3";
    var cPrice = "720";

    $('#vipModal .vip-year-list .vip-kuang').on('click',function(){
        changeYear($(this).attr('data-id'),$(this).attr('data-year'),$(this).attr('data-price'),this);
        var couponCode = $("#vipModal input[name='coupon_code']").val();
        if(couponCode == ''){
            //checkPay(cPayType);
        }
    });


    var siModel = null;
    function strartBuy(){
        if(typeof siModel != 'undefined' && siModel){
            clearInterval(siModel);
            siModel = null;
        }
        if(typeof siInsert != 'undefined' && siInsert){
            clearInterval(siInsert);
            siInsert = null;
        }
        siModel = setInterval(function(){
            getWxPayStatus();
        }, 3000);
        //checkPay(cPayType);
        setTimeout(function() {
            getcouponlist(cGoods_id);
        }, 300);
    }
</script> <style type="text/css">
    #confirmModal .btn{
        width: 90px;
        font-size: 12px;
    }

    #confirmModal .title>.bd{
        min-height: 42px;
        display: table-cell;
        vertical-align: middle;
    }
   
    #confirmModal .icon-warning{
        top: 3px;
    }
</style> <div class="modal fade" id="confirmModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal" style="width: 500px;"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">提示</h4> </div> <div class="modal-body clearfix"> <div class="title font-16 clearfix"> <div class="bd"> <span class="icon-warning"></span> </div> <div class="bd" style="padding-left: 10px;"> <span id="tkConfirmTitle">此操作永久删除，是否继续</span> </div> </div> <div class="btn-area m-t-md pull-right"> <a class="btn btn-default m-r-xs" data-dismiss="modal">取消</a> <a class="btn btn-primary" data-dismiss="modal" onclick="tkConfirmFuc()">确认删除</a> </div> </div> </div> </div> </div> <script type="text/javascript">
    var tkConfirmFuc;
    function tkConfirm(fuc,title) {
        $('#confirmModal').modal('show');
        tkConfirmFuc = fuc;
        if(title){
            $('#tkConfirmTitle').text(title);
        }else{
            $('#tkConfirmTitle').text('此操作永久删除，是否继续');
        }
    }
    function tkConfirmOk(){
        tkConfirmFuc();
    }
</script> <div id="openSuspend" class="openSuspend" style="cursor:pointer;"></div> <div class="bottomSuspend" id="bottomSuspend" style="margin-left: -100%;background-image: url('/material/theme/chacha/cms/v2/images/footer_cert_banner.png');"> <div id="attendDownload" class="attendDownload" data-href="https://www.qichacha.com/order_certpay"></div> <div id="closeSuspend" class="closeSuspend"></div> </div> <script type="text/javascript">
    bottomSus();
</script> </body> </html>

'''
import re
from bs4 import BeautifulSoup
rep = BeautifulSoup(html,'lxml')
labels = rep.select('label[class="text-dark-lter"] input')[:-2]
# print(labels)
for i in labels:
    # print(i)
    name = i.get('data-name').replace('<em>','').replace('</em>','')
    link = i.get('value')
    print(name,link)