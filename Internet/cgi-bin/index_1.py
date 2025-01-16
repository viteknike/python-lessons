# print('Content-type: text/html; charset=utf-8')
# print()
# print('<html><head><title>Заголовок</title></head><body style="text-align: center">')
# print('<h1>Ебал твой рот</h1>')
# print('<p>Первая Web-страница!')
# print('</body></html>')

print("Content-type: text/html; charset=utf-8")
print('''<html itemscope="" itemtype="https://schema.org/QAPage" class="html__responsive " lang="ru"><head>

        <title>python - What is the pythonic way to loop through two arrays at the same time? - Stack Overflow</title>
        <link rel="shortcut icon" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/favicon.ico?v=ec617d715196">
        <link rel="apple-touch-icon" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a">
        <link rel="image_src" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a"> 
        <link rel="search" type="application/opensearchdescription+xml" title="Stack Overflow" href="/opensearch.xml">
        <link rel="canonical" href="https://stackoverflow.com/questions/14293869/what-is-the-pythonic-way-to-loop-through-two-arrays-at-the-same-time">
    <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, minimum-scale=1.0">
        <meta name="bingbot" content="noarchive">         
        <meta property="og:type" content="website">
        <meta property="og:url" content="https://stackoverflow.com/questions/14293869/what-is-the-pythonic-way-to-loop-through-two-arrays-at-the-same-time">
        <meta property="og:site_name" content="Stack Overflow">
        <meta property="og:image" itemprop="image primaryImageOfPage" content="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded">
        <meta name="twitter:card" content="summary">
        <meta name="twitter:domain" content="stackoverflow.com">
        <meta name="twitter:title" property="og:title" itemprop="name" content="What is the pythonic way to loop through two arrays at the same time?">
        <meta name="twitter:description" property="og:description" itemprop="description" content="If I have two arrays, of the same length - say a and b

a = [4,6,2,6,7,3,6,7,2,5]

b = [6,4,6,3,2,7,8,5,3,5]

normally, I would do this like so:

for i in range(len(a)):
    print a[i] + b[i]
rather ">
    <script async="" src="https://www.google-analytics.com/analytics.js"></script><script id="webpack-public-path" type="text/uri-list">https://cdn.sstatic.net/</script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script defer="" src="https://cdn.sstatic.net/Js/third-party/npm/@stackoverflow/stacks/dist/js/stacks.min.js?v=fe3ef2b1305f"></script>
    <script src="https://cdn.sstatic.net/Js/stub.en.js?v=44cbb4d4d062"></script>

    <link rel="stylesheet" type="text/css" href="https://cdn.sstatic.net/Shared/stacks.css?v=1e9dfb1f6199">
    <link rel="stylesheet" type="text/css" href="https://cdn.sstatic.net/Sites/stackoverflow/primary.css?v=90f1fc95eb69">


    
            <link rel="alternate" type="application/atom+xml" title="Feed for question 'What is the pythonic way to loop through two arrays at the same time?'" href="/feeds/question/14293869">
        <script>
            StackExchange.ready(function () {

                    StackExchange.using("snippets", function () {
                        StackExchange.snippets.initSnippetRenderer();
                    });
                    
                StackExchange.using("postValidation", function () {
                    StackExchange.postValidation.initOnBlurAndSubmit($('#post-form'), 2, 'answer');
                });


                StackExchange.question.init({showAnswerHelp:true,showTrendingSortLaunchPopover:false,showTrendingSortPostLaunchPopover:false,totalCommentCount:0,shownCommentCount:0,enableTables:true,questionId:14293869});

                styleCode();

                    StackExchange.realtime.subscribeToQuestion('1', '14293869');
                    StackExchange.using("gps", function () { StackExchange.gps.trackOutboundClicks('#content', '.js-post-body'); });


            });
        </script>

        
        
        
        <link rel="stylesheet" type="text/css" href="https://cdn.sstatic.net/Shared/Channels/channels.css?v=5981bb1a5bd7">

        
        

    


    <script type="application/json" data-role="module-args" data-module-name="Shared/options.mod">{"options":{"locale":"en","serverTime":1734895760,"routeName":"Questions/Show","stackAuthUrl":"https://stackauth.com","networkMetaHostname":"meta.stackexchange.com","site":{"name":"Stack Overflow","description":"Q\u0026A for professional and enthusiast programmers","isNoticesTabEnabled":true,"enableNewTagCreationWarning":true,"insertSpaceAfterNameTabCompletion":false,"id":1,"cookieDomain":".stackoverflow.com","childUrl":"https://meta.stackoverflow.com","negativeVoteScoreFloor":null,"enableSocialMediaInSharePopup":true,"protocol":"https"},"user":{"fkey":"d75a38c9f46387c074e42866b21fab101776168769fc53229633006b67a9d8d5","tid":"f7a37f77-762a-4586-8978-1bd55c94f394","rep":0,"isAnonymous":true,"isAnonymousNetworkWide":true,"ab":{"collectives_survey":{"v":"coso_survey","g":1},"mobile_signup_link":{"v":"question_assistant","g":1}}},"events":{"postType":{"question":1},"postEditionSection":{"title":1,"body":2,"tags":3}}}}</script>
<script type="application/json" data-role="module-args" data-module-name="Shared/settings.mod">{"settings":{"mentions":{"maxNumUsersInDropdown":50},"paths":{"jQueryUIJSPath":"https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.0/jquery-ui.min.js","jQueryUICSSPath":"https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.0/themes/smoothness/jquery-ui.css"},"intercom":{"appId":"inf0secd"},"subscriptions":{"defaultBasicMaxTrueUpSeats":250,"defaultMaxTrueUpSeats":1000,"defaultFreemiumMaxTrueUpSeats":50},"questionLinkTitleReplacement":{"maxNumberOfSitesProcessed":10,"maxReplacementsPerSite":20},"flags":{"allowRetractingCommentFlags":true,"allowRetractingFlags":true},"image":{"maxImageUploadSizeInBytesAnimatedGif":2097152,"maxImageUploadSizeInBytes":10485760},"site":{"enableUserHovercards":true,"enableImageHttps":true,"allowImageUploads":true,"styleCode":true,"stacksEditorPreviewEnabled":true,"forceHttpsImages":true},"questions":{"questionTitleLengthStartLiveWarningChars":50,"enableSavesFeature":true,"enableQuestionTitleLengthLiveWarning":true,"maxTitleSize":150},"userMessaging":{"showNewFeatureNotice":true},"markdown":{"enableTables":true},"search":{},"legal":{"useCustomConsent":false,"oneTrustTCFConfigId":"c3d9f1e3-55f3-4eba-b268-46cee4c6789c"},"auth":{"oauthInPopup":true},"accounts":{"currentPasswordRequiredForChangingStackIdPassword":true},"tags":{},"elections":{"opaVoteResultsBaseUrl":"https://www.opavote.com/results/"},"snippets":{"snippetsEnabled":true,"renderDomain":"stacksnippets.net"},"comments":{}}}</script>
<script>StackExchange.init();</script>

    <script>
        StackExchange.using.setCacheBreakers({"Js/adops.en.js":"6da43f5e0a84","Js/ask.en.js":"","Js/begin-edit-event.en.js":"20edbaccceae","Js/copy-transpiled.en.js":"7959520085c5","Js/events.en.js":"","Js/explore-qlist.en.js":"ee2a4f8c3992","Js/full-anon.en.js":"756e9cf92803","Js/full.en.js":"db82f5b1e046","Js/highlightjs-loader.en.js":"dec53251ce5d","Js/inline-tag-editing.en.js":"8517756a2cb6","Js/keyboard-shortcuts.en.js":"c255a5a5979b","Js/markdown-it-loader.en.js":"5818ef89ff9d","Js/mentions-transpiled.en.js":"54b80f913964","Js/moderator.en.js":"038dfaeac3b5","Js/postCollections-transpiled.en.js":"fd1c4a681d04","Js/post-validation.en.js":"6c596a8d33b1","Js/question-editor.en.js":"","Js/review-v2-transpiled.en.js":"b80294337dec","Js/revisions.en.js":"9dd135bb585f","Js/stacks-editor.en.js":"8de4a63a68e8","Js/tageditor.en.js":"4d22c6090e5a","Js/tageditornew.en.js":"4554c63a5fa6","Js/tagsuggestions.en.js":"d9e40cbceb75","Js/unlimited-transpiled.en.js":"8713a979101d","Js/wmd.en.js":"8e5e21c8ea03","Js/snippet-javascript-codemirror.en.js":"8aaa42d59dbc"});
        StackExchange.using("gps", function() {
             StackExchange.gps.init(true);
        });
    </script>
    <noscript id="noscript-css"><style>body,.s-topbar{margin-top:1.9em}</style></noscript>
    <script src="https://cdn.cookielaw.org/scripttemplates/202409.2.0/otBannerSdk.js" async="" type="text/javascript"></script><style id="svelte-9quauz">a.svelte-9quauz{outline:none}</style><style id="svelte-209kup">h1.svelte-209kup{font-size:13px;font-weight:400;overflow:hidden;text-align:center;color:var(--black-400)}h1.svelte-209kup:before,h1.svelte-209kup:after{content:"";display:inline-block;width:50%;margin:0 0.5em 0 -55%;vertical-align:middle;border-bottom:1px solid;border-color:var(--black-225)}h1.svelte-209kup:after{margin:0 -55% 0 0.5em}</style><style id="svelte-1rlgrxv">.show-hide-password.svelte-1rlgrxv{position:absolute;top:8px;right:8px;border:none;background:none;padding:0;cursor:pointer}</style><script src="https://accounts.google.com/gsi/client" async=""></script><style id="svelte-12r9hfl">.s-input-icon.svelte-12r9hfl+.chips.svelte-12r9hfl{margin-left:25px}</style><script async="" src="https://cdn.sstatic.net/Js/full-anon.en.js?v=756e9cf92803"></script><style id="googleidentityservice_button_styles">.qJTHM{-webkit-user-select:none;color:#202124;direction:ltr;-webkit-touch-callout:none;font-family:"Roboto-Regular",arial,sans-serif;-webkit-font-smoothing:antialiased;font-weight:400;margin:0;overflow:hidden;-webkit-text-size-adjust:100%}.ynRLnc{left:-9999px;position:absolute;top:-9999px}.L6cTce{display:none}.bltWBb{word-break:break-all}.hSRGPd{color:#1a73e8;cursor:pointer;font-weight:500;text-decoration:none}.Bz112c-W3lGp{height:16px;width:16px}.Bz112c-E3DyYd{height:20px;width:20px}.Bz112c-r9oPif{height:24px;width:24px}.Bz112c-uaxL4e{-webkit-border-radius:10px;border-radius:10px}.LgbsSe-Bz112c{display:block}.S9gUrf-YoZ4jf,.S9gUrf-YoZ4jf *{border:none;margin:0;padding:0}.fFW7wc-ibnC6b>.aZ2wEe>div{border-color:#4285f4}.P1ekSe-ZMv3u>div:nth-child(1){background-color:#1a73e8!important}.P1ekSe-ZMv3u>div:nth-child(2),.P1ekSe-ZMv3u>div:nth-child(3){background-image:linear-gradient(to right,rgba(255,255,255,.7),rgba(255,255,255,.7)),linear-gradient(to right,#1a73e8,#1a73e8)!important}.haAclf{display:inline-block}.nsm7Bb-HzV7m-LgbsSe{-webkit-border-radius:4px;border-radius:4px;-webkit-box-sizing:border-box;box-sizing:border-box;-webkit-transition:background-color .218s,border-color .218s;transition:background-color .218s,border-color .218s;-webkit-user-select:none;-webkit-appearance:none;background-color:#fff;background-image:none;border:1px solid #dadce0;color:#3c4043;cursor:pointer;font-family:"Google Sans",arial,sans-serif;font-size:14px;height:40px;letter-spacing:0.25px;outline:none;overflow:hidden;padding:0 12px;position:relative;text-align:center;vertical-align:middle;white-space:nowrap;width:auto}@media screen and (-ms-high-contrast:active){.nsm7Bb-HzV7m-LgbsSe{border:2px solid windowText;color:windowText}}.nsm7Bb-HzV7m-LgbsSe.pSzOP-SxQuSe{font-size:14px;height:32px;letter-spacing:0.25px;padding:0 10px}.nsm7Bb-HzV7m-LgbsSe.purZT-SxQuSe{font-size:11px;height:20px;letter-spacing:0.3px;padding:0 8px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe{padding:0;width:40px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe.pSzOP-SxQuSe{width:32px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe.purZT-SxQuSe{width:20px}.nsm7Bb-HzV7m-LgbsSe.JGcpL-RbRzK{-webkit-border-radius:20px;border-radius:20px}.nsm7Bb-HzV7m-LgbsSe.JGcpL-RbRzK.pSzOP-SxQuSe{-webkit-border-radius:16px;border-radius:16px}.nsm7Bb-HzV7m-LgbsSe.JGcpL-RbRzK.purZT-SxQuSe{-webkit-border-radius:10px;border-radius:10px}.nsm7Bb-HzV7m-LgbsSe.MFS4be-Ia7Qfc{border:none;color:#fff}.nsm7Bb-HzV7m-LgbsSe.MFS4be-v3pZbf-Ia7Qfc{background-color:#1a73e8}.nsm7Bb-HzV7m-LgbsSe.MFS4be-JaPV2b-Ia7Qfc{background-color:#202124;color:#e8eaed}.nsm7Bb-HzV7m-LgbsSe .nsm7Bb-HzV7m-LgbsSe-Bz112c{height:18px;margin-right:8px;min-width:18px;width:18px}.nsm7Bb-HzV7m-LgbsSe.pSzOP-SxQuSe .nsm7Bb-HzV7m-LgbsSe-Bz112c{height:14px;min-width:14px;width:14px}.nsm7Bb-HzV7m-LgbsSe.purZT-SxQuSe .nsm7Bb-HzV7m-LgbsSe-Bz112c{height:10px;min-width:10px;width:10px}.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-Bz112c{margin-left:8px;margin-right:-4px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe .nsm7Bb-HzV7m-LgbsSe-Bz112c{margin:0;padding:10px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe.pSzOP-SxQuSe .nsm7Bb-HzV7m-LgbsSe-Bz112c{padding:8px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe.purZT-SxQuSe .nsm7Bb-HzV7m-LgbsSe-Bz112c{padding:4px}.nsm7Bb-HzV7m-LgbsSe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{-webkit-border-top-left-radius:3px;border-top-left-radius:3px;-webkit-border-bottom-left-radius:3px;border-bottom-left-radius:3px;display:-webkit-box;display:-webkit-flex;display:flex;justify-content:center;-webkit-align-items:center;align-items:center;background-color:#fff;height:36px;margin-left:-10px;margin-right:12px;min-width:36px;width:36px}.nsm7Bb-HzV7m-LgbsSe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf .nsm7Bb-HzV7m-LgbsSe-Bz112c,.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf .nsm7Bb-HzV7m-LgbsSe-Bz112c{margin:0;padding:0}.nsm7Bb-HzV7m-LgbsSe.pSzOP-SxQuSe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{height:28px;margin-left:-8px;margin-right:10px;min-width:28px;width:28px}.nsm7Bb-HzV7m-LgbsSe.purZT-SxQuSe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{height:16px;margin-left:-6px;margin-right:8px;min-width:16px;width:16px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{-webkit-border-radius:3px;border-radius:3px;margin-left:2px;margin-right:0;padding:0}.nsm7Bb-HzV7m-LgbsSe.JGcpL-RbRzK .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{-webkit-border-radius:18px;border-radius:18px}.nsm7Bb-HzV7m-LgbsSe.pSzOP-SxQuSe.JGcpL-RbRzK .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{-webkit-border-radius:14px;border-radius:14px}.nsm7Bb-HzV7m-LgbsSe.purZT-SxQuSe.JGcpL-RbRzK .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{-webkit-border-radius:8px;border-radius:8px}.nsm7Bb-HzV7m-LgbsSe .nsm7Bb-HzV7m-LgbsSe-bN97Pc-sM5MNb{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-align-items:center;align-items:center;-webkit-flex-direction:row;flex-direction:row;justify-content:space-between;-webkit-flex-wrap:nowrap;flex-wrap:nowrap;height:100%;position:relative;width:100%}.nsm7Bb-HzV7m-LgbsSe .oXtfBe-l4eHX{justify-content:center}.nsm7Bb-HzV7m-LgbsSe .nsm7Bb-HzV7m-LgbsSe-BPrWId{-webkit-flex-grow:1;flex-grow:1;font-family:"Google Sans",arial,sans-serif;font-weight:500;overflow:hidden;text-overflow:ellipsis;vertical-align:top}.nsm7Bb-HzV7m-LgbsSe.purZT-SxQuSe .nsm7Bb-HzV7m-LgbsSe-BPrWId{font-weight:300}.nsm7Bb-HzV7m-LgbsSe .oXtfBe-l4eHX .nsm7Bb-HzV7m-LgbsSe-BPrWId{-webkit-flex-grow:0;flex-grow:0}.nsm7Bb-HzV7m-LgbsSe .nsm7Bb-HzV7m-LgbsSe-MJoBVe{-webkit-transition:background-color .218s;transition:background-color .218s;bottom:0;left:0;position:absolute;right:0;top:0}.nsm7Bb-HzV7m-LgbsSe:hover,.nsm7Bb-HzV7m-LgbsSe:focus{-webkit-box-shadow:none;box-shadow:none;border-color:#d2e3fc;outline:none}.nsm7Bb-HzV7m-LgbsSe:hover .nsm7Bb-HzV7m-LgbsSe-MJoBVe,.nsm7Bb-HzV7m-LgbsSe:focus .nsm7Bb-HzV7m-LgbsSe-MJoBVe{background:rgba(66,133,244,.04)}.nsm7Bb-HzV7m-LgbsSe:active .nsm7Bb-HzV7m-LgbsSe-MJoBVe{background:rgba(66,133,244,.1)}.nsm7Bb-HzV7m-LgbsSe.MFS4be-Ia7Qfc:hover .nsm7Bb-HzV7m-LgbsSe-MJoBVe,.nsm7Bb-HzV7m-LgbsSe.MFS4be-Ia7Qfc:focus .nsm7Bb-HzV7m-LgbsSe-MJoBVe{background:rgba(255,255,255,.24)}.nsm7Bb-HzV7m-LgbsSe.MFS4be-Ia7Qfc:active .nsm7Bb-HzV7m-LgbsSe-MJoBVe{background:rgba(255,255,255,.32)}.nsm7Bb-HzV7m-LgbsSe .n1UuX-DkfjY{-webkit-border-radius:50%;border-radius:50%;display:-webkit-box;display:-webkit-flex;display:flex;height:20px;margin-left:-4px;margin-right:8px;min-width:20px;width:20px}.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-BPrWId{font-family:"Roboto";font-size:12px;text-align:left}.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-BPrWId .ssJRIf,.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-BPrWId .K4efff .fmcmS{overflow:hidden;text-overflow:ellipsis}.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-BPrWId .K4efff{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-align-items:center;align-items:center;color:#5f6368;fill:#5f6368;font-size:11px;font-weight:400}.nsm7Bb-HzV7m-LgbsSe.jVeSEe.MFS4be-Ia7Qfc .nsm7Bb-HzV7m-LgbsSe-BPrWId .K4efff{color:#e8eaed;fill:#e8eaed}.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-BPrWId .K4efff .Bz112c{height:18px;margin:-3px -3px -3px 2px;min-width:18px;width:18px}.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{-webkit-border-top-left-radius:0;border-top-left-radius:0;-webkit-border-bottom-left-radius:0;border-bottom-left-radius:0;-webkit-border-top-right-radius:3px;border-top-right-radius:3px;-webkit-border-bottom-right-radius:3px;border-bottom-right-radius:3px;margin-left:12px;margin-right:-10px}.nsm7Bb-HzV7m-LgbsSe.jVeSEe.JGcpL-RbRzK .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{-webkit-border-radius:18px;border-radius:18px}.L5Fo6c-sM5MNb{border:0;display:block;left:0;position:relative;top:0}.L5Fo6c-bF1uUb{-webkit-border-radius:4px;border-radius:4px;bottom:0;cursor:pointer;left:0;position:absolute;right:0;top:0}.L5Fo6c-bF1uUb:focus{border:none;outline:none}sentinel{}</style><link id="googleidentityservice" type="text/css" media="all" href="https://accounts.google.com/gsi/style" rel="stylesheet"><script async="" src="https://cdn.sstatic.net/Js/post-validation.en.js?v=6c596a8d33b1"></script><script async="" src="https://cdn.sstatic.net/Js/highlightjs-loader.en.js?v=dec53251ce5d"></script><style>#tr-popup,#tr-popup * {all: unset;}#tr-popup {font: 15px "Segoe UI", Arial, Helvetica, sans-serif;color: #222;padding: 24px;display: block;z-index: 2147483647;position: absolute;max-width: 400px;min-width: 300px;direction: ltr;text-align: left;background: #fff;border-radius: 2px;box-sizing: border-box;box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.1), 0 12px 24px 0 rgba(51, 51, 51, 0.3);transition: opacity, visibility;transition-duration: 0.2s;}#tr-popup[data-hidden="true"] {opacity: 0;visibility: hidden;}#tr-popup[data-position="top"] {margin-top: -12px;}#tr-popup[data-position="bottom"] {margin-top: 12px;}#tr-popup .tr-popup__arrow {top: 100%;left: 50%;width: 26px;height: 12px;display: block;position: absolute;margin-left: -13px;margin-top: -1px;background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNiIgaGVpZ2h0PSIxMiI+PHBhdGggZD0iTTAgMGwxMyAxMkwyNiAweiIgb3BhY2l0eT0iLjEiLz48cGF0aCBkPSJNMSAwbDEyIDExTDI1IDB6IiBmaWxsPSIjZmZmIi8+PC9zdmc+") no-repeat;}#tr-popup[data-position="bottom"] .tr-popup__arrow {top: auto;bottom: 100%;margin-bottom: -1px;transform: rotate(180deg);}#tr-popup .tr-popup__value,#tr-popup .tr-popup__block {word-wrap: break-word;white-space: pre-wrap;}[data-type="trSpan"][data-translated="true"][data-source-lang="ja"],[data-type="trSpan"][data-translated="true"][data-source-lang="zh"],#tr-popup .tr-popup__title_original,#tr-popup .tr-popup__block_a,#tr-popup .tr-popup__block_b,#tr-popup .tr-popup__button {font-family: "Segoe UI", Arial, Helvetica, sans-serif !important;}#tr-popup .tr-popup__title_original {font-weight: bold;}#tr-popup .tr-popup__block {display: block;}#tr-popup .tr-popup__link {cursor: pointer;-webkit-user-select: none;user-select: none;}#tr-popup .tr-popup__link_suggest {color: #1378d7;font-size: 13px;line-height: 18px;margin-right: 22px;}#tr-popup .tr-popup__link_suggest:hover,#tr-popup .tr-popup__link_suggest:active {color: #000;}#tr-popup .tr-popup__logo {height: 18px;opacity: 0.3;display: inline-block;transition: opacity 0.2s;vertical-align: top;}#tr-popup .tr-popup__logo_company {width: 34px;filter: brightness(0);background: url("https://yastatic.net/s3/trbro/v20.5.1.0/i/service_logo.svg");background-size: 34px;background-position: 0 -18px;}#tr-popup[lang="ru"] .tr-popup__logo_company {background-position: 0 0;}#tr-popup .tr-popup__logo_service {width: 42px;background: url("https://yastatic.net/s3/trbro/v20.5.1.0/i/service_name.svg");margin-left: 2px;background-size: 63px;background-position: 0 -18px;}#tr-popup[lang="ru"] .tr-popup__logo_service {width: 57px;background-position: 0 0;}#tr-popup[lang="uk"] .tr-popup__logo_service {width: 56px;background-position: 0 -36px;}#tr-popup[lang="tr"] .tr-popup__logo_service {width: 25px;background-position: 0 -54px;}#tr-popup .tr-popup__link_service:hover .tr-popup__logo {opacity: 0.6;}#tr-popup .tr-popup__input {width: 100%;height: 80px;resize: none;border: 2px solid #e5e5e5;padding: 8px;display: block;font-size: 15px;box-sizing: border-box;border-radius: 2px;}#tr-popup .tr-popup__input:focus {border-color: #bbb;}#tr-popup .tr-popup__block_a,#tr-popup .tr-popup__block_b {margin-top: 16px;}#tr-popup .tr-popup__block_a {display: flex;justify-content: space-between;}#tr-popup .tr-popup__block_b {position: relative;}#tr-popup .tr-popup__block_submit {text-align: right;margin-top: 24px;}#tr-popup .tr-popup__overlay {top: 0;left: 0;right: 0;bottom: 0;position: absolute;}#tr-popup .tr-popup__overlay_submitted {color: #999;z-index: 1;display: flex;background: #fff;align-items: center;justify-content: center;}#tr-popup:not([data-expanded="true"]) .tr-popup__block_b,#tr-popup:not([data-submitted="true"]) .tr-popup__overlay_submitted {display: none;}#tr-popup .tr-popup__menu {font-size: 13px;opacity: 0;visibility: hidden;white-space: nowrap;position: absolute;bottom: 100%;margin-bottom: 8px;padding: 4px 14px;z-index: 1;background-color: #f5f5f5;border: 1px solid #bbb;border-radius: 2px;box-shadow: 0px 0 0 1px rgba(0, 0, 0, 0.1), 0 8px 14px 0 rgba(51, 51, 51, 0.3);}#tr-popup[data-menu-position="left"] .tr-popup__menu {right: 0;}#tr-popup[data-menu="true"] .tr-popup__menu {opacity: 1;visibility: visible;}#tr-popup .tr-popup__menu:hover {background-color: #efefef;}#tr-popup .tr-popup__button {cursor: pointer;display: inline-block;-webkit-user-select: none;user-select: none;}#tr-popup .tr-popup__button_menu,#tr-popup .tr-popup__button_close {top: 4px;width: 20px;height: 20px;opacity: 0.3;position: absolute;}#tr-popup .tr-popup__button_close {right: 4px;background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMCIgaGVpZ2h0PSIyMCI+PHBhdGggZD0iTTkuMjkzIDEwTDYuMTQ2IDYuODU0YS41LjUgMCAxIDEgLjcwOC0uNzA4TDEwIDkuMjkzbDMuMTQ2LTMuMTQ3YS41LjUgMCAwIDEgLjcwOC43MDhMMTAuNzA3IDEwbDMuMTQ3IDMuMTQ2YS41LjUgMCAwIDEtLjcwOC43MDhMMTAgMTAuNzA3bC0zLjE0NiAzLjE0N2EuNS41IDAgMCAxLS43MDgtLjcwOEw5LjI5MyAxMHoiLz48L3N2Zz4=");}#tr-popup .tr-popup__button_menu {right: 24px;background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjAiIHdpZHRoPSIyMCI+PHBhdGggZD0ibTUgNnYxaDEwdi0xaC0xMHptMCAzdjFoMTB2LTFoLTEwem0wIDN2MWgxMHYtMWgtMTB6Ii8+PC9zdmc+");}#tr-popup .tr-popup__button_menu:hover,#tr-popup .tr-popup__button_close:hover {opacity: 0.5;}#tr-popup .tr-popup__button_close:active {opacity: 0.6;}#tr-popup[data-menu="true"] .tr-popup__button_menu {opacity: 1;}#tr-popup .tr-popup__button_submit {color: #000;height: 28px;padding: 0 16px;font-size: 13px;min-width: 112px;background: #fc0;box-sizing: border-box;text-align: center;line-height: 28px;border-radius: 2px;}#tr-popup .tr-popup__button_submit:hover {background: #ffb800;}#tr-popup .tr-popup__button_submit:active {background: #ffa400;}#tr-popup[data-invalid="true"] .tr-popup__button_submit {color: rgba(0, 0, 0, 0.5);cursor: default;background: rgba(0, 0, 0, 0.1);}[data-type="trSpan"][data-selected="true"] {color: #222 !important;background: #cce4f7 !important;}[data-type="trSpan"] {font-size: inherit !important;}</style><style id="onetrust-style">#onetrust-banner-sdk .onetrust-vendors-list-handler{cursor:pointer;color:#1f96db;font-size:inherit;font-weight:bold;text-decoration:none;margin-left:5px}#onetrust-banner-sdk .onetrust-vendors-list-handler:hover{color:#1f96db}#onetrust-banner-sdk:focus{outline:2px solid #000;outline-offset:-2px}#onetrust-banner-sdk a:focus{outline:2px solid #000}#onetrust-banner-sdk #onetrust-accept-btn-handler,#onetrust-banner-sdk #onetrust-reject-all-handler,#onetrust-banner-sdk #onetrust-pc-btn-handler{outline-offset:1px}#onetrust-banner-sdk.ot-bnr-w-logo .ot-bnr-logo{height:64px;width:64px}#onetrust-banner-sdk .ot-tcf2-vendor-count.ot-text-bold{font-weight:bold}#onetrust-banner-sdk .ot-close-icon,#onetrust-pc-sdk .ot-close-icon,#ot-sync-ntfy .ot-close-icon{background-size:contain;background-repeat:no-repeat;background-position:center;height:12px;width:12px}#onetrust-banner-sdk .powered-by-logo,#onetrust-banner-sdk .ot-pc-footer-logo a,#onetrust-pc-sdk .powered-by-logo,#onetrust-pc-sdk .ot-pc-footer-logo a,#ot-sync-ntfy .powered-by-logo,#ot-sync-ntfy .ot-pc-footer-logo a{background-size:contain;background-repeat:no-repeat;background-position:center;height:25px;width:152px;display:block;text-decoration:none;font-size:.75em}#onetrust-banner-sdk .powered-by-logo:hover,#onetrust-banner-sdk .ot-pc-footer-logo a:hover,#onetrust-pc-sdk .powered-by-logo:hover,#onetrust-pc-sdk .ot-pc-footer-logo a:hover,#ot-sync-ntfy .powered-by-logo:hover,#ot-sync-ntfy .ot-pc-footer-logo a:hover{color:#565656}#onetrust-banner-sdk h3 *,#onetrust-banner-sdk h4 *,#onetrust-banner-sdk h6 *,#onetrust-banner-sdk button *,#onetrust-banner-sdk a[data-parent-id] *,#onetrust-pc-sdk h3 *,#onetrust-pc-sdk h4 *,#onetrust-pc-sdk h6 *,#onetrust-pc-sdk button *,#onetrust-pc-sdk a[data-parent-id] *,#ot-sync-ntfy h3 *,#ot-sync-ntfy h4 *,#ot-sync-ntfy h6 *,#ot-sync-ntfy button *,#ot-sync-ntfy a[data-parent-id] *{font-size:inherit;font-weight:inherit;color:inherit}#onetrust-banner-sdk .ot-hide,#onetrust-pc-sdk .ot-hide,#ot-sync-ntfy .ot-hide{display:none !important}#onetrust-banner-sdk button.ot-link-btn:hover,#onetrust-pc-sdk button.ot-link-btn:hover,#ot-sync-ntfy button.ot-link-btn:hover{text-decoration:underline;opacity:1}#onetrust-pc-sdk .ot-sdk-row .ot-sdk-column{padding:0}#onetrust-pc-sdk .ot-sdk-container{padding-right:0}#onetrust-pc-sdk .ot-sdk-row{flex-direction:initial;width:100%}#onetrust-pc-sdk [type=checkbox]:checked,#onetrust-pc-sdk [type=checkbox]:not(:checked){pointer-events:initial}#onetrust-pc-sdk [type=checkbox]:disabled+label::before,#onetrust-pc-sdk [type=checkbox]:disabled+label:after,#onetrust-pc-sdk [type=checkbox]:disabled+label{pointer-events:none;opacity:.8}#onetrust-pc-sdk #vendor-list-content{transform:translate3d(0, 0, 0)}#onetrust-pc-sdk li input[type=checkbox]{z-index:1}#onetrust-pc-sdk li .ot-checkbox label{z-index:2}#onetrust-pc-sdk li .ot-checkbox input[type=checkbox]{height:auto;width:auto}#onetrust-pc-sdk li .host-title a,#onetrust-pc-sdk li .ot-host-name a,#onetrust-pc-sdk li .accordion-text,#onetrust-pc-sdk li .ot-acc-txt{z-index:2;position:relative}#onetrust-pc-sdk input{margin:3px .1ex}#onetrust-pc-sdk .pc-logo,#onetrust-pc-sdk .ot-pc-logo{height:60px;width:180px;background-position:center;background-size:contain;background-repeat:no-repeat;display:inline-flex;justify-content:center;align-items:center}#onetrust-pc-sdk .pc-logo img,#onetrust-pc-sdk .ot-pc-logo img{max-height:100%;max-width:100%}#onetrust-pc-sdk .screen-reader-only,#onetrust-pc-sdk .ot-scrn-rdr,.ot-sdk-cookie-policy .screen-reader-only,.ot-sdk-cookie-policy .ot-scrn-rdr{border:0;clip:rect(0 0 0 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px}#onetrust-pc-sdk.ot-fade-in,.onetrust-pc-dark-filter.ot-fade-in,#onetrust-banner-sdk.ot-fade-in{animation-name:onetrust-fade-in;animation-duration:400ms;animation-timing-function:ease-in-out}#onetrust-pc-sdk.ot-hide{display:none !important}.onetrust-pc-dark-filter.ot-hide{display:none !important}#ot-sdk-btn.ot-sdk-show-settings,#ot-sdk-btn.optanon-show-settings{color:#68b631;border:1px solid #68b631;height:auto;white-space:normal;word-wrap:break-word;padding:.8em 2em;font-size:.8em;line-height:1.2;cursor:pointer;-moz-transition:.1s ease;-o-transition:.1s ease;-webkit-transition:1s ease;transition:.1s ease}#ot-sdk-btn.ot-sdk-show-settings:hover,#ot-sdk-btn.optanon-show-settings:hover{color:#fff;background-color:#68b631}.onetrust-pc-dark-filter{background:rgba(0,0,0,.5);z-index:2147483646;width:100%;height:100%;overflow:hidden;position:fixed;top:0;bottom:0;left:0}@keyframes onetrust-fade-in{0%{opacity:0}100%{opacity:1}}.ot-cookie-label{text-decoration:underline}@media only screen and (min-width: 426px)and (max-width: 896px)and (orientation: landscape){#onetrust-pc-sdk p{font-size:.75em}}#onetrust-banner-sdk .banner-option-input:focus+label{outline:1px solid #000;outline-style:auto}.category-vendors-list-handler+a:focus,.category-vendors-list-handler+a:focus-visible{outline:2px solid #000}#onetrust-pc-sdk .ot-userid-title{margin-top:10px}#onetrust-pc-sdk .ot-userid-title>span,#onetrust-pc-sdk .ot-userid-timestamp>span{font-weight:700}#onetrust-pc-sdk .ot-userid-desc{font-style:italic}#onetrust-pc-sdk .ot-host-desc a{pointer-events:initial}#onetrust-pc-sdk .ot-ven-hdr>p a{position:relative;z-index:2;pointer-events:initial}#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info a,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-vnd-info a{margin-right:auto}#onetrust-pc-sdk .ot-pc-footer-logo img{width:136px;height:16px}#onetrust-pc-sdk .ot-pur-vdr-count{font-weight:400;font-size:.7rem;padding-top:3px;display:block}#onetrust-banner-sdk .ot-optout-signal,#onetrust-pc-sdk .ot-optout-signal{border:1px solid #32ae88;border-radius:3px;padding:5px;margin-bottom:10px;background-color:#f9fffa;font-size:.85rem;line-height:2}#onetrust-banner-sdk .ot-optout-signal .ot-optout-icon,#onetrust-pc-sdk .ot-optout-signal .ot-optout-icon{display:inline;margin-right:5px}#onetrust-banner-sdk .ot-optout-signal svg,#onetrust-pc-sdk .ot-optout-signal svg{height:20px;width:30px;transform:scale(0.5)}#onetrust-banner-sdk .ot-optout-signal svg path,#onetrust-pc-sdk .ot-optout-signal svg path{fill:#32ae88}#onetrust-consent-sdk .ot-general-modal{overflow:hidden;position:fixed;margin:0 auto;top:50%;left:50%;width:40%;padding:1.5rem;max-width:575px;min-width:575px;z-index:2147483647;border-radius:2.5px;transform:translate(-50%, -50%)}#onetrust-consent-sdk .ot-signature-health-group{margin-top:1rem;padding-left:1.25rem;padding-right:1.25rem;margin-bottom:.625rem;width:calc(100% - 2.5rem)}#onetrust-consent-sdk .ot-signature-health-group .ot-signature-health-form{gap:.5rem}#onetrust-consent-sdk .ot-signature-health .ot-signature-health-form{width:70%;gap:.35rem}#onetrust-consent-sdk .ot-signature-health .ot-signature-input{height:38px;padding:6px 10px;background-color:#fff;border:1px solid #d1d1d1;border-radius:4px;box-shadow:none;box-sizing:border-box}#onetrust-consent-sdk .ot-signature-health .ot-signature-subtitle{font-size:1.125rem}#onetrust-consent-sdk .ot-signature-health .ot-signature-group-title{font-size:1.25rem;font-weight:bold}#onetrust-consent-sdk .ot-signature-health,#onetrust-consent-sdk .ot-signature-health-group{display:flex;flex-direction:column;gap:1rem}#onetrust-consent-sdk .ot-signature-health .ot-signature-cont,#onetrust-consent-sdk .ot-signature-health-group .ot-signature-cont{display:flex;flex-direction:column;gap:.25rem}#onetrust-consent-sdk .ot-signature-health .ot-signature-paragraph,#onetrust-consent-sdk .ot-signature-health-group .ot-signature-paragraph{margin:0;line-height:20px;font-size:max(14px,.875rem)}#onetrust-consent-sdk .ot-signature-health .ot-health-signature-error,#onetrust-consent-sdk .ot-signature-health-group .ot-health-signature-error{color:#4d4d4d;font-size:min(12px,.75rem)}#onetrust-consent-sdk .ot-signature-health .ot-signature-buttons-cont,#onetrust-consent-sdk .ot-signature-health-group .ot-signature-buttons-cont{margin-top:max(.75rem,2%);gap:1rem;display:flex;justify-content:flex-end}#onetrust-consent-sdk .ot-signature-health .ot-signature-button,#onetrust-consent-sdk .ot-signature-health-group .ot-signature-button{flex:1;height:auto;color:#fff;cursor:pointer;line-height:1.2;min-width:125px;font-weight:600;font-size:.813em;border-radius:2px;padding:12px 10px;white-space:normal;word-wrap:break-word;word-break:break-word;background-color:#68b631;border:2px solid #68b631}#onetrust-consent-sdk .ot-signature-health .ot-signature-button.reject,#onetrust-consent-sdk .ot-signature-health-group .ot-signature-button.reject{background-color:#fff}#onetrust-consent-sdk .ot-input-field-cont{display:flex;flex-direction:column;gap:.5rem}#onetrust-consent-sdk .ot-input-field-cont .ot-signature-input{width:65%}#onetrust-consent-sdk .ot-signature-health-form{display:flex;flex-direction:column}#onetrust-consent-sdk .ot-signature-health-form .ot-signature-label{margin-bottom:0;line-height:20px;font-size:max(14px,.875rem)}@media only screen and (max-width: 600px){#onetrust-consent-sdk .ot-general-modal{min-width:100%}#onetrust-consent-sdk .ot-signature-health .ot-signature-health-form{width:100%}#onetrust-consent-sdk .ot-input-field-cont .ot-signature-input{width:100%}}#onetrust-banner-sdk,#onetrust-pc-sdk,#ot-sdk-cookie-policy,#ot-sync-ntfy{font-size:16px}#onetrust-banner-sdk *,#onetrust-banner-sdk ::after,#onetrust-banner-sdk ::before,#onetrust-pc-sdk *,#onetrust-pc-sdk ::after,#onetrust-pc-sdk ::before,#ot-sdk-cookie-policy *,#ot-sdk-cookie-policy ::after,#ot-sdk-cookie-policy ::before,#ot-sync-ntfy *,#ot-sync-ntfy ::after,#ot-sync-ntfy ::before{-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box}#onetrust-banner-sdk div,#onetrust-banner-sdk span,#onetrust-banner-sdk h1,#onetrust-banner-sdk h2,#onetrust-banner-sdk h3,#onetrust-banner-sdk h4,#onetrust-banner-sdk h5,#onetrust-banner-sdk h6,#onetrust-banner-sdk p,#onetrust-banner-sdk img,#onetrust-banner-sdk svg,#onetrust-banner-sdk button,#onetrust-banner-sdk section,#onetrust-banner-sdk a,#onetrust-banner-sdk label,#onetrust-banner-sdk input,#onetrust-banner-sdk ul,#onetrust-banner-sdk li,#onetrust-banner-sdk nav,#onetrust-banner-sdk table,#onetrust-banner-sdk thead,#onetrust-banner-sdk tr,#onetrust-banner-sdk td,#onetrust-banner-sdk tbody,#onetrust-banner-sdk .ot-main-content,#onetrust-banner-sdk .ot-toggle,#onetrust-banner-sdk #ot-content,#onetrust-banner-sdk #ot-pc-content,#onetrust-banner-sdk .checkbox,#onetrust-pc-sdk div,#onetrust-pc-sdk span,#onetrust-pc-sdk h1,#onetrust-pc-sdk h2,#onetrust-pc-sdk h3,#onetrust-pc-sdk h4,#onetrust-pc-sdk h5,#onetrust-pc-sdk h6,#onetrust-pc-sdk p,#onetrust-pc-sdk img,#onetrust-pc-sdk svg,#onetrust-pc-sdk button,#onetrust-pc-sdk section,#onetrust-pc-sdk a,#onetrust-pc-sdk label,#onetrust-pc-sdk input,#onetrust-pc-sdk ul,#onetrust-pc-sdk li,#onetrust-pc-sdk nav,#onetrust-pc-sdk table,#onetrust-pc-sdk thead,#onetrust-pc-sdk tr,#onetrust-pc-sdk td,#onetrust-pc-sdk tbody,#onetrust-pc-sdk .ot-main-content,#onetrust-pc-sdk .ot-toggle,#onetrust-pc-sdk #ot-content,#onetrust-pc-sdk #ot-pc-content,#onetrust-pc-sdk .checkbox,#ot-sdk-cookie-policy div,#ot-sdk-cookie-policy span,#ot-sdk-cookie-policy h1,#ot-sdk-cookie-policy h2,#ot-sdk-cookie-policy h3,#ot-sdk-cookie-policy h4,#ot-sdk-cookie-policy h5,#ot-sdk-cookie-policy h6,#ot-sdk-cookie-policy p,#ot-sdk-cookie-policy img,#ot-sdk-cookie-policy svg,#ot-sdk-cookie-policy button,#ot-sdk-cookie-policy section,#ot-sdk-cookie-policy a,#ot-sdk-cookie-policy label,#ot-sdk-cookie-policy input,#ot-sdk-cookie-policy ul,#ot-sdk-cookie-policy li,#ot-sdk-cookie-policy nav,#ot-sdk-cookie-policy table,#ot-sdk-cookie-policy thead,#ot-sdk-cookie-policy tr,#ot-sdk-cookie-policy td,#ot-sdk-cookie-policy tbody,#ot-sdk-cookie-policy .ot-main-content,#ot-sdk-cookie-policy .ot-toggle,#ot-sdk-cookie-policy #ot-content,#ot-sdk-cookie-policy #ot-pc-content,#ot-sdk-cookie-policy .checkbox,#ot-sync-ntfy div,#ot-sync-ntfy span,#ot-sync-ntfy h1,#ot-sync-ntfy h2,#ot-sync-ntfy h3,#ot-sync-ntfy h4,#ot-sync-ntfy h5,#ot-sync-ntfy h6,#ot-sync-ntfy p,#ot-sync-ntfy img,#ot-sync-ntfy svg,#ot-sync-ntfy button,#ot-sync-ntfy section,#ot-sync-ntfy a,#ot-sync-ntfy label,#ot-sync-ntfy input,#ot-sync-ntfy ul,#ot-sync-ntfy li,#ot-sync-ntfy nav,#ot-sync-ntfy table,#ot-sync-ntfy thead,#ot-sync-ntfy tr,#ot-sync-ntfy td,#ot-sync-ntfy tbody,#ot-sync-ntfy .ot-main-content,#ot-sync-ntfy .ot-toggle,#ot-sync-ntfy #ot-content,#ot-sync-ntfy #ot-pc-content,#ot-sync-ntfy .checkbox{font-family:inherit;font-weight:normal;-webkit-font-smoothing:auto;letter-spacing:normal;line-height:normal;padding:0;margin:0;height:auto;min-height:0;max-height:none;width:auto;min-width:0;max-width:none;border-radius:0;border:none;clear:none;float:none;position:static;bottom:auto;left:auto;right:auto;top:auto;text-align:left;text-decoration:none;text-indent:0;text-shadow:none;text-transform:none;white-space:normal;background:none;overflow:visible;vertical-align:baseline;visibility:visible;z-index:auto;box-shadow:none}#onetrust-banner-sdk label:before,#onetrust-banner-sdk label:after,#onetrust-banner-sdk .checkbox:after,#onetrust-banner-sdk .checkbox:before,#onetrust-pc-sdk label:before,#onetrust-pc-sdk label:after,#onetrust-pc-sdk .checkbox:after,#onetrust-pc-sdk .checkbox:before,#ot-sdk-cookie-policy label:before,#ot-sdk-cookie-policy label:after,#ot-sdk-cookie-policy .checkbox:after,#ot-sdk-cookie-policy .checkbox:before,#ot-sync-ntfy label:before,#ot-sync-ntfy label:after,#ot-sync-ntfy .checkbox:after,#ot-sync-ntfy .checkbox:before{content:"";content:none}#onetrust-banner-sdk .ot-sdk-container,#onetrust-pc-sdk .ot-sdk-container,#ot-sdk-cookie-policy .ot-sdk-container{position:relative;width:100%;max-width:100%;margin:0 auto;padding:0 20px;box-sizing:border-box}#onetrust-banner-sdk .ot-sdk-column,#onetrust-banner-sdk .ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-column,#onetrust-pc-sdk .ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-column,#ot-sdk-cookie-policy .ot-sdk-columns{width:100%;float:left;box-sizing:border-box;padding:0;display:initial}@media(min-width: 400px){#onetrust-banner-sdk .ot-sdk-container,#onetrust-pc-sdk .ot-sdk-container,#ot-sdk-cookie-policy .ot-sdk-container{width:90%;padding:0}}@media(min-width: 550px){#onetrust-banner-sdk .ot-sdk-container,#onetrust-pc-sdk .ot-sdk-container,#ot-sdk-cookie-policy .ot-sdk-container{width:100%}#onetrust-banner-sdk .ot-sdk-column,#onetrust-banner-sdk .ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-column,#onetrust-pc-sdk .ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-column,#ot-sdk-cookie-policy .ot-sdk-columns{margin-left:4%}#onetrust-banner-sdk .ot-sdk-column:first-child,#onetrust-banner-sdk .ot-sdk-columns:first-child,#onetrust-pc-sdk .ot-sdk-column:first-child,#onetrust-pc-sdk .ot-sdk-columns:first-child,#ot-sdk-cookie-policy .ot-sdk-column:first-child,#ot-sdk-cookie-policy .ot-sdk-columns:first-child{margin-left:0}#onetrust-banner-sdk .ot-sdk-two.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-two.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-two.ot-sdk-columns{width:13.3333333333%}#onetrust-banner-sdk .ot-sdk-three.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-three.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-three.ot-sdk-columns{width:22%}#onetrust-banner-sdk .ot-sdk-four.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-four.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-four.ot-sdk-columns{width:30.6666666667%}#onetrust-banner-sdk .ot-sdk-eight.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-eight.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-eight.ot-sdk-columns{width:65.3333333333%}#onetrust-banner-sdk .ot-sdk-nine.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-nine.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-nine.ot-sdk-columns{width:74%}#onetrust-banner-sdk .ot-sdk-ten.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-ten.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-ten.ot-sdk-columns{width:82.6666666667%}#onetrust-banner-sdk .ot-sdk-eleven.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-eleven.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-eleven.ot-sdk-columns{width:91.3333333333%}#onetrust-banner-sdk .ot-sdk-twelve.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-twelve.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-twelve.ot-sdk-columns{width:100%;margin-left:0}}#onetrust-banner-sdk h1,#onetrust-banner-sdk h2,#onetrust-banner-sdk h3,#onetrust-banner-sdk h4,#onetrust-banner-sdk h5,#onetrust-banner-sdk h6,#onetrust-pc-sdk h1,#onetrust-pc-sdk h2,#onetrust-pc-sdk h3,#onetrust-pc-sdk h4,#onetrust-pc-sdk h5,#onetrust-pc-sdk h6,#ot-sdk-cookie-policy h1,#ot-sdk-cookie-policy h2,#ot-sdk-cookie-policy h3,#ot-sdk-cookie-policy h4,#ot-sdk-cookie-policy h5,#ot-sdk-cookie-policy h6{margin-top:0;font-weight:600;font-family:inherit}#onetrust-banner-sdk h1,#onetrust-pc-sdk h1,#ot-sdk-cookie-policy h1{font-size:1.5rem;line-height:1.2}#onetrust-banner-sdk h2,#onetrust-pc-sdk h2,#ot-sdk-cookie-policy h2{font-size:1.5rem;line-height:1.25}#onetrust-banner-sdk h3,#onetrust-pc-sdk h3,#ot-sdk-cookie-policy h3{font-size:1.5rem;line-height:1.3}#onetrust-banner-sdk h4,#onetrust-pc-sdk h4,#ot-sdk-cookie-policy h4{font-size:1.5rem;line-height:1.35}#onetrust-banner-sdk h5,#onetrust-pc-sdk h5,#ot-sdk-cookie-policy h5{font-size:1.5rem;line-height:1.5}#onetrust-banner-sdk h6,#onetrust-pc-sdk h6,#ot-sdk-cookie-policy h6{font-size:1.5rem;line-height:1.6}@media(min-width: 550px){#onetrust-banner-sdk h1,#onetrust-pc-sdk h1,#ot-sdk-cookie-policy h1{font-size:1.5rem}#onetrust-banner-sdk h2,#onetrust-pc-sdk h2,#ot-sdk-cookie-policy h2{font-size:1.5rem}#onetrust-banner-sdk h3,#onetrust-pc-sdk h3,#ot-sdk-cookie-policy h3{font-size:1.5rem}#onetrust-banner-sdk h4,#onetrust-pc-sdk h4,#ot-sdk-cookie-policy h4{font-size:1.5rem}#onetrust-banner-sdk h5,#onetrust-pc-sdk h5,#ot-sdk-cookie-policy h5{font-size:1.5rem}#onetrust-banner-sdk h6,#onetrust-pc-sdk h6,#ot-sdk-cookie-policy h6{font-size:1.5rem}}#onetrust-banner-sdk p,#onetrust-pc-sdk p,#ot-sdk-cookie-policy p{margin:0 0 1em 0;font-family:inherit;line-height:normal}#onetrust-banner-sdk a,#onetrust-pc-sdk a,#ot-sdk-cookie-policy a{color:#565656;text-decoration:underline}#onetrust-banner-sdk a:hover,#onetrust-pc-sdk a:hover,#ot-sdk-cookie-policy a:hover{color:#565656;text-decoration:none}#onetrust-banner-sdk .ot-sdk-button,#onetrust-banner-sdk button,#onetrust-pc-sdk .ot-sdk-button,#onetrust-pc-sdk button,#ot-sdk-cookie-policy .ot-sdk-button,#ot-sdk-cookie-policy button{margin-bottom:1rem;font-family:inherit}#onetrust-banner-sdk .ot-sdk-button,#onetrust-banner-sdk button,#onetrust-pc-sdk .ot-sdk-button,#onetrust-pc-sdk button,#ot-sdk-cookie-policy .ot-sdk-button,#ot-sdk-cookie-policy button{display:inline-block;height:38px;padding:0 30px;color:#555;text-align:center;font-size:.9em;font-weight:400;line-height:38px;letter-spacing:.01em;text-decoration:none;white-space:nowrap;background-color:rgba(0,0,0,0);border-radius:2px;border:1px solid #bbb;cursor:pointer;box-sizing:border-box}#onetrust-banner-sdk .ot-sdk-button:hover,#onetrust-banner-sdk :not(.ot-leg-btn-container)>button:not(.ot-link-btn):hover,#onetrust-banner-sdk :not(.ot-leg-btn-container)>button:not(.ot-link-btn):focus,#onetrust-pc-sdk .ot-sdk-button:hover,#onetrust-pc-sdk :not(.ot-leg-btn-container)>button:not(.ot-link-btn):hover,#onetrust-pc-sdk :not(.ot-leg-btn-container)>button:not(.ot-link-btn):focus,#ot-sdk-cookie-policy .ot-sdk-button:hover,#ot-sdk-cookie-policy :not(.ot-leg-btn-container)>button:not(.ot-link-btn):hover,#ot-sdk-cookie-policy :not(.ot-leg-btn-container)>button:not(.ot-link-btn):focus{color:#333;border-color:#888;opacity:.7}#onetrust-banner-sdk .ot-sdk-button:focus,#onetrust-banner-sdk :not(.ot-leg-btn-container)>button:focus,#onetrust-pc-sdk .ot-sdk-button:focus,#onetrust-pc-sdk :not(.ot-leg-btn-container)>button:focus,#ot-sdk-cookie-policy .ot-sdk-button:focus,#ot-sdk-cookie-policy :not(.ot-leg-btn-container)>button:focus{outline:2px solid #000}#onetrust-banner-sdk .ot-sdk-button.ot-sdk-button-primary,#onetrust-banner-sdk button.ot-sdk-button-primary,#onetrust-banner-sdk input[type=submit].ot-sdk-button-primary,#onetrust-banner-sdk input[type=reset].ot-sdk-button-primary,#onetrust-banner-sdk input[type=button].ot-sdk-button-primary,#onetrust-pc-sdk .ot-sdk-button.ot-sdk-button-primary,#onetrust-pc-sdk button.ot-sdk-button-primary,#onetrust-pc-sdk input[type=submit].ot-sdk-button-primary,#onetrust-pc-sdk input[type=reset].ot-sdk-button-primary,#onetrust-pc-sdk input[type=button].ot-sdk-button-primary,#ot-sdk-cookie-policy .ot-sdk-button.ot-sdk-button-primary,#ot-sdk-cookie-policy button.ot-sdk-button-primary,#ot-sdk-cookie-policy input[type=submit].ot-sdk-button-primary,#ot-sdk-cookie-policy input[type=reset].ot-sdk-button-primary,#ot-sdk-cookie-policy input[type=button].ot-sdk-button-primary{color:#fff;background-color:#33c3f0;border-color:#33c3f0}#onetrust-banner-sdk .ot-sdk-button.ot-sdk-button-primary:hover,#onetrust-banner-sdk button.ot-sdk-button-primary:hover,#onetrust-banner-sdk input[type=submit].ot-sdk-button-primary:hover,#onetrust-banner-sdk input[type=reset].ot-sdk-button-primary:hover,#onetrust-banner-sdk input[type=button].ot-sdk-button-primary:hover,#onetrust-banner-sdk .ot-sdk-button.ot-sdk-button-primary:focus,#onetrust-banner-sdk button.ot-sdk-button-primary:focus,#onetrust-banner-sdk input[type=submit].ot-sdk-button-primary:focus,#onetrust-banner-sdk input[type=reset].ot-sdk-button-primary:focus,#onetrust-banner-sdk input[type=button].ot-sdk-button-primary:focus,#onetrust-pc-sdk .ot-sdk-button.ot-sdk-button-primary:hover,#onetrust-pc-sdk button.ot-sdk-button-primary:hover,#onetrust-pc-sdk input[type=submit].ot-sdk-button-primary:hover,#onetrust-pc-sdk input[type=reset].ot-sdk-button-primary:hover,#onetrust-pc-sdk input[type=button].ot-sdk-button-primary:hover,#onetrust-pc-sdk .ot-sdk-button.ot-sdk-button-primary:focus,#onetrust-pc-sdk button.ot-sdk-button-primary:focus,#onetrust-pc-sdk input[type=submit].ot-sdk-button-primary:focus,#onetrust-pc-sdk input[type=reset].ot-sdk-button-primary:focus,#onetrust-pc-sdk input[type=button].ot-sdk-button-primary:focus,#ot-sdk-cookie-policy .ot-sdk-button.ot-sdk-button-primary:hover,#ot-sdk-cookie-policy button.ot-sdk-button-primary:hover,#ot-sdk-cookie-policy input[type=submit].ot-sdk-button-primary:hover,#ot-sdk-cookie-policy input[type=reset].ot-sdk-button-primary:hover,#ot-sdk-cookie-policy input[type=button].ot-sdk-button-primary:hover,#ot-sdk-cookie-policy .ot-sdk-button.ot-sdk-button-primary:focus,#ot-sdk-cookie-policy button.ot-sdk-button-primary:focus,#ot-sdk-cookie-policy input[type=submit].ot-sdk-button-primary:focus,#ot-sdk-cookie-policy input[type=reset].ot-sdk-button-primary:focus,#ot-sdk-cookie-policy input[type=button].ot-sdk-button-primary:focus{color:#fff;background-color:#1eaedb;border-color:#1eaedb}#onetrust-banner-sdk input[type=text],#onetrust-pc-sdk input[type=text],#ot-sdk-cookie-policy input[type=text]{height:38px;padding:6px 10px;background-color:#fff;border:1px solid #d1d1d1;border-radius:4px;box-shadow:none;box-sizing:border-box}#onetrust-banner-sdk input[type=text],#onetrust-pc-sdk input[type=text],#ot-sdk-cookie-policy input[type=text]{-webkit-appearance:none;-moz-appearance:none;appearance:none}#onetrust-banner-sdk input[type=text]:focus,#onetrust-pc-sdk input[type=text]:focus,#ot-sdk-cookie-policy input[type=text]:focus{border:1px solid #000;outline:0}#onetrust-banner-sdk label,#onetrust-pc-sdk label,#ot-sdk-cookie-policy label{display:block;margin-bottom:.5rem;font-weight:600}#onetrust-banner-sdk input[type=checkbox],#onetrust-pc-sdk input[type=checkbox],#ot-sdk-cookie-policy input[type=checkbox]{display:inline}#onetrust-banner-sdk ul,#onetrust-pc-sdk ul,#ot-sdk-cookie-policy ul{list-style:circle inside}#onetrust-banner-sdk ul,#onetrust-pc-sdk ul,#ot-sdk-cookie-policy ul{padding-left:0;margin-top:0}#onetrust-banner-sdk ul ul,#onetrust-pc-sdk ul ul,#ot-sdk-cookie-policy ul ul{margin:1.5rem 0 1.5rem 3rem;font-size:90%}#onetrust-banner-sdk li,#onetrust-pc-sdk li,#ot-sdk-cookie-policy li{margin-bottom:1rem}#onetrust-banner-sdk th,#onetrust-banner-sdk td,#onetrust-pc-sdk th,#onetrust-pc-sdk td,#ot-sdk-cookie-policy th,#ot-sdk-cookie-policy td{padding:12px 15px;text-align:left;border-bottom:1px solid #e1e1e1}#onetrust-banner-sdk button,#onetrust-pc-sdk button,#ot-sdk-cookie-policy button{margin-bottom:1rem;font-family:inherit}#onetrust-banner-sdk .ot-sdk-container:after,#onetrust-banner-sdk .ot-sdk-row:after,#onetrust-pc-sdk .ot-sdk-container:after,#onetrust-pc-sdk .ot-sdk-row:after,#ot-sdk-cookie-policy .ot-sdk-container:after,#ot-sdk-cookie-policy .ot-sdk-row:after{content:"";display:table;clear:both}#onetrust-banner-sdk .ot-sdk-row,#onetrust-pc-sdk .ot-sdk-row,#ot-sdk-cookie-policy .ot-sdk-row{margin:0;max-width:none;display:block}.ot-sdk-cookie-policy{font-family:inherit;font-size:16px}.ot-sdk-cookie-policy.otRelFont{font-size:1rem}.ot-sdk-cookie-policy h3,.ot-sdk-cookie-policy h4,.ot-sdk-cookie-policy h6,.ot-sdk-cookie-policy p,.ot-sdk-cookie-policy li,.ot-sdk-cookie-policy a,.ot-sdk-cookie-policy th,.ot-sdk-cookie-policy #cookie-policy-description,.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group,.ot-sdk-cookie-policy #cookie-policy-title{color:dimgray}.ot-sdk-cookie-policy #cookie-policy-description{margin-bottom:1em}.ot-sdk-cookie-policy h4{font-size:1.2em}.ot-sdk-cookie-policy h6{font-size:1em;margin-top:2em}.ot-sdk-cookie-policy th{min-width:75px}.ot-sdk-cookie-policy a,.ot-sdk-cookie-policy a:hover{background:#fff}.ot-sdk-cookie-policy thead{background-color:#f6f6f4;font-weight:bold}.ot-sdk-cookie-policy .ot-mobile-border{display:none}.ot-sdk-cookie-policy section{margin-bottom:2em}.ot-sdk-cookie-policy table{border-collapse:inherit}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy{font-family:inherit;font-size:1rem}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h3,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h4,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h6,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy p,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy li,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-title{color:dimgray}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description{margin-bottom:1em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-subgroup{margin-left:1.5em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group-desc,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-table-header,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy span,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td{font-size:.9em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td span,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td a{font-size:inherit}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group{font-size:1em;margin-bottom:.6em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-title{margin-bottom:1.2em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy>section{margin-bottom:1em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th{min-width:75px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a:hover{background:#fff}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy thead{background-color:#f6f6f4;font-weight:bold}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-mobile-border{display:none}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy section{margin-bottom:2em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-subgroup ul li{list-style:disc;margin-left:1.5em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-subgroup ul li h4{display:inline-block}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table{border-collapse:inherit;margin:auto;border:1px solid #d7d7d7;border-radius:5px;border-spacing:initial;width:100%;overflow:hidden}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table th,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table td{border-bottom:1px solid #d7d7d7;border-right:1px solid #d7d7d7}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr:last-child td{border-bottom:0px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr th:last-child,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr td:last-child{border-right:0px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-host,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-cookies-type{width:25%}.ot-sdk-cookie-policy[dir=rtl]{text-align:left}#ot-sdk-cookie-policy h3{font-size:1.5em}@media only screen and (max-width: 530px){.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) table,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) thead,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tbody,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) th,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr{display:block}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) thead tr{position:absolute;top:-9999px;left:-9999px}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr{margin:0 0 1em 0}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr:nth-child(odd),.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr:nth-child(odd) a{background:#f6f6f4}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td{border:none;border-bottom:1px solid #eee;position:relative;padding-left:50%}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td:before{position:absolute;height:100%;left:6px;width:40%;padding-right:10px}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) .ot-mobile-border{display:inline-block;background-color:#e4e4e4;position:absolute;height:100%;top:0;left:45%;width:2px}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td:before{content:attr(data-label);font-weight:bold}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) li{word-break:break-word;word-wrap:break-word}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table{overflow:hidden}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table td{border:none;border-bottom:1px solid #d7d7d7}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy thead,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy tbody,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy tr{display:block}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-host,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-cookies-type{width:auto}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy tr{margin:0 0 1em 0}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td:before{height:100%;width:40%;padding-right:10px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td:before{content:attr(data-label);font-weight:bold}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy li{word-break:break-word;word-wrap:break-word}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy thead tr{position:absolute;top:-9999px;left:-9999px;z-index:-9999}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr:last-child td{border-bottom:1px solid #d7d7d7;border-right:0px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr:last-child td:last-child{border-bottom:0px}}
                
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h5,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h6,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy li,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy p,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy span,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description {
                        color: #696969;
                    }
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th {
                        color: #696969;
                    }
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group {
                        color: #696969;
                    }
                    
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-title {
                            color: #696969;
                        }
                    
            
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table th {
                            background-color: #F8F8F8;
                        }
                    
            .ot-floating-button__front{background-image:url('https://cdn.cookielaw.org/logos/static/ot_persistent_cookie_icon.png')}</style></head>
    <body class="question-page unified-theme">

        
<div id="signup-modal-container"><aside class="s-modal" role="dialog" aria-hidden="true" aria-labelledby="signup-modal-title" aria-describedby="signup-modal-description"><div class="s-modal--dialog pt32 pr32 pb32" role="document"><h1 id="signup-modal-title" class="s-modal--header"><div slot="header" class="s-modal--header d-flex g4 mt8 ai-center"><img class="h48 w48 native" src="https://cdn.sstatic.net/Sites/stackoverflow/Img/icon-48.png?v=b7e36f88ff92" alt="логотип сайта"> <span class="fs-headline1 mb0 fc-black-700"><strong><ya-tr-span data-index="0-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Join Stack Overflow" data-translation="Присоединиться к переполнению стека" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Присоединиться к переполнению стека</ya-tr-span></strong></span></div></h1> <div id="signup-modal-description" class="s-modal--body"><div slot="body" class="wmx4 pl8"><div class="mb24"><span class="fs-caption fc-black-400 ta-left"><ya-tr-span data-index="1-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="By clicking “Sign up”, you agree to our" data-translation="Нажимая «Зарегистрироваться», вы соглашаетесь с нашими " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Нажимая «Зарегистрироваться», вы соглашаетесь с нашими </ya-tr-span> <a href="/legal/terms-of-service/public" target="_blank" rel="noopener noreferrer" class="s-link svelte-9quauz"><ya-tr-span data-index="1-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="terms of service" data-translation="условиями предоставления услуг" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">условиями предоставления услуг</ya-tr-span></a> <ya-tr-span data-index="1-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" and acknowledge you have read our" data-translation=" и подтверждаете, что ознакомились с нашей " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> и подтверждаете, что ознакомились с нашей </ya-tr-span> <a href="/legal/privacy-policy" target="_blank" rel="noopener noreferrer" class="s-link svelte-9quauz"><ya-tr-span data-index="1-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="privacy policy" data-translation="политикой конфиденциальности" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">политикой конфиденциальности</ya-tr-span></a><ya-tr-span data-index="1-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="." data-translation="." data-ch="0" data-type="trSpan" style="visibility: inherit !important;">.</ya-tr-span></span></div> <div class="pb32"><form class="flex--item" action="/users/signup?ssrc=undefined&amp;returnurl=https%3A%2F%2Fstackoverflow.com%2Fusers%2Fafter-signup%2Foauth-only" method="POST" target="oauth-frame"><input type="hidden" name="fkey" value="d75a38c9f46387c074e42866b21fab101776168769fc53229633006b67a9d8d5"> <input type="hidden" name="legalLinksShown" value="1"> <input type="hidden" name="ssrc" value="undefined">    <input type="hidden" name="oauth_version" value="2.0"> <input type="hidden" name="oauth_server"> <div class="d-flex fd-column gy12"><button class="s-btn w100 s-btn__google" type="submit" data-testid="signup-google" data-provider="Google"><div class="d-flex ai-center jc-center gx8"><svg aria-hidden="true" class="native svg-icon iconGoogle" width="18" height="18" viewBox="0 0 18 18"><path fill="#4285F4" d="M16.51 8H8.98v3h4.3c-.18 1-.74 1.48-1.6 2.04v2.01h2.6a7.8 7.8 0 0 0 2.38-5.88c0-.57-.05-.66-.15-1.18"></path><path fill="#34A853" d="M8.98 17c2.16 0 3.97-.72 5.3-1.94l-2.6-2a4.8 4.8 0 0 1-7.18-2.54H1.83v2.07A8 8 0 0 0 8.98 17"></path><path fill="#FBBC05" d="M4.5 10.52a4.8 4.8 0 0 1 0-3.04V5.41H1.83a8 8 0 0 0 0 7.18z"></path><path fill="#EA4335" d="M8.98 4.18c1.17 0 2.23.4 3.06 1.2l2.3-2.3A8 8 0 0 0 1.83 5.4L4.5 7.49a4.8 4.8 0 0 1 4.48-3.3"></path></svg> <ya-tr-span data-index="2-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Sign up with Google" data-translation="Зарегистрируйтесь в Google" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Зарегистрируйтесь в Google</ya-tr-span></div> </button><button class="s-btn w100 s-btn__google" type="submit" data-testid="signup-github" data-provider="GitHub"><div class="d-flex ai-center jc-center gx8"><svg aria-hidden="true" class="native svg-icon iconGitHub" width="18" height="18" viewBox="0 0 18 18"><path fill="#010101" d="M9 1a8 8 0 0 0-2.53 15.59c.4.07.55-.17.55-.38l-.01-1.49c-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.4 7.4 0 0 1 4 0c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48l-.01 2.2c0 .21.15.46.55.38A8.01 8.01 0 0 0 9 1"></path></svg> <ya-tr-span data-index="3-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Sign up with GitHub" data-translation="Зарегистрируйтесь на GitHub" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Зарегистрируйтесь на GitHub</ya-tr-span></div> </button></div></form></div> <h1 class="svelte-209kup"><ya-tr-span data-index="4-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="OR" data-translation="или" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">или</ya-tr-span></h1> <form id="signup-modal-signup-form" class="mt32 d-flex fd-column gy16" action="/users/signup?ssrc=undefined&amp;returnurl=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F14293869%2Fwhat-is-the-pythonic-way-to-loop-through-two-arrays-at-the-same-time" method="POST"><input type="hidden" name="fkey" value="d75a38c9f46387c074e42866b21fab101776168769fc53229633006b67a9d8d5"> <input type="hidden" name="legalLinksShown" value="1"> <input type="hidden" name="ssrc" value=""> <input type="hidden" name="vote" value=""> <input type="hidden" name="votehash" value=""> <input type="hidden" name="tagAction" value=""> <input type="hidden" name="tagNames" value=""> <input type="hidden" name="anonTheme" value=""> <div class="flex--item d-flex fd-column gs4 gsy  svelte-1rlgrxv"><label class="flex--item s-label" for="signup-modal-email"><ya-tr-span data-index="5-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Email" data-translation="Электронная почта" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Электронная почта</ya-tr-span></label> <div class="d-flex ps-relative"><input class="s-input" id="signup-modal-email" size="30" maxlength="100" name="email" autocomplete="off"></div> </div> <div class="flex--item d-flex fd-column gs4 gsy  svelte-1rlgrxv"><label class="flex--item s-label" for="signup-modal-password"><ya-tr-span data-index="6-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Password" data-translation="Пароль" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Пароль</ya-tr-span></label> <div class="d-flex ps-relative"><input id="signup-modal-password" class="flex--item s-input" type="password" autocomplete="new-password" name="password" placeholder="8+ символов (не менее 1 буквы и 1 цифры)"> <button type="button" class="show-hide-password svelte-1rlgrxv"><svg aria-hidden="true" class="svg-icon iconEyeOff" width="18" height="18" viewBox="0 0 18 18"><path d="m5.02 9.44-2.22 2.2C1.63 10.25 1 9 1 9s3-6 8.06-6q1.13.01 2.12.38L9.5 5.03 9 5a4 4 0 0 0-3.98 4.44m2.03 3.05A4 4 0 0 0 13 9q-.01-1.1-.54-2l-1.51 1.54q.05.22.05.46a2 2 0 0 1-2.44 1.95zm7.11-7.22A15 15 0 0 1 17 9s-3 6-7.94 6c-1.31 0-2.48-.4-3.5-1l-1.97 2L2 14.41 14.59 2 16 3.41z"></path></svg></button></div> </div>  <div class="flex--item d-flex gs4 gsy fd-column svelte-1rlgrxv"><button class="s-btn flex--item mt12 s-btn__filled" id="signup-modal-submit-button" name="submit-button" type="submit"><ya-tr-span data-index="7-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Sign up" data-translation="Регистрация" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Регистрация</ya-tr-span></button> <p class="flex--item s-input-message d-none svelte-1rlgrxv" aria-hidden="true" aria-live="assertive"></p></div></form></div></div> <div class="d-flex g8 s-modal--footer"><div slot="footer" class="fs-body1 pl8"><ya-tr-span data-index="8-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Already have an account?" data-translation="У вас уже есть аккаунт?" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">У вас уже есть аккаунт?</ya-tr-span>  <a href="/users/login" class="s-link"><ya-tr-span data-index="8-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Log in" data-translation="Вход" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Вход</ya-tr-span></a></div></div> <button class="s-btn s-modal--close s-btn__muted s-btn__icon" aria-label="Закрыть"><div class="modal-close"><ya-tr-span data-index="9-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="X" data-translation="X" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">X</ya-tr-span></div></button></div></aside></div>
<script type="application/json" data-role="module-args" data-module-name="islands/signup-modal/index.mod">{"ContainerElementId":"signup-modal-container","FKey":"d75a38c9f46387c074e42866b21fab101776168769fc53229633006b67a9d8d5","TriggerEvent":"signupModalShow","OauthInPopup":true,"ReturnUrl":"https://stackoverflow.com/questions/14293869/what-is-the-pythonic-way-to-loop-through-two-arrays-at-the-same-time","ReturnUrlForPopup":"https://stackoverflow.com/users/after-signup/oauth-only","SiteName":"Stack Overflow","SiteLogoPath":"https://cdn.sstatic.net/Sites/stackoverflow/Img/icon-48.png?v=b7e36f88ff92","AuthProviders":["Google","GitHub"],"ParentSiteUrl":"","IsInitiallyVisible":false}</script>
<script defer="" src="https://cdn.sstatic.net/Js/webpack-chunks/svelte.en.js?v=150134e89426"></script><script defer="" src="https://cdn.sstatic.net/Js/webpack-chunks/stacks-svelte.en.js?v=72feec5d5528"></script><script defer="" src="https://cdn.sstatic.net/Js/webpack-chunks/1315.en.js?v=d971ebf7a8e2"></script><script defer="" src="https://cdn.sstatic.net/Js/webpack-chunks/4537.en.js?v=e6769247457b"></script><script defer="" src="https://cdn.sstatic.net/Js/islands/signup-modal.en.js?v=70d42243ade4"></script>

<script defer="">
    dispatchEvent(new CustomEvent("openSignupModal"));
</script>
    
        <div id="one-tap-container"> <form id="one-tap-form" method="post" action="/users/auth/gcp?ssrc=google-one-tap&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f14293869%2fwhat-is-the-pythonic-way-to-loop-through-two-arrays-at-the-same-time"><input type="hidden" name="fKey" value="d75a38c9f46387c074e42866b21fab101776168769fc53229633006b67a9d8d5"> <input type="hidden" name="googleIdToken" value=""></form></div>
<script type="application/json" data-role="module-args" data-module-name="islands/one-tap/index.mod">{"ContainerElementId":"one-tap-container","FKey":"d75a38c9f46387c074e42866b21fab101776168769fc53229633006b67a9d8d5","GoogleClientId":"717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com","Autoselect":false,"ReturnUrl":"https%3a%2f%2fstackoverflow.com%2fquestions%2f14293869%2fwhat-is-the-pythonic-way-to-loop-through-two-arrays-at-the-same-time"}</script><script defer="" src="https://cdn.sstatic.net/Js/webpack-chunks/svelte.en.js?v=150134e89426"></script><script defer="" src="https://cdn.sstatic.net/Js/islands/one-tap.en.js?v=661858832214"></script>    <div id="notify-container"></div>
    <div id="custom-header"></div>
        

<header class="s-topbar ps-fixed t0 l0 js-top-bar">
    <a href="#content" class="s-topbar--skip-link"><ya-tr-span data-index="10-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Skip to main content" data-translation="Перейти к основному контенту" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Перейти к основному контенту</ya-tr-span></a>
	<div class="s-topbar--container">
			<a href="#" class="s-topbar--menu-btn js-left-sidebar-toggle" role="menuitem" aria-haspopup="true" aria-controls="left-sidebar" aria-expanded="false"><span></span></a>
			<div class="topbar-dialog leftnav-dialog js-leftnav-dialog dno">
				<div class="left-sidebar js-unpinned-left-sidebar" data-can-be="left-sidebar" data-is-here-when="sm"></div>
			</div>
				<a href="https://stackoverflow.com" class="s-topbar--logo js-gps-track" data-gps-track="top_nav.click({is_current:false, location:2, destination:8}); homelogo_nav.click({location:2})">
					<span class="-img _glyph"><ya-tr-span data-index="11-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Stack Overflow" data-translation="Переполнение стека" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Переполнение стека</ya-tr-span></span>
				</a>



			<ol class="s-navigation fw-nowrap" role="presentation">

					<li class="md:d-none">
						<a href="https://stackoverflow.co/" class="s-navigation--item js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:7})" data-ga="[&quot;top navigation&quot;,&quot;about menu click&quot;,null,null,null]"><ya-tr-span data-index="79-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="About" data-translation="О нас" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">О нас</ya-tr-span></a>
					</li>

				<li>
					<button class="s-navigation--item js-gps-track" type="button" aria-controls="products-popover" aria-expanded="false" data-controller="s-popover" data-action="s-popover#toggle" data-s-popover-toggle-class="is-selected" data-gps-track="top_nav.products.click({location:2, destination:1})" data-ga="[&quot;top navigation&quot;,&quot;products menu click&quot;,null,null,null]"><ya-tr-span data-index="12-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Products " data-translation=" Продукты " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Продукты  </ya-tr-span></button>
				</li>

                    <li class="md:d-none">
                        <a href="https://stackoverflow.co/teams/ai/?utm_medium=referral&amp;utm_source=stackoverflow-community&amp;utm_campaign=top-nav-bar&amp;utm_content=overflowai" class="s-navigation--item js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:10})" data-ga="[&quot;top navigation&quot;,&quot;learn more - overflowai&quot;,null,null,null]"><ya-tr-span data-index="80-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="OverflowAI" data-translation="Переполненный поток" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Переполненный поток</ya-tr-span></a>
                    </li>

			</ol>
			<div class="s-popover ws2 mtn2 p0" id="products-popover" role="menu" aria-hidden="true">
				<div class="s-popover--arrow"></div>
				<ol class="list-reset s-anchors s-anchors__inherit">
					<li class="m6">
						<a href="https://stackoverflow.co/teams/?utm_medium=referral&amp;utm_source=stackoverflow-community&amp;utm_campaign=top-nav&amp;utm_content=stack-overflow-for-teams" class="bar-sm p6 d-block h:bg-black-225 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:3})" data-ga="[&quot;top navigation&quot;,&quot;teams submenu click&quot;,null,null,null]">
							<span class="fs-body1 d-block">Stack Overflow for Teams</span>
							<span class="fs-caption d-block fc-black-400">Where developers &amp; technologists share private knowledge with coworkers</span>
						</a>
					</li>
					<li class="m6">
						<a href="https://stackoverflow.co/advertising/?utm_medium=referral&amp;utm_source=stackoverflow-community&amp;utm_campaign=top-nav&amp;utm_content=stack-overflow-advertising" class="bar-sm p6 d-block h:bg-black-225 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:6})" data-ga="[&quot;top navigation&quot;,&quot;advertising submenu click&quot;,null,null,null]">
							<span class="fs-body1 d-block">Advertising &amp; Talent</span>
							<span class="fs-caption d-block fc-black-400">Reach devs &amp; technologists worldwide about your product, service or employer brand</span>
						</a>
					</li>
					<li class="bt bc-black-200 pt6 px6 bbr-md">
						<a href="https://stackoverflow.co/teams/ai/?utm_medium=referral&amp;utm_source=stackoverflow-community&amp;utm_campaign=top-nav&amp;utm_content=overflow-ai" class="bar-sm p6 d-block h:bg-black-225 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:10})" data-ga="[&quot;top navigation&quot;,&quot;overflowai submenu click&quot;,null,null,null]">
						 	<span class="fs-body1 d-block">OverflowAI</span>
							<span class="fs-caption d-block fc-black-400">GenAI features for Teams</span>
						 </a>
					</li>
					<li class="pb6 px6 bbr-md">
						<a href="https://stackoverflow.co/api-solutions/?utm_medium=referral&amp;utm_source=stackoverflow-community&amp;utm_campaign=top-nav&amp;utm_content=overflow-api" class="bar-sm p6 d-block h:bg-black-225 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:11})" data-ga="[&quot;top navigation&quot;,&quot;overflowapi submenu click&quot;,null,null,null]">
						 	<span class="fs-body1 d-block">OverflowAPI</span>
							<span class="fs-caption d-block fc-black-400">Train &amp; fine-tune LLMs</span>
						 </a>
					</li>
					<li class="bt bc-black-200 py6 px6 bbr-md">
						<a href="https://stackoverflow.co/labs/?utm_medium=referral&amp;utm_source=stackoverflow-community&amp;utm_campaign=top-nav&amp;utm_content=labs" class="bar-sm p6 d-block h:bg-black-225 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:12})" data-ga="[&quot;top navigation&quot;,&quot;labs submenu click&quot;,null,null,null]">
						 	<span class="fs-body1 d-block">Labs</span>
							<span class="fs-caption d-block fc-black-400">The future of collective knowledge sharing</span>
						 </a>
					</li>
					<li class="bg-black-100 bt bc-black-200 py6 px6 bbr-md">
						<a href="https://stackoverflow.co/?utm_medium=referral&amp;utm_source=stackoverflow-community&amp;utm_campaign=top-nav&amp;utm_content=about-the-company" class="fc-black-400 d-block py6 px6 h:fc-black-600" data-ga="[&quot;top navigation&quot;,&quot;about submenu click&quot;,null,null,null]">About the company</a>

						<a href="https://stackoverflow.blog/?utm_medium=referral&amp;utm_source=stackoverflow-community&amp;utm_campaign=top-nav&amp;utm_content=blog" class="fc-black-400 d-block py6 px6 h:fc-black-600" data-ga="[&quot;top navigation&quot;,&quot;blog submenu click&quot;,null,null,null]">Visit the blog</a>
					</li>
				</ol>
			</div>


		        <form id="search" role="search" action="/search" class="s-topbar--searchbar js-searchbar " autocomplete="off">
                        <div class="s-topbar--searchbar--input-group">
                            <input name="q" type="text" role="combobox" placeholder="Поиск…" value="" autocomplete="off" maxlength="240" class="s-input s-input__search js-search-field wmn1 " aria-label="Поиск" aria-controls="top-search" data-controller="s-popover" data-action="focus->s-popover#show" data-s-popover-placement="bottom-start" aria-expanded="false">
                            <svg aria-hidden="true" class="s-input-icon s-input-icon__search svg-icon iconSearch" width="18" height="18" viewBox="0 0 18 18"><path d="m18 16.5-5.14-5.18h-.35a7 7 0 1 0-1.19 1.19v.35L16.5 18zM12 7A5 5 0 1 1 2 7a5 5 0 0 1 10 0"></path></svg>
                            <div class="s-popover p0 wmx100 wmn4 sm:wmn-initial js-top-search-popover" id="top-search" role="menu">
    <div class="s-popover--arrow"></div>
    <div class="s-popover--content">
        <div class="js-spinner p24 d-flex ai-center jc-center d-none">
            <div class="s-spinner s-spinner__sm fc-orange-400">
                <div class="v-visible-sr">Loading…</div>
            </div>
        </div>

        <span class="v-visible-sr js-screen-reader-info"></span>
        <div class="js-ac-results overflow-y-auto hmx3 d-none"></div>

        <div class="js-search-hints" aria-describedby="Tips for searching"></div>
    </div>
</div>
                        </div>
                </form>
		

<nav class="h100 ml-auto overflow-x-auto pr12" aria-label="Верхняя Панель">
    <ol class="s-topbar--content" role="menubar">
    
    
    
        <li class="js-topbar-dialog-corral" role="presentation">
                

    <div class="topbar-dialog siteSwitcher-dialog dno" role="menu">
        <div class="header fw-wrap">
            <h3 class="flex--item">
                <a href="https://stackoverflow.com">current community</a>
            </h3>
            <div class="flex--item fl1">
                <div class="ai-center d-flex jc-end">
                    <button class="js-close-button s-btn s-btn__muted p0 ml8 d-none sm:d-block" type="button" aria-label="Close">
                        <svg aria-hidden="true" class="svg-icon iconClear" width="18" height="18" viewBox="0 0 18 18"><path d="M15 4.41 13.59 3 9 7.59 4.41 3 3 4.41 7.59 9 3 13.59 4.41 15 9 10.41 13.59 15 15 13.59 10.41 9z"></path></svg>
                    </button>
                </div>
            </div>
        </div>
        <div class="modal-content bg-blue-200 current-site-container">
            <ul class="current-site">
                    <li class="d-flex">
                            <div class="fl1">
                <a href="https://stackoverflow.com" class="current-site-link d-flex gx8 site-link js-gps-track" data-id="1" data-gps-track="site_switcher.click({ item_type:3 })">
        <div class="favicon favicon-stackoverflow site-icon flex--item" title="Stack Overflow"></div>
        <span class="flex--item fl1">
            Stack Overflow
        </span>
    </a>

    </div>
    <div class="related-links">
            <a href="https://stackoverflow.com/help" class="js-gps-track" data-gps-track="site_switcher.click({ item_type:14 })">help</a>
            <a href="https://chat.stackoverflow.com/?tab=site&amp;host=stackoverflow.com" class="js-gps-track" data-gps-track="site_switcher.click({ item_type:6 })">chat</a>
    </div>

                    </li>
                    <li class="related-site d-flex">
                            <div class="L-shaped-icon-container">
        <span class="L-shaped-icon"></span>
    </div>

                            <a href="https://meta.stackoverflow.com" class="s-block-link px16 d-flex gx8 site-link js-gps-track" data-id="552" data-gps-track="site.switch({ target_site:552, item_type:3 }),site_switcher.click({ item_type:4 })">
        <div class="favicon favicon-stackoverflowmeta site-icon flex--item" title="Meta Stack Overflow"></div>
        <span class="flex--item fl1">
            Meta Stack Overflow
        </span>
    </a>

                    </li>
            </ul>
        </div>

        <div class="header" id="your-communities-header">
            <h3>
your communities            </h3>

        </div>
        <div class="modal-content" id="your-communities-section">

                <div class="call-to-login">
<a href="https://stackoverflow.com/users/signup?ssrc=site_switcher&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f14293869%2fwhat-is-the-pythonic-way-to-loop-through-two-arrays-at-the-same-time" class="login-link js-gps-track" data-gps-track="site_switcher.click({ item_type:10 })">Sign up</a> or <a href="https://stackoverflow.com/users/login?ssrc=site_switcher&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f14293869%2fwhat-is-the-pythonic-way-to-loop-through-two-arrays-at-the-same-time" class="login-link js-gps-track" data-gps-track="site_switcher.click({ item_type:11 })">log in</a> to customize your list.                </div>
        </div>

        <div class="header">
            <h3><a href="https://stackexchange.com/sites">more stack exchange communities</a>
            </h3>
            <a href="https://stackoverflow.blog" class="float-right">company blog</a>
        </div>
        <div class="modal-content">
                <div class="child-content"></div>
        </div>        
    </div>

        </li>
    
            <li role="none"><button class="s-topbar--item s-btn s-btn__icon s-btn__muted d-none sm:d-inline-flex js-searchbar-trigger" role="menuitem" aria-label="Поиск" aria-haspopup="true" aria-controls="search" title="Нажмите, чтобы показать поиск"><svg aria-hidden="true" class="svg-icon iconSearch" width="18" height="18" viewBox="0 0 18 18"><path d="m18 16.5-5.14-5.18h-.35a7 7 0 1 0-1.19 1.19v.35L16.5 18zM12 7A5 5 0 1 1 2 7a5 5 0 0 1 10 0"></path></svg></button></li>
                        <li role="none">
                            <a href="https://stackoverflow.com/users/login?ssrc=head&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f14293869%2fwhat-is-the-pythonic-way-to-loop-through-two-arrays-at-the-same-time" class="s-topbar--item s-topbar--item__unset s-btn s-btn__outlined ws-nowrap js-gps-track" role="menuitem" rel="nofollow" data-gps-track="login.click" data-ga="[&quot;top navigation&quot;,&quot;login button click&quot;,null,null,null]"><ya-tr-span data-index="13-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Log in" data-translation="Вход" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Вход</ya-tr-span></a>
                        </li>
                        <li role="none"><a href="https://stackoverflow.com/users/signup?ssrc=head&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f14293869%2fwhat-is-the-pythonic-way-to-loop-through-two-arrays-at-the-same-time" class="s-topbar--item s-topbar--item__unset ml4 s-btn s-btn__filled ws-nowrap js-signup-button js-gps-track" role="menuitem" rel="nofollow" data-gps-track="signup.topbar.click" data-ga="[&quot;sign up&quot;,&quot;Sign Up Navigation&quot;,&quot;Header&quot;,null,null]"><ya-tr-span data-index="14-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Sign up" data-translation="Регистрация" data-ch="1" data-type="trSpan" style="visibility: inherit !important;">Регистрация</ya-tr-span></a></li>
    </ol>
</nav>


	</div>
</header>

	<script>
		StackExchange.ready(function () { StackExchange.topbar.init(); });
		StackExchange.scrollPadding.setPaddingTop(50, 10); 
	</script>





    <div class="container">
                


    <div id="homepage-wizard-container"><div class=""><aside class="s-modal" role="dialog" aria-hidden="true" aria-labelledby="signup-modal-title" aria-describedby="signup-modal-description"><div class="s-modal--dialog pt32 pr32 pb32 ws4 overflow-visible" role="document"><h1 id="signup-modal-title" class="s-modal--header"><div slot="header" class="d-flex fd-column g8"><span class="flex--item fs-title fw-bold"><ya-tr-span data-index="15-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Let's set up your homepage" data-translation="Давайте настроим вашу домашнюю страницу" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Давайте настроим вашу домашнюю страницу</ya-tr-span></span> <span class="flex--item fs-body2"><ya-tr-span data-index="15-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Select a few topics you're interested in:" data-translation="Выберите несколько интересующих вас тем:" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Выберите несколько интересующих вас тем:</ya-tr-span></span></div></h1> <div id="signup-modal-description" class="s-modal--body"><div slot="body" class="d-flex fd-column g8" data-testid="tag-step-body"><div id="popular-tags" class="mb8 mln8"><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="python " data-translation="python " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">python </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="javascript " data-translation="javascript " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">javascript </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="c# " data-translation="c# " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">c# </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="reactjs " data-translation="reactjs " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">reactjs </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="java " data-translation="java " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">java </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="android " data-translation="android " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">android </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="html " data-translation="html " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">html </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="flutter " data-translation="flutter " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">flutter </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="c++ " data-translation="c++ " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">c++ </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="node.js " data-translation="node.js " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">node.js </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="typescript " data-translation="typescript " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">typescript </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="css " data-translation="css " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">css </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="r " data-translation="r " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">r </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="php " data-translation="php " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">php </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="angular " data-translation="angular " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">angular </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="next.js " data-translation="next.js " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">next.js </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="spring-boot " data-translation="spring-boot " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">spring-boot </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="machine-learning " data-translation="машинное обучение " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">машинное обучение </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="sql " data-translation="sql " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">sql </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="excel " data-translation="excel " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">excel </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="ios " data-translation="ios " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">ios </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="azure " data-translation="azure " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">azure </ya-tr-span></button><button class="m8 s-tag s-tag__md post-tag c-pointer h:bg-black-200"><ya-tr-span data-index="16-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="docker " data-translation="docker " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">docker </ya-tr-span></button></div> <div class="d-flex fd-column g8 ps-relative"><span class="flex--item fs-body2"><ya-tr-span data-index="17-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Or search from our full list:" data-translation="Или выполните поиск по нашему полному списку:" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Или выполните поиск по нашему полному списку:</ya-tr-span></span> <div role="combobox" tabindex="0" aria-expanded="false" aria-controls="search-popover-popover"><span><div id="text-input-container" class="d-flex fd-column gy4"> <div class="d-flex"> <div class="d-flex ps-relative w100 s-input fw-wrap py4"><div class="s-input-icon svelte-12r9hfl s-input-icon__search"><svg aria-hidden="true" class="svg-icon iconSearch" width="18" height="18" viewBox="0 0 18 18"><path d="m18 16.5-5.14-5.18h-.35a7 7 0 1 0-1.19 1.19v.35L16.5 18zM12 7A5 5 0 1 1 2 7a5 5 0 0 1 10 0"></path></svg></div> <span class="chips d-flex gx8 fw-wrap as-start flex__fl-equal svelte-12r9hfl"> <input id="filterInput" aria-invalid="false" class="s-input bc-transparent bs-none p0 h100 fl-grow1 w-auto py4 s-input__search svelte-12r9hfl" type="search" placeholder="Поиск" role="search" aria-label="Теги"></span> </div></div> </div></span></div> <div id="search-popover-popover" class="s-popover wmx-initial" role="dialog" aria-hidden="true" data-popper-placement="top" style="position: absolute; left: 206.667px; top: 382.042px;"><div class="s-popover--arrow" style="left: 210.5px;"></div> <div class="s-popover--content p12 mn12"><div class="ps-relative"><ul class="s-menu hmx1 overflow-x-hidden" role="menu"><li role="menuitem" class="h:bg-black-150"><button class="s-block-link bg-black-150">javascript</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">python</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">java</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">c#</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">php</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">android</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">html</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jquery</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">c++</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">css</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ios</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sql</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">mysql</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">r</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">reactjs</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">node.js</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">arrays</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">c</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">asp.net</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">json</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">python-3.x</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">.net</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ruby-on-rails</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sql-server</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">swift</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">django</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">angular</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">objective-c</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">excel</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">pandas</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">angularjs</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">regex</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">typescript</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ruby</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">linux</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ajax</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">iphone</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">vba</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">xml</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">laravel</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">spring</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">asp.net-mvc</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">database</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">wordpress</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">string</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">flutter</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">postgresql</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">mongodb</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">wpf</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">windows</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">amazon-web-services</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">xcode</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">bash</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">git</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">oracle-database</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">spring-boot</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">dataframe</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">firebase</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">azure</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">list</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">multithreading</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">vb.net</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">docker</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">react-native</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">eclipse</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">algorithm</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">powershell</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">macos</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">visual-studio</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">numpy</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">image</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">forms</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">scala</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">function</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">vue.js</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">twitter-bootstrap</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">performance</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">selenium</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">winforms</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">kotlin</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">loops</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">express</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">dart</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">hibernate</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sqlite</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">matlab</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">python-2.7</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">shell</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">rest</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">apache</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">api</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">entity-framework</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">android-studio</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">csv</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">maven</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">linq</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">qt</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">dictionary</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">unit-testing</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">facebook</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">asp.net-core</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">tensorflow</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">apache-spark</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">file</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">swing</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">class</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">unity-game-engine</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sorting</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">date</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">authentication</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">symfony</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">go</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">opencv</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">t-sql</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">.htaccess</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">matplotlib</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">google-chrome</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">for-loop</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">datetime</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">codeigniter</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">http</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">perl</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">validation</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sockets</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">google-maps</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">object</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">uitableview</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">xaml</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">oop</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">if-statement</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">visual-studio-code</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">cordova</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ubuntu</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">web-services</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">email</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">android-layout</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">github</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">elasticsearch</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">spring-mvc</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">kubernetes</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">selenium-webdriver</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ms-access</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">user-interface</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">parsing</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ggplot2</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">pointers</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">c++11</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">machine-learning</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">security</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">google-sheets</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">flask</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ruby-on-rails-3</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">nginx</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">google-apps-script</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">templates</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">variables</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">exception</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sql-server-2008</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">gradle</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">debugging</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">tkinter</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">listview</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">delphi</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jpa</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">asynchronous</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">pdf</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">web-scraping</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jsp</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">haskell</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ssl</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">amazon-s3</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">google-cloud-platform</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jenkins</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">xamarin</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">testing</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">wcf</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">npm</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">batch-file</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">generics</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ionic-framework</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">network-programming</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">unix</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">recursion</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">google-app-engine</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">mongoose</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">visual-studio-2010</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">.net-core</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">android-fragments</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">assembly</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">animation</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">math</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">session</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">hadoop</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">next.js</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">svg</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">intellij-idea</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">curl</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">django-models</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">join</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">laravel-5</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">url</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">heroku</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">winapi</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">http-redirect</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">tomcat</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">rust</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">google-cloud-firestore</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">web</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">inheritance</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">webpack</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">keras</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">image-processing</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">asp.net-mvc-4</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">gcc</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">logging</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">dom</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">matrix</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">pyspark</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">actionscript-3</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">swiftui</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">button</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">post</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">firebase-realtime-database</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">optimization</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jquery-ui</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">cocoa</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">iis</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">xpath</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">d3.js</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">firefox</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">internet-explorer</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">javafx</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">xslt</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">caching</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">select</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">asp.net-mvc-3</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">opengl</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">events</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">asp.net-web-api</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">plot</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">dplyr</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">magento</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">encryption</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">search</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">stored-procedures</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">amazon-ec2</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ruby-on-rails-4</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">memory</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">audio</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">canvas</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">multidimensional-array</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jsf</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">random</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">redux</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">cookies</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">vector</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">facebook-graph-api</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">input</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">flash</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">xamarin.forms</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">arraylist</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">indexing</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ipad</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">cocoa-touch</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">data-structures</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">video</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">model-view-controller</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">apache-kafka</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">serialization</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jdbc</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">woocommerce</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">routes</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">razor</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">awk</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">servlets</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">mod-rewrite</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">azure-devops</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">beautifulsoup</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">iframe</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">docker-compose</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">filter</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">excel-formula</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">aws-lambda</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">design-patterns</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">django-rest-framework</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">text</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">visual-c++</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">cakephp</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">mobile</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">android-intent</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">react-hooks</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">struct</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">methods</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">groovy</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">mvvm</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ssh</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">lambda</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">checkbox</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ecmascript-6</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">google-chrome-extension</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">time</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">grails</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">installation</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sharepoint</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">shiny</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">spring-security</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">cmake</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jakarta-ee</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">android-recyclerview</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">core-data</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">plsql</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">meteor</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">types</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">android-activity</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sed</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">bootstrap-4</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">websocket</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">activerecord</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">graph</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">replace</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">scikit-learn</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">file-upload</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">group-by</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">vim</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">junit</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">boost</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">deep-learning</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">import</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sass</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">memory-management</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">error-handling</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">async-await</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">eloquent</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">dynamic</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">soap</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">silverlight</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">charts</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">dependency-injection</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">layout</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">apache-spark-sql</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">deployment</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">browser</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">gridview</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">svn</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">while-loop</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">google-bigquery</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">vuejs2</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ffmpeg</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">dll</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">highcharts</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">view</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">foreach</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">c#-4.0</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">plugins</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">makefile</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">redis</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">reporting-services</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jupyter-notebook</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">server</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">merge</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">https</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">unicode</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">reflection</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">google-maps-api-3</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">twitter</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">extjs</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">oauth-2.0</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">axios</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">pytorch</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">terminal</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">split</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">pip</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">mysqli</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">cmd</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">django-views</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">encoding</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">netbeans</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">database-design</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">collections</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">hash</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">automation</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ember.js</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">data-binding</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">build</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">tcp</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">pdo</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sqlalchemy</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">apache-flex</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">command-line</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">printing</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">spring-data-jpa</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">entity-framework-core</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">concurrency</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">java-8</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">react-redux</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jestjs</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">service</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">html-table</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">neo4j</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ansible</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">lua</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">parameters</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">material-ui</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">visual-studio-2012</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">module</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">enums</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">promise</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">flexbox</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">outlook</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">webview</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">firebase-authentication</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">web-applications</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">uwp</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jquery-mobile</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">utf-8</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">datatable</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">python-requests</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">drop-down-menu</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">scroll</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">colors</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">parallel-processing</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">hive</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">tfs</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">scipy</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">count</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">syntax</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ms-word</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">twitter-bootstrap-3</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ssis</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">google-analytics</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">fonts</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">three.js</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">graphql</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">constructor</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">file-io</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">rxjs</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">paypal</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">powerbi</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">discord</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">cassandra</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">socket.io</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">graphics</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">gwt</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">compiler-errors</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">nlp</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">react-router</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">solr</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">backbone.js</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">url-rewriting</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">datatables</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">memory-leaks</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">datagridview</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">oauth</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">oracle11g</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">drupal</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">zend-framework</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">neural-network</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">terraform</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">knockout.js</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">django-forms</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">interface</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">triggers</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">google-api</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">casting</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">angular-material</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">linked-list</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jmeter</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">proxy</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">path</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">timer</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">django-templates</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">directory</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">orm</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">parse-platform</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">visual-studio-2015</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">arduino</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">cron</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">windows-phone-7</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">push-notification</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">conditional-statements</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">primefaces</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">functional-programming</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">pagination</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">model</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jar</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">xamarin.android</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">hyperlink</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">uiview</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">visual-studio-2013</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">vbscript</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">gitlab</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">google-cloud-functions</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">azure-active-directory</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">download</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jwt</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">swift3</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sql-server-2005</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">process</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">rspec</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">configuration</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">properties</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">callback</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">pygame</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">combobox</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">windows-phone-8</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">safari</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">permissions</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">linux-kernel</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">scrapy</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">raspberry-pi</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">scripting</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">emacs</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">clojure</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">scope</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">io</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">x86</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">mongodb-query</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">compilation</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">angularjs-directive</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">nhibernate</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">responsive-design</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">request</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">bluetooth</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">3d</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">dns</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">binding</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">reference</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">discord.js</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">architecture</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">playframework</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">version-control</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">pyqt</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">doctrine-orm</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">expo</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">azure-functions</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">pycharm</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">package</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">get</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sql-server-2012</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">rubygems</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">f#</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">autocomplete</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">datepicker</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">openssl</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">kendo-ui</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">tree</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jackson</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">controller</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">yii</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">xamarin.ios</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">grep</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">nested</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">static</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">statistics</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">datagrid</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">dockerfile</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">active-directory</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">null</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">transactions</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">uiviewcontroller</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">phpmyadmin</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">webforms</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">discord.py</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">notifications</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sas</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">computer-vision</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">duplicates</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">youtube</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">mocking</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">nullpointerexception</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">menu</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">yaml</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">bitmap</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sum</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">asp.net-mvc-5</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">visual-studio-2008</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">electron</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jsf-2</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">yii2</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">time-series</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">android-listview</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">stl</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">css-selectors</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">stream</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">floating-point</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ant</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">cryptography</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">hashmap</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">character-encoding</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">blazor</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sdk</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">msbuild</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">google-drive-api</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">selenium-chromedriver</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jboss</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">asp.net-core-mvc</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">frontend</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">joomla</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">devise</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">anaconda</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">navigation</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">cors</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">background</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">camera</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">binary</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">pyqt5</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">multiprocessing</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">linq-to-sql</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">cuda</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">iterator</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">onclick</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ios7</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">mariadb</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">plotly</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">rabbitmq</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">android-asynctask</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">laravel-4</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">tabs</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">insert</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">uicollectionview</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">amazon-dynamodb</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">environment-variables</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">microsoft-graph-api</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">linker</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">android-jetpack-compose</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">console</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">xsd</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">coldfusion</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">upload</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ftp</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">continuous-integration</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">textview</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">opengl-es</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">operating-system</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">localization</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">xml-parsing</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">mockito</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">formatting</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">macros</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">kivy</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">json.net</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">vuejs3</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">type-conversion</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">data.table</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">timestamp</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">calendar</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">integer</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">segmentation-fault</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">android-ndk</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">drag-and-drop</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">prolog</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">char</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">crash</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jasmine</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">automated-tests</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">dependencies</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">geometry</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">android-gradle-plugin</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">itext</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">header</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">firebase-cloud-messaging</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sprite-kit</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">mfc</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">fortran</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">nosql</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">attributes</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">nuxt.js</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">format</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">nestjs</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jquery-plugins</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">odoo</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">db2</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jenkins-pipeline</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">leaflet</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">event-handling</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">flutter-layout</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">azure-pipelines</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">postman</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">annotations</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">julia</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">keyboard</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">textbox</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">arm</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">visual-studio-2017</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">gulp</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">libgdx</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">xampp</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">synchronization</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">crystal-reports</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">stripe-payments</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">dom-events</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">timezone</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">azure-web-app-service</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">android-emulator</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sequelize.js</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">swagger</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">wso2</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">uikit</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">uiscrollview</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">aggregation-framework</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">namespaces</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jvm</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">chart.js</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">com</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">webdriver</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">geolocation</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">centos</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">subprocess</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">google-sheets-formula</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">widget</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">html5-canvas</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">dialog</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">garbage-collection</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">numbers</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">concatenation</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sql-update</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">qml</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">mapreduce</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">windows-10</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">set</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ionic2</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">smtp</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">tuples</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">snowflake-cloud-data-platform</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">modal-dialog</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">rotation</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">android-edittext</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">http-headers</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">spring-data</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">radio-button</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">doctrine</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">nuget</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">grid</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">java-stream</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sonarqube</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">lucene</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">xmlhttprequest</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">internationalization</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">listbox</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">components</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">switch-statement</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">initialization</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">apache-camel</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">google-play</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">boolean</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">serial-port</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ldap</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ios5</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">youtube-api</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">return</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">eclipse-plugin</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">pivot</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">latex</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">gdb</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">frameworks</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">tags</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">containers</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">dataset</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">asp-classic</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">foreign-keys</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">subquery</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">label</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">uinavigationcontroller</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">copy</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">google-cloud-storage</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">delegates</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">github-actions</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">struts2</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">migration</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">base64</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">protractor</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">c++17</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">sql-server-2008-r2</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">queue</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">find</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">uibutton</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">arguments</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">append</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">composer-php</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">embedded</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jaxb</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">zip</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">stack</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">cucumber</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">autolayout</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ide</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">popup</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">entity-framework-6</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">iteration</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">windows-7</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">r-markdown</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">vb6</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">gmail</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">ssl-certificate</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">airflow</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">jqgrid</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">hover</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">passwords</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">android-viewpager</button> </li><li role="menuitem" class="h:bg-black-150"><button class="s-block-link">udp</button> </li></ul></div></div></div></div></div></div> <div class="d-flex g8 s-modal--footer"><div slot="footer" class="w100 ta-center"><button class="s-btn w100 mb16 s-btn__filled" disabled="" data-testid="next-button"><ya-tr-span data-index="18-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Next" data-translation="Далее" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Далее</ya-tr-span></button> <span class="fc-black-400 fs-caption px16"><ya-tr-span data-index="18-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="You’ll be prompted to create an account to view your personalized homepage." data-translation="вам будет предложено создать учетную запись для просмотра вашей персонализированной домашней страницы." data-ch="0" data-type="trSpan" style="visibility: inherit !important;">вам будет предложено создать учетную запись для просмотра вашей персонализированной домашней страницы.</ya-tr-span></span></div></div> <button class="s-btn s-modal--close s-btn__muted s-btn__icon" aria-label="Закрыть"><div class="modal-close"><ya-tr-span data-index="19-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="X" data-translation="X" data-ch="1" data-type="trSpan" style="visibility: inherit !important;">X</ya-tr-span></div></button></div></aside></div></div>
<script type="application/json" data-role="module-args" data-module-name="islands/homepage-wizard/index.mod">{"ContainerElementId":"homepage-wizard-container","FKey":"d75a38c9f46387c074e42866b21fab101776168769fc53229633006b67a9d8d5","Tags":["javascript","python","java","c#","php","android","html","jquery","c++","css","ios","sql","mysql","r","reactjs","node.js","arrays","c","asp.net","json","python-3.x",".net","ruby-on-rails","sql-server","swift","django","angular","objective-c","excel","pandas","angularjs","regex","typescript","ruby","linux","ajax","iphone","vba","xml","laravel","spring","asp.net-mvc","database","wordpress","string","flutter","postgresql","mongodb","wpf","windows","amazon-web-services","xcode","bash","git","oracle-database","spring-boot","dataframe","firebase","azure","list","multithreading","vb.net","docker","react-native","eclipse","algorithm","powershell","macos","visual-studio","numpy","image","forms","scala","function","vue.js","twitter-bootstrap","performance","selenium","winforms","kotlin","loops","express","dart","hibernate","sqlite","matlab","python-2.7","shell","rest","apache","api","entity-framework","android-studio","csv","maven","linq","qt","dictionary","unit-testing","facebook","asp.net-core","tensorflow","apache-spark","file","swing","class","unity-game-engine","sorting","date","authentication","symfony","go","opencv","t-sql",".htaccess","matplotlib","google-chrome","for-loop","datetime","codeigniter","http","perl","validation","sockets","google-maps","object","uitableview","xaml","oop","if-statement","visual-studio-code","cordova","ubuntu","web-services","email","android-layout","github","elasticsearch","spring-mvc","kubernetes","selenium-webdriver","ms-access","user-interface","parsing","ggplot2","pointers","c++11","machine-learning","security","google-sheets","flask","ruby-on-rails-3","nginx","google-apps-script","templates","variables","exception","sql-server-2008","gradle","debugging","tkinter","listview","delphi","jpa","asynchronous","pdf","web-scraping","jsp","haskell","ssl","amazon-s3","google-cloud-platform","jenkins","xamarin","testing","wcf","npm","batch-file","generics","ionic-framework","network-programming","unix","recursion","google-app-engine","mongoose","visual-studio-2010",".net-core","android-fragments","assembly","animation","math","session","hadoop","next.js","svg","intellij-idea","curl","django-models","join","laravel-5","url","heroku","winapi","http-redirect","tomcat","rust","google-cloud-firestore","web","inheritance","webpack","keras","image-processing","asp.net-mvc-4","gcc","logging","dom","matrix","pyspark","actionscript-3","swiftui","button","post","firebase-realtime-database","optimization","jquery-ui","cocoa","iis","xpath","d3.js","firefox","internet-explorer","javafx","xslt","caching","select","asp.net-mvc-3","opengl","events","asp.net-web-api","plot","dplyr","magento","encryption","search","stored-procedures","amazon-ec2","ruby-on-rails-4","memory","audio","canvas","multidimensional-array","jsf","random","redux","cookies","vector","facebook-graph-api","input","flash","xamarin.forms","arraylist","indexing","ipad","cocoa-touch","data-structures","video","model-view-controller","apache-kafka","serialization","jdbc","woocommerce","routes","razor","awk","servlets","mod-rewrite","azure-devops","beautifulsoup","iframe","docker-compose","filter","excel-formula","aws-lambda","design-patterns","django-rest-framework","text","visual-c++","cakephp","mobile","android-intent","react-hooks","struct","methods","groovy","mvvm","ssh","lambda","checkbox","ecmascript-6","google-chrome-extension","time","grails","installation","sharepoint","shiny","spring-security","cmake","jakarta-ee","android-recyclerview","core-data","plsql","meteor","types","android-activity","sed","bootstrap-4","websocket","activerecord","graph","replace","scikit-learn","file-upload","group-by","vim","junit","boost","deep-learning","import","sass","memory-management","error-handling","async-await","eloquent","dynamic","soap","silverlight","charts","dependency-injection","layout","apache-spark-sql","deployment","browser","gridview","svn","while-loop","google-bigquery","vuejs2","ffmpeg","dll","highcharts","view","foreach","c#-4.0","plugins","makefile","redis","reporting-services","jupyter-notebook","server","merge","https","unicode","reflection","google-maps-api-3","twitter","extjs","oauth-2.0","axios","pytorch","terminal","split","pip","mysqli","cmd","django-views","encoding","netbeans","database-design","collections","hash","automation","ember.js","data-binding","build","tcp","pdo","sqlalchemy","apache-flex","command-line","printing","spring-data-jpa","entity-framework-core","concurrency","java-8","react-redux","jestjs","service","html-table","neo4j","ansible","lua","parameters","material-ui","visual-studio-2012","module","enums","promise","flexbox","outlook","webview","firebase-authentication","web-applications","uwp","jquery-mobile","utf-8","datatable","python-requests","drop-down-menu","scroll","colors","parallel-processing","hive","tfs","scipy","count","syntax","ms-word","twitter-bootstrap-3","ssis","google-analytics","fonts","three.js","graphql","constructor","file-io","rxjs","paypal","powerbi","discord","cassandra","socket.io","graphics","gwt","compiler-errors","nlp","react-router","solr","backbone.js","url-rewriting","datatables","memory-leaks","datagridview","oauth","oracle11g","drupal","zend-framework","neural-network","terraform","knockout.js","django-forms","interface","triggers","google-api","casting","angular-material","linked-list","jmeter","proxy","path","timer","django-templates","directory","orm","parse-platform","visual-studio-2015","arduino","cron","windows-phone-7","push-notification","conditional-statements","primefaces","functional-programming","pagination","model","jar","xamarin.android","hyperlink","uiview","visual-studio-2013","vbscript","gitlab","google-cloud-functions","azure-active-directory","download","jwt","swift3","sql-server-2005","process","rspec","configuration","properties","callback","pygame","combobox","windows-phone-8","safari","permissions","linux-kernel","scrapy","raspberry-pi","scripting","emacs","clojure","scope","io","x86","mongodb-query","compilation","angularjs-directive","nhibernate","responsive-design","request","bluetooth","3d","dns","binding","reference","discord.js","architecture","playframework","version-control","pyqt","doctrine-orm","expo","azure-functions","pycharm","package","get","sql-server-2012","rubygems","f#","autocomplete","datepicker","openssl","kendo-ui","tree","jackson","controller","yii","xamarin.ios","grep","nested","static","statistics","datagrid","dockerfile","active-directory","null","transactions","uiviewcontroller","phpmyadmin","webforms","discord.py","notifications","sas","computer-vision","duplicates","youtube","mocking","nullpointerexception","menu","yaml","bitmap","sum","asp.net-mvc-5","visual-studio-2008","electron","jsf-2","yii2","time-series","android-listview","stl","css-selectors","stream","floating-point","ant","cryptography","hashmap","character-encoding","blazor","sdk","msbuild","google-drive-api","selenium-chromedriver","jboss","asp.net-core-mvc","frontend","joomla","devise","anaconda","navigation","cors","background","camera","binary","pyqt5","multiprocessing","linq-to-sql","cuda","iterator","onclick","ios7","mariadb","plotly","rabbitmq","android-asynctask","laravel-4","tabs","insert","uicollectionview","amazon-dynamodb","environment-variables","microsoft-graph-api","linker","android-jetpack-compose","console","xsd","coldfusion","upload","ftp","continuous-integration","textview","opengl-es","operating-system","localization","xml-parsing","mockito","formatting","macros","kivy","json.net","vuejs3","type-conversion","data.table","timestamp","calendar","integer","segmentation-fault","android-ndk","drag-and-drop","prolog","char","crash","jasmine","automated-tests","dependencies","geometry","android-gradle-plugin","itext","header","firebase-cloud-messaging","sprite-kit","mfc","fortran","nosql","attributes","nuxt.js","format","nestjs","jquery-plugins","odoo","db2","jenkins-pipeline","leaflet","event-handling","flutter-layout","azure-pipelines","postman","annotations","julia","keyboard","textbox","arm","visual-studio-2017","gulp","libgdx","xampp","synchronization","crystal-reports","stripe-payments","dom-events","timezone","azure-web-app-service","android-emulator","sequelize.js","swagger","wso2","uikit","uiscrollview","aggregation-framework","namespaces","jvm","chart.js","com","webdriver","geolocation","centos","subprocess","google-sheets-formula","widget","html5-canvas","dialog","garbage-collection","numbers","concatenation","sql-update","qml","mapreduce","windows-10","set","ionic2","smtp","tuples","snowflake-cloud-data-platform","modal-dialog","rotation","android-edittext","http-headers","spring-data","radio-button","doctrine","nuget","grid","java-stream","sonarqube","lucene","xmlhttprequest","internationalization","listbox","components","switch-statement","initialization","apache-camel","google-play","boolean","serial-port","ldap","ios5","youtube-api","return","eclipse-plugin","pivot","latex","gdb","frameworks","tags","containers","dataset","asp-classic","foreign-keys","subquery","label","uinavigationcontroller","copy","google-cloud-storage","delegates","github-actions","struts2","migration","base64","protractor","c++17","sql-server-2008-r2","queue","find","uibutton","arguments","append","composer-php","embedded","jaxb","zip","stack","cucumber","autolayout","ide","popup","entity-framework-6","iteration","windows-7","r-markdown","vb6","gmail","ssl-certificate","airflow","jqgrid","hover","passwords","android-viewpager","udp"],"TriggerEvent":"homepageWizardShow","OauthInPopup":true,"ReturnUrl":"https://stackoverflow.com","ReturnUrlForPopup":"https://stackoverflow.com/users/after-signup/oauth-only"}</script><script defer="" src="https://cdn.sstatic.net/Js/webpack-chunks/svelte.en.js?v=150134e89426"></script><script defer="" src="https://cdn.sstatic.net/Js/webpack-chunks/stacks-svelte.en.js?v=72feec5d5528"></script><script defer="" src="https://cdn.sstatic.net/Js/webpack-chunks/3397.en.js?v=ecde4075784a"></script><script defer="" src="https://cdn.sstatic.net/Js/webpack-chunks/1315.en.js?v=d971ebf7a8e2"></script><script defer="" src="https://cdn.sstatic.net/Js/webpack-chunks/7224.en.js?v=8ca862d5f302"></script><script defer="" src="https://cdn.sstatic.net/Js/webpack-chunks/4537.en.js?v=e6769247457b"></script><script defer="" src="https://cdn.sstatic.net/Js/islands/homepage-wizard.en.js?v=e1f9f3c67beb"></script>
<div id="left-sidebar" data-is-here-when="md lg" class="left-sidebar js-pinned-left-sidebar ps-relative">
    <div class="left-sidebar--sticky-container js-sticky-leftnav">
        <nav aria-label="Первичный">
            <ol class="nav-links">
                <li>
                    <ol class="nav-links">
                        

<li class="ps-relative" aria-current="false">


    <a href="/" class="s-block-link pl8 js-homepage-wizard-link js-gps-track nav-links--link -link__with-icon" data-gps-track="top_nav.click({is_current: false, location:2, destination:8,  has_activity_notification:False});home_nav.click({location:2})" aria-controls="" data-controller=" " data-s-popover-placement="right" aria-current="false" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
        <div class="d-flex ai-center">
<svg aria-hidden="true" class="svg-icon iconHome" width="18" height="18" viewBox="0 0 18 18"><path d="M15 10v5a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-5H0l9-9 9 9zm-8 1v6h4v-6z"></path></svg>                <span class="-link--channel-name pl6"><ya-tr-span data-index="20-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Home" data-translation="Главная" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Главная</ya-tr-span></span>

        </div>
    </a>
</li>



                        

<li class="ps-relative  youarehere" aria-current="true">


    <a id="nav-questions" href="/questions" class="s-block-link pl8 js-gps-track nav-links--link -link__with-icon" data-gps-track="top_nav.click({is_current: true, location:2, destination:1,  has_activity_notification:False})" aria-controls="" data-controller=" " data-s-popover-placement="right" aria-current="false" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
        <div class="d-flex ai-center">
<svg aria-hidden="true" class="svg-icon iconQuestion" width="18" height="18" viewBox="0 0 18 18"><path d="m4 15-3 3V4c0-1.1.9-2 2-2h12c1.09 0 2 .91 2 2v9c0 1.09-.91 2-2 2zm7.75-3.97c.72-.83.98-1.86.98-2.94 0-1.65-.7-3.22-2.3-3.83a4.4 4.4 0 0 0-3.02 0 3.8 3.8 0 0 0-2.32 3.83q0 1.93 1.03 3a3.8 3.8 0 0 0 2.85 1.07q.94 0 1.71-.34.97.66 1.06.7.34.2.7.3l.59-1.13a5 5 0 0 1-1.28-.66m-1.27-.9a5 5 0 0 0-1.5-.8l-.45.9q.5.18.98.5-.3.1-.65.11-.92 0-1.52-.68c-.86-1-.86-3.12 0-4.11.8-.9 2.35-.9 3.15 0 .9 1.01.86 3.03-.01 4.08"></path></svg>                <span class="-link--channel-name pl6"><ya-tr-span data-index="21-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Questions" data-translation="Вопросы" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Вопросы</ya-tr-span></span>

        </div>
    </a>
</li>






                        

<li class="ps-relative" aria-current="false">


    <a href="/tags" class="s-block-link pl8 js-gps-track nav-links--link -link__with-icon" data-gps-track="top_nav.click({is_current: false, location:2, destination:2,  has_activity_notification:False})" aria-controls="" data-controller=" " data-s-popover-placement="right" aria-current="false" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
        <div class="d-flex ai-center">
<svg aria-hidden="true" class="svg-icon iconTags" width="18" height="18" viewBox="0 0 18 18"><path d="M9.24 1a3 3 0 0 0-2.12.88l-5.7 5.7a2 2 0 0 0-.38 2.31 3 3 0 0 1 .67-1.01l6-6A3 3 0 0 1 9.83 2H14a3 3 0 0 1 .79.1A2 2 0 0 0 13 1z" opacity=".4"></path><path d="M9.83 3a2 2 0 0 0-1.42.59l-6 6a2 2 0 0 0 0 2.82L6.6 16.6a2 2 0 0 0 2.82 0l6-6A2 2 0 0 0 16 9.17V5a2 2 0 0 0-2-2zM12 9a2 2 0 1 1 0-4 2 2 0 0 1 0 4"></path></svg>                <span class="-link--channel-name pl6"><ya-tr-span data-index="22-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Tags" data-translation="Теги" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Теги</ya-tr-span></span>

        </div>
    </a>
</li>


                        
                        <li class="pb24"></li>


                        

<li class="ps-relative" aria-current="false">


    <a id="nav-users" href="/users" class="s-block-link pl8 js-gps-track nav-links--link -link__with-icon" data-gps-track="top_nav.click({is_current: false, location:2, destination:3,  has_activity_notification:False})" aria-controls="" data-controller=" " data-s-popover-placement="right" aria-current="false" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
        <div class="d-flex ai-center">
<svg aria-hidden="true" class="svg-icon iconPeople" width="18" height="18" viewBox="0 0 18 18"><path d="M17 14c0 .44-.45 1-1 1H9a1 1 0 0 1-1-1H2c-.54 0-1-.56-1-1 0-2.63 3-4 3-4s.23-.4 0-1c-.84-.62-1.06-.59-1-3s1.37-3 2.5-3 2.44.58 2.5 3-.16 2.38-1 3c-.23.59 0 1 0 1s1.55.71 2.42 2.09c.78-.72 1.58-1.1 1.58-1.1s.23-.4 0-1c-.84-.61-1.06-.58-1-3s1.37-3 2.5-3 2.44.59 2.5 3c.05 2.42-.16 2.39-1 3-.23.6 0 1 0 1s3 1.38 3 4"></path></svg>                <span class="-link--channel-name pl6"><ya-tr-span data-index="23-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Users" data-translation="Пользователи" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Пользователи</ya-tr-span></span>

        </div>
    </a>
</li>


                            

<li class="ps-relative" aria-current="false">


    <a id="nav-companies" href="https://stackoverflow.com/jobs/companies?so_medium=stackoverflow&amp;so_source=SiteNav" class="s-block-link pl8 js-gps-track nav-links--link -link__with-icon" data-gps-track="top_nav.click({is_current: false, location:2, destination:12,  has_activity_notification:False})" aria-controls="" data-controller=" " data-s-popover-placement="right" aria-current="false" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
        <div class="d-flex ai-center">
<svg aria-hidden="true" class="svg-icon iconIndustry" width="18" height="18" viewBox="0 0 18 18"><path d="M10 16v-4H8v4H2V4c0-1.1.9-2 2-2h6c1.09 0 2 .91 2 2v2h2c1.09 0 2 .91 2 2v8zM4 4v2h2V4zm0 4v2h2V8zm4-4v2h2V4zm0 4v2h2V8zm-4 4v2h2v-2zm8 0v2h2v-2zm0-4v2h2V8z"></path></svg>                <span class="-link--channel-name pl6"><ya-tr-span data-index="24-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Companies" data-translation="Компании" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Компании</ya-tr-span></span>

        </div>
    </a>
</li>




        <li class="ml8 mt32 mb8">
            <a href="javascript:void(0)" class="s-link s-link d-flex fl-grow1 fc-black-400 h:fc-black-600 fs-fine" role="button" aria-controls="popover-labs-left-nav" data-controller="s-popover" data-action="s-popover#toggle" data-s-popover-placement="top" data-s-popover-toggle-class="is-selected" aria-expanded="false">
                <div class="flex--item fl-grow1 tt-uppercase fc-black-600 fw-bold"><ya-tr-span data-index="25-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Labs" data-translation="Лаборатории" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Лаборатории</ya-tr-span></div>
                <div class="flex--item px12">
                    <svg aria-hidden="true" class="svg-icon iconInfoSm" width="14" height="14" viewBox="0 0 14 14"><path d="M7 1a6 6 0 1 1 0 12A6 6 0 0 1 7 1m1 10V6H6v5zm0-6V3H6v2z"></path></svg>
                </div>
            </a>
        </li>
        

<li class="ps-relative" aria-current="false">


    <a id="nav-labs-jobs" href="/jobs?source=so-left-nav" class="s-block-link pl8 ai-center js-disable-jobs-new-link js-gps-track nav-links--link -link__with-icon" data-gps-track="top_nav.click({is_current: false, location:2, destination:26,  has_activity_notification:False});jobs.click({destination:JobsFakeDoor, is_registered:False, rep_bucket:new, origin:Stack Overflow})" aria-controls="" data-controller=" " data-s-popover-placement="right" aria-current="false" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
        <div class="d-flex ai-center">
<svg aria-hidden="true" class="svg-icon iconBriefcase" width="18" height="18" viewBox="0 0 18 18"><path d="M5 4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v1h1a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V7c0-1.1.9-2 2-2h1zm7 0H6v1h6z"></path></svg>                <span class="-link--channel-name pl6"><ya-tr-span data-index="26-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Jobs" data-translation="Вакансии" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Вакансии</ya-tr-span></span>

        </div>
    </a>
</li>


                

<li class="ps-relative" aria-current="false">


    <a id="nav-labs-discussions" href="/beta/discussions" class="s-block-link pl8 ai-center js-gps-track nav-links--link -link__with-icon" data-gps-track="top_nav.click({is_current: false, location:2, destination:24,  has_activity_notification:False})" aria-controls="" data-controller=" " data-s-popover-placement="right" aria-current="false" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
        <div class="d-flex ai-center">
<svg aria-hidden="true" class="w16 svg-icon iconMessage" width="18" height="18" viewBox="0 0 18 18"><path d="M5 7a1 1 0 0 1 1-1h6a1 1 0 1 1 0 2H6a1 1 0 0 1-1-1m1 2a1 1 0 1 0 0 2h4a1 1 0 1 0 0-2zm-5 9V4c0-1.1.9-2 2-2h12c1.09 0 2 .91 2 2v9c0 1.09-.91 2-2 2H4.5zm2.76-5h11.23v-.01H15V4H3v9.65z"></path></svg>                <span class="-link--channel-name pl6"><ya-tr-span data-index="27-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Discussions" data-translation="Обсуждения" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Обсуждения</ya-tr-span></span>

        </div>
    </a>
</li>



                            <li class="ml8 mt32 mb4">
                                <div class="d-flex jc-space-between ai-center">
                                    <a class="s-link d-flex fl-grow1 fc-black-400 h:fc-black-600 fs-fine" href="javascript:void(0)" role="button" aria-controls="popover-discover-collectives" data-controller="s-popover" data-action="s-popover#toggle" data-s-popover-placement="top" data-s-popover-toggle-class="is-selected" data-gps-track="top_nav.click({is_current:false, location:2, destination:17})" aria-expanded="false">
                                        <div class="flex--item fl-grow1 tt-uppercase fc-black-600 fw-bold"><ya-tr-span data-index="28-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Collectives" data-translation="Коллективы" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Коллективы</ya-tr-span></div>
                                        <div class="flex--item px12 js-collectives-navcta-toggle">
                                            <svg aria-hidden="true" class="svg-icon iconPlusSm" width="14" height="14" viewBox="0 0 14 14"><path d="M8 2H6v4H2v2h4v4h2V8h4V6H8z"></path></svg>
                                        </div>
                                    </a>
                                </div>

                            </li>
                                <li class="ps-relative js-collectives-navcta-toggle">
                                    <p class="fs-fine pr8 pl8 pt4 fc-black-400"><ya-tr-span data-index="29-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Communities for your favorite technologies. " data-translation=" Сообщества для ваших любимых технологий. " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Сообщества для ваших любимых технологий. </ya-tr-span><a href="/collectives-all" class="s-link s-link__grayscale s-link__underlined fw-bold"><ya-tr-span data-index="29-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Explore all Collectives" data-translation="Исследуйте все коллективы" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Исследуйте все коллективы</ya-tr-span></a>
                                    </p>
                                </li>

                        
                    </ol>
                </li>
                
                

        

<li class="js-freemium-cta ps-relative mt32 mb8">


    <div class="fs-fine tt-uppercase fc-black-600 fw-bold ml8 mt16 mb8"><ya-tr-span data-index="30-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Teams" data-translation="Команды" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Команды</ya-tr-span></div>

    <div class="px12 pt12 pb4 mb12 fc-medium overflow-hidden">        
        <img class="wmx100 mx-auto mb12 h-auto d-block" width="151" height="24" src="https://cdn.sstatic.net/Img/teams/teams-promo.svg?v=e507948b81bf" alt="">
        <p class="fs-fine"><ya-tr-span data-index="31-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Ask questions, find answers and collaborate at work with Stack Overflow for Teams. " data-translation=" Задавайте вопросы, находите ответы и сотрудничайте на работе с помощью Stack Overflow для Teams. " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Задавайте вопросы, находите ответы и сотрудничайте на работе с помощью Stack Overflow для Teams.  </ya-tr-span></p>
        <a href="https://stackoverflowteams.com/teams/create/free/?utm_medium=referral&amp;utm_source=stackoverflow-community&amp;utm_campaign=side-bar&amp;utm_content=explore-teams" class="w100 s-btn s-btn__filled s-btn__xs bg-orange-400 h:bg-orange-500 js-gps-track pt8 pr7 pb6 pl7" data-gps-track="teams.create.left-sidenav.click({ Action: 6 })" data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav free cta&quot;,&quot;stackoverflow.com/teams/create/free&quot;,null,null]"><ya-tr-span data-index="32-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Try Teams for free" data-translation="Играйте в команды бесплатно" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Играйте в команды бесплатно</ya-tr-span></a>
        <a href="https://stackoverflow.co/teams/?utm_medium=referral&amp;utm_source=stackoverflow-community&amp;utm_campaign=side-bar&amp;utm_content=explore-teams" class="w100 s-btn s-btn__muted s-btn__xs mt1 js-gps-track" data-gps-track="teams.create.left-sidenav.click({ Action: 5 })" data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav free cta&quot;,&quot;stackoverflow.com/teams&quot;,null,null]"><ya-tr-span data-index="32-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Explore Teams" data-translation="Изучайте команды" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Изучайте команды</ya-tr-span></a>
    </div>
</li>


    <li class="d-flex ai-center jc-space-between ml8 mt32 mb8 js-create-team-cta d-none">

        <a href="javascript:void(0)" class="s-link d-flex fl-grow1 fc-black-400 h:fc-black-600 fs-fine js-gps-track" role="button" aria-controls="popover-teams-create-cta" data-controller="s-popover" data-action="s-popover#toggle" data-s-popover-placement="bottom-start" data-s-popover-toggle-class="is-selected" data-gps-track="teams.create.left-sidenav.click({ Action: ShowInfo })" data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav show teams info&quot;,null,null,null]" aria-expanded="false">
            <div class="flex--item fl-grow1 fc-black-600 fw-bold tt-uppercase">Teams</div>
            <div class="flex--item px12">
                <svg aria-hidden="true" class="svg-icon iconPlusSm" width="14" height="14" viewBox="0 0 14 14"><path d="M8 2H6v4H2v2h4v4h2V8h4V6H8z"></path></svg>
            </div>
        </a>
    </li>
    <li class="ps-relative js-create-team-cta d-none">
        <p class="fs-fine pr8 pl8 pb4 fc-black-400">
            Ask questions, find answers and collaborate at work with Stack Overflow for Teams.
            <a href="https://stackoverflow.co/teams/?utm_medium=referral&amp;utm_source=stackoverflow-community&amp;utm_campaign=side-bar&amp;utm_content=explore-teams-compact" class="s-link s-link__grayscale s-link__underlined fw-bold">Explore Teams</a>
        </p>
    </li> 

            </ol>
        </nav>
    </div>


        <div class="s-popover ws2" id="popover-discover-collectives" role="menu">
            <div class="s-popover--arrow"></div>
            <div>
                <svg aria-hidden="true" class="fc-orange-400 float-right ml24 svg-spot spotCollective" width="48" height="48" viewBox="0 0 48 48"><path d="M25.5 7a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5M14 18.25c0-.69.56-1.25 1.25-1.25h22.5c.69 0 1.25.56 1.25 1.25V37.5a1 1 0 0 1-1.6.8l-4.07-3.05a1.3 1.3 0 0 0-.75-.25H15.25c-.69 0-1.25-.56-1.25-1.25zM7 24.5a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0M25.5 48a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5M48 24.5a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0" opacity=".2"></path><path d="M21 3.5a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0M24.5 2a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3M0 23.5a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0M3.5 22a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3M21 44.5a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0m3.5-1.5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3m20-23a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7M43 23.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0m-23.23-3.14a1 1 0 0 1-.13 1.4l-2.08 1.74 2.08 1.73a1 1 0 1 1-1.28 1.54l-2.42-2.02a1.63 1.63 0 0 1 0-2.5l2.42-2.02a1 1 0 0 1 1.4.13m7.6 1.41a1 1 0 1 1 1.28-1.54l2.42 2.02c.78.65.78 1.85 0 2.5l-2.42 2.02a1 1 0 1 1-1.28-1.54l2.08-1.73zM24.12 18a1 1 0 0 1 .87 1.12l-1 8a1 1 0 1 1-1.98-.24l1-8a1 1 0 0 1 1.11-.87M12.25 13C11.01 13 10 14 10 15.25v15.5c0 1.24 1 2.25 2.25 2.25h17.33q.09 0 .15.05l4.07 3.05a2 2 0 0 0 3.2-1.6V15.25c0-1.24-1-2.25-2.25-2.25zM12 15.25q.02-.23.25-.25h22.5q.23.02.25.25V34.5l-4.07-3.05q-.6-.45-1.35-.45H12.25a.25.25 0 0 1-.25-.25zm7.24-10.68a1 1 0 1 0-.48-1.94A22 22 0 0 0 2.91 17.7a1 1 0 1 0 1.92.58 20 20 0 0 1 14.4-13.72m11.06-1.65a1 1 0 0 0-.58 1.92c6.45 1.92 11.54 7 13.46 13.46a1 1 0 1 0 1.92-.58 22 22 0 0 0-14.8-14.8M4.57 28.76a1 1 0 0 0-1.94.48 22 22 0 0 0 16.13 16.13 1 1 0 1 0 .48-1.94A20 20 0 0 1 4.57 28.76m40.8.48a1 1 0 1 0-1.94-.48 20 20 0 0 1-13.72 14.41 1 1 0 0 0 .58 1.92 22 22 0 0 0 15.08-15.85"></path></svg>
                <h5 class="pt4 fw-bold">Collectives™ on Stack Overflow</h5>
                <p class="my16 fs-caption fc-black-500">Find centralized, trusted content and collaborate around the technologies you use most.</p>
                <a href="/collectives" class="js-gps-track s-btn s-btn__filled s-btn__xs" data-gps-track="top_nav.click({is_current:false, location:2, destination:18})">
                    Learn more about Collectives
                </a>
            </div>
        </div>

        <div class="s-popover ws2" id="popover-teams-create-cta" role="menu" aria-hidden="true">
            <div class="s-popover--arrow"></div>

            <div class="ps-relative overflow-hidden">
                <p class="mb2"><strong>Teams</strong></p>
                <p class="mb12 fs-caption fc-black-400">Q&amp;A for work</p>
                <p class="mb12 fs-caption fc-black-500">Connect and share knowledge within a single location that is structured and easy to search.</p>
                <a href="https://stackoverflow.co/teams/" class="js-gps-track s-btn s-btn__filled s-btn__xs" data-gps-track="teams.create.left-sidenav.click({ Action: CtaClick })" data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav cta&quot;,&quot;stackoverflow.com/teams&quot;,null,null]">
                    Learn more about Teams
                </a>
            </div>

            <div class="ps-absolute t8 r8">
                <svg aria-hidden="true" class="fc-orange-400 svg-spot spotPeople" width="48" height="48" viewBox="0 0 48 48"><path d="M13.5 28a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9M7 30a1 1 0 0 1 1-1h11a1 1 0 0 1 1 1v5h11v-5a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v10a2 2 0 0 1-2 2H33v5a1 1 0 0 1-1 1H20a1 1 0 0 1-1-1v-5H8a1 1 0 0 1-1-1zm25-6.5a4.5 4.5 0 1 0 9 0 4.5 4.5 0 0 0-9 0M24.5 34a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9" opacity=".2"></path><path d="M16.4 26.08A6 6 0 1 0 7.53 26C5.64 26.06 4 27.52 4 29.45V40a1 1 0 0 0 1 1h9a1 1 0 1 0 0-2h-4v-7a1 1 0 1 0-2 0v7H6v-9.55c0-.73.67-1.45 1.64-1.45H16a1 1 0 0 0 .4-1.92M12 18a4 4 0 1 1 0 8 4 4 0 0 1 0-8m16.47 14a6 6 0 1 0-8.94 0A3.6 3.6 0 0 0 16 35.5V46a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V35.5c0-1.94-1.64-3.42-3.53-3.5M20 28a4 4 0 1 1 8 0 4 4 0 0 1-8 0m-.3 6h8.6c1 0 1.7.75 1.7 1.5V45h-2v-7a1 1 0 1 0-2 0v7h-4v-7a1 1 0 1 0-2 0v7h-2v-9.5c0-.75.7-1.5 1.7-1.5M42 22c0 1.54-.58 2.94-1.53 4A3.5 3.5 0 0 1 44 29.45V40a1 1 0 0 1-1 1h-9a1 1 0 1 1 0-2h4v-7a1 1 0 1 1 2 0v7h2v-9.55A1.5 1.5 0 0 0 40.48 28H32a1 1 0 0 1-.4-1.92A6 6 0 1 1 42 22m-2 0a4 4 0 1 0-8 0 4 4 0 0 0 8 0"></path><g opacity=".35"><path d="M17 10a1 1 0 011-1h12a1 1 0 110 2H18a1 1 0 01-1-1m1-5a1 1 0 100 2h12a1 1 0 100-2zM14 1a1 1 0 00-1 1v12a1 1 0 001 1h5.09l4.2 4.2a1 1 0 001.46-.04l3.7-4.16H34a1 1 0 001-1V2a1 1 0 00-1-1zm1 12V3h18v10h-5a1 1 0 00-.75.34l-3.3 3.7-3.74-3.75a1 1 0 00-.71-.29z"></path></g></svg>
            </div>
        </div>

        <div class="s-popover ws2" id="popover-labs-left-nav" role="menu" aria-hidden="true">
            <div class="s-popover--arrow"></div>
            <svg aria-hidden="true" class="fc-black-600 mb8 svg-icon iconLabsAltSm" width="42" height="18" viewBox="0 0 42 18"><path fill="var(--black-600)" d="M11.5 13.62c0 .21-.17.38-.37.38H5.36a.37.37 0 0 1-.37-.38V4.38c0-.21.17-.38.37-.38h1.26c.2 0 .37.17.37.38v7.6h4.14c.2 0 .37.18.37.38zm9.43.22a.4.4 0 0 1-.3.16h-1.5q-.25-.01-.36-.25l-.55-1.7h-3.1l-.56 1.7a.4.4 0 0 1-.35.25h-1.5a.38.38 0 0 1-.35-.5l3.39-9.25c.05-.15.2-.25.35-.25h1.13q.26.01.36.25l3.39 9.24q.06.19-.05.35m-4.16-7.39-1.21 3.53h2.26zm13.34 5.71a.37.37 0 0 0 0 .53A4.5 4.5 0 0 0 33.59 14c1.02 0 1.92-.27 2.58-.79a2.8 2.8 0 0 0 1.07-2.25c0-.86-.27-1.62-.87-2.15-.46-.4-1-.63-1.89-.76l-1.04-.16a2 2 0 0 1-.83-.33q-.22-.19-.22-.57 0-.46.3-.73c.2-.18.53-.32 1-.32.7 0 1.25.15 1.72.6.14.14.37.14.52 0l.88-.87a.37.37 0 0 0-.01-.53A4.2 4.2 0 0 0 33.72 4c-1.01 0-1.87.3-2.48.84a3 3 0 0 0-.93 2.2q-.02 1.24.78 2.01.72.66 1.93.83l1.07.15c.5.07.65.15.8.29q.23.2.24.67-.01.5-.35.73-.34.29-1.16.3c-.87 0-1.49-.19-2.07-.76a.37.37 0 0 0-.52 0zM22.37 14a.37.37 0 0 1-.37-.38V4.38c0-.21.17-.38.37-.38h3.54q1.4 0 2.26.78c.56.52.86 1.26.86 2.13 0 .84-.37 1.52-.87 1.95A2.6 2.6 0 0 1 29.17 11q0 1.42-.9 2.23c-.56.51-1.34.76-2.22.76zm3.54-1.98c.96 0 .96-1 .96-1s0-1.02-.96-1.02H24v2.02zm-.11-4.06c1.07 0 1.07-1.02 1.07-1.02s0-1.01-1.07-1.01H24v2.03zM0 4v10a4 4 0 0 0 4 4h34a4 4 0 0 0 4-4V4a4 4 0 0 0-4-4H4a4 4 0 0 0-4 4m4-2h34a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V4c0-1.1.9-2 2-2"></path></svg>
            <p class="fs-caption">Get early access and see previews of new features.</p>
            <a class="s-btn s-btn__filled s-btn__xs s-btn__icon fs-fine" href="https://stackoverflow.co/labs/"><svg aria-hidden="true" class="svg-icon iconShareSm" width="14" height="14" viewBox="0 0 14 14"><path d="M5 1H3a2 2 0 0 0-2 2v8c0 1.1.9 2 2 2h8a2 2 0 0 0 2-2V9h-2v2H3V3h2zm2 0h6v6h-2V4.5L6.5 9 5 7.5 9.5 3H7z"></path></svg> Learn more about Labs</a>
        </div>



</div>



        <div id="content" class="snippet-hidden">

            

<div itemprop="mainEntity" itemscope="" itemtype="https://schema.org/Question">
    <link itemprop="image" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a">

    <div class="inner-content clearfix">
        

            <div id="question-header" class="d-flex sm:fd-column">
                        <h1 itemprop="name" class="fs-headline1 ow-break-word mb8 flex--item fl1"><a href="/questions/14293869/what-is-the-pythonic-way-to-loop-through-two-arrays-at-the-same-time" class="question-hyperlink">What is the pythonic way to loop through two arrays at the same time?</a></h1>

                <div class="ml12 aside-cta flex--item sm:ml0 sm:mb12 sm:order-first d-flex jc-end">

                        <div class="ml12 aside-cta flex--item print:d-none">
                                <a href="/questions/ask" class="ws-nowrap s-btn s-btn__filled">
        Ask Question
    </a>

                        </div>
                </div>
            </div>
            <div class="d-flex fw-wrap pb8 mb16 bb bc-black-200">
                    <div class="flex--item ws-nowrap mr16 mb8" title="2013-01-12 13:40:54Z">
                        <span class="fc-black-400 mr2">Asked</span>
                        <time itemprop="dateCreated" datetime="2013-01-12T13:40:54">11 years, 11 months ago</time>
                    </div>
                    <div class="flex--item ws-nowrap mr16 mb8">
                        <span class="fc-black-400 mr2">Modified</span>
                        <a href="?lastactivity" class="s-link s-link__inherit" title="2024-01-10 15:30:23Z">11 months ago</a>
                    </div>
                    <div class="flex--item ws-nowrap mb8" title="Viewed 69,421 times">
                        <span class="fc-black-400 mr2">Viewed</span>
                        69k times
                    </div>
            </div>



            <div id="mainbar" role="main" aria-label="вопросы и ответы">
                
<div class="question js-question" data-questionid="14293869" data-position-on-page="0" data-score="48" id="question">
    <style>
    </style>
<div class="js-zone-container zone-container-main">
    <div id="dfp-tlb" class="everyonelovesstackoverflow everyoneloves__top-leaderboard everyoneloves__leaderboard"></div>
		<div class="js-report-ad-button-container " style="width: 728px"></div>
</div>

    <div class="post-layout ">
        <div class="votecell post-layout--left">
            

<div class="js-voting-container d-flex jc-center fd-column ai-center gs4 fc-black-300" data-post-id="14293869" data-referrer="None">
        <button class="js-vote-up-btn flex--item s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Up vote" data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100" data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200" aria-describedby="--stacks-s-tooltip-xdb4pydm">
            <svg aria-hidden="true" class="svg-icon iconArrowUp" width="18" height="18" viewBox="0 0 18 18"><path d="M1 12h16L9 4z"></path></svg>
        </button><div id="--stacks-s-tooltip-xdb4pydm" class="s-popover s-popover__tooltip" role="tooltip">This question shows research effort; it is useful and clear<div class="s-popover--arrow"></div></div>
        <input type="hidden" id="voteUpHash" value="70:3:31e,16:5ac00db905453e42,10:1734895760,16:8aceb25279dcabe1,8:14293869,860268df729da16b0261a7e2b02cba5d7d608d53935607a003689e779fb483a8">
        <div class="js-vote-count flex--item d-flex fd-column ai-center fc-theme-body-font fw-bold fs-subheading py4" itemprop="upvoteCount" data-value="48">
48        </div>
        <button class="js-vote-down-btn js-vote-down-question flex--item mb8 s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200" title="This question does not show any research effort; it is unclear or not useful" aria-pressed="false" aria-label="Down vote" data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100" data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200">
            <svg aria-hidden="true" class="svg-icon iconArrowDown" width="18" height="18" viewBox="0 0 18 18"><path d="M1 6h16l-8 8z"></path></svg>
        </button>
        <input type="hidden" id="voteDownHash" value="70:3:31e,16:56c952dc75052cab,10:1734895760,16:979721f554bd54d6,8:14293869,6836ab0f64d808def660305a8f5b912edbb60ac728a57c79383f2becf1da2586">


        
<button class="js-saves-btn s-btn s-btn__unset c-pointer py4" type="button" id="saves-btn-14293869" data-controller="s-tooltip" data-s-tooltip-placement="right" data-s-popover-placement="" data-is-saved="false" aria-label="Save" data-post-id="14293869" data-post-type-id="1" data-user-privilege-for-post-click="0" aria-controls="" data-s-popover-auto-show="false" aria-describedby="--stacks-s-tooltip-xg207710">
    <svg aria-hidden="true" class="fc-theme-primary-400 js-saves-btn-selected d-none svg-icon iconBookmark" width="18" height="18" viewBox="0 0 18 18"><path d="M3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4z"></path></svg>
    <svg aria-hidden="true" class="js-saves-btn-unselected svg-icon iconBookmarkAlt" width="18" height="18" viewBox="0 0 18 18"><path d="m9 10.6 4 2.66V3H5v10.26zM3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4z"></path></svg>
</button><div id="--stacks-s-tooltip-xg207710" class="s-popover s-popover__tooltip" role="tooltip">Save this question.<div class="s-popover--arrow"></div></div>








    
    <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/14293869/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-label="Timeline" aria-describedby="--stacks-s-tooltip-7fo0ap2w"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18" viewBox="0 0 19 18"><path d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10z"></path></svg></a><div id="--stacks-s-tooltip-7fo0ap2w" class="s-popover s-popover__tooltip" role="tooltip">Show activity on this post.<div class="s-popover--arrow"></div></div>

</div>

        </div>

        

<div class="postcell post-layout--right">
    
    <div class="s-prose js-post-body" itemprop="text">
                
<p>If I have two arrays, of the same length - say <code>a</code> and <code>b</code></p>

<p><code>a = [4,6,2,6,7,3,6,7,2,5]</code></p>

<p><code>b = [6,4,6,3,2,7,8,5,3,5]</code></p>

<p>normally, I would do this like so:</p>

<pre class="lang-py s-code-block"><code data-highlighted="yes" class="hljs language-python"><span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">range</span>(<span class="hljs-built_in">len</span>(a)):
    <span class="hljs-built_in">print</span> a[i] + b[i]
</code></pre>

<p>rather than something like this:</p>

<pre class="lang-py s-code-block"><code data-highlighted="yes" class="hljs language-python">i=<span class="hljs-number">0</span>
<span class="hljs-keyword">for</span> number <span class="hljs-keyword">in</span> a:
    <span class="hljs-built_in">print</span> number + b[i]
    i += <span class="hljs-number">1</span>
</code></pre>

<p><ya-tr-span data-index="33-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="because I prefer to be consistent with methods used." data-translation="потому что я предпочитаю быть последовательным в отношении используемых методов." data-ch="0" data-type="trSpan" style="visibility: inherit !important;">потому что я предпочитаю быть последовательным в отношении используемых методов.</ya-tr-span></p>

<p><ya-tr-span data-index="34-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="I know of " data-translation="Я знаю о " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Я знаю о </ya-tr-span><code>zip</code><ya-tr-span data-index="34-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=", but I never use it. " data-translation=", но никогда им не пользовался. " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">, но никогда им не пользовался. </ya-tr-span><ya-tr-span data-index="34-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Is this what " data-translation="Для этого ли " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Для этого ли </ya-tr-span><code>zip</code><ya-tr-span data-index="34-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" was made for?" data-translation=" был создан?" data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> был создан?</ya-tr-span></p>

<p><ya-tr-span data-index="35-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="would " data-translation="бы " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">бы </ya-tr-span></p>

<pre class="lang-py s-code-block"><code data-highlighted="yes" class="hljs language-python"><span class="hljs-keyword">for</span> pair <span class="hljs-keyword">in</span> <span class="hljs-built_in">zip</span>(a,b):
    <span class="hljs-built_in">print</span> pair[<span class="hljs-number">0</span>] + pair[<span class="hljs-number">1</span>]
</code></pre>

<p><ya-tr-span data-index="36-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="be the " data-translation="быть " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">быть </ya-tr-span><em><ya-tr-span data-index="36-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="pythonic" data-translation="питоническим" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">питоническим</ya-tr-span></em><ya-tr-span data-index="36-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" way to do this?" data-translation=" способом сделать это?" data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> способом сделать это?</ya-tr-span></p>
    </div>

        <div class="mt24 mb12">
            <div class="post-taglist d-flex gs4 gsy fd-column">
                <div class="d-flex ps-relative fw-wrap">
                    
                    <ul class="ml0 list-ls-none js-post-tag-list-wrapper d-inline"><li class="d-inline mr4 js-post-tag-list-item"><a href="/questions/tagged/python" class="s-tag post-tag js-gps-track" title="показывать вопросы с тегом &quot;python&quot;" aria-label="показывать вопросы с тегом &quot;python&quot;" rel="tag" aria-labelledby="tag-python-tooltip-container" data-tag-menu-origin="Unknown"><ya-tr-span data-index="37-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="python" data-translation="питон" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">питон</ya-tr-span></a></li></ul>
                </div>
            </div>
        </div>

    <div class="mb0 ">
        <div class="mt16 d-flex gs8 gsy fw-wrap jc-end ai-start pt4 mb16">
            <div class="flex--item mr16 fl1 w96">
                


<div class="js-post-menu pt2" data-post-id="14293869" data-post-type-id="1">

    <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">

        <div class="flex--item">
            <a href="/q/14293869" rel="nofollow" itemprop="url" class="js-share-link js-gps-track" title="Короткая постоянная ссылка на этот вопрос" data-gps-track="post.click({ item: 2, priv: 0, post_type: 1 })" data-controller="se-share-sheet s-popover" data-se-share-sheet-title="Share a link to this question" data-se-share-sheet-subtitle="" data-se-share-sheet-post-type="question" data-se-share-sheet-social="facebook twitter devto" data-se-share-sheet-location="1" data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f3.0%2f" data-se-share-sheet-license-name="CC BY-SA 3.0" data-s-popover-placement="bottom-start" aria-controls="se-share-sheet-0" data-action=" s-popover#toggle se-share-sheet#preventNavigation s-popover:show->se-share-sheet#willShow s-popover:shown->se-share-sheet#didShow" aria-expanded="false"><ya-tr-span data-index="38-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Share" data-translation="Поделиться" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Поделиться</ya-tr-span></a><div class="s-popover z-dropdown s-anchors s-anchors__default" style="width: unset; max-width: 28em;" id="se-share-sheet-0"><div class="s-popover--arrow"></div><div><label for="share-sheet-input-se-share-sheet-0"><span class="js-title fw-bold">Share a link to this question</span> <span class="js-subtitle"></span></label></div><div class="my8"><input type="text" id="share-sheet-input-se-share-sheet-0" class="js-input s-input wmn3 sm:wmn-initial bc-black-300 bg-white fc-black-600" readonly=""></div><div class="d-flex jc-space-between ai-center mbn4"><button class="js-copy-link-btn s-btn s-btn__link js-gps-track" data-gps-track="">Copy link</button><a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="license" class="js-license s-block-link w-auto" target="_blank" title="The current license for this post: CC BY-SA 3.0">CC BY-SA 3.0</a><div class="js-social-container d-none"></div></div></div>
        </div>


                    <div class="flex--item">
                        <a href="/posts/14293869/edit" class="js-suggest-edit-post js-gps-track" data-gps-track="post.click({ item: 6, priv: 0, post_type: 1 })" title=""><ya-tr-span data-index="39-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Improve this question" data-translation="Улучшите этот вопрос" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Улучшите этот вопрос</ya-tr-span></a>
                    </div>

                <div class="flex--item">
                    <button type="button" id="btnFollowPost-14293869" class="s-btn s-btn__link js-follow-post js-follow-question js-gps-track" data-gps-track="post.click({ item: 14, priv: 0, post_type: 1 })" data-controller="s-tooltip " data-s-tooltip-placement="bottom" data-s-popover-placement="bottom" aria-controls="" aria-describedby="--stacks-s-tooltip-w9s4geqz"><ya-tr-span data-index="40-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Follow " data-translation=" Подписаться " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Подписаться  </ya-tr-span><input type="hidden" id="voteFollowHash" value="70:3:31e,16:3c90edf56a2e92af,10:1734895760,16:531967c64d56ec7c,8:14293869,78f3877ac66aa85a539e31374ef590e40e4eb4a241941de4f702e506e543c3f4">
                    </button><div id="--stacks-s-tooltip-w9s4geqz" class="s-popover s-popover__tooltip" role="tooltip">Follow this question to receive notifications<div class="s-popover--arrow"></div></div>
                </div>






    </div>
    <div class="js-menu-popup-container"></div>
</div>
            </div>

                <div class="post-signature flex--item">
<div class="user-info user-hover ">
    <div class="d-flex ">
        <div class="user-action-time fl-grow1">
            <a href="/posts/14293869/revisions" title="показать все правки в этом посте" class="js-gps-track" data-gps-track="post.click({ item: 4, priv: 0, post_type: 1 })"><ya-tr-span data-index="41-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="edited " data-translation="отредактировано " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">отредактировано </ya-tr-span><span title="2013-01-12 15:24:21Z" class="relativetime"><ya-tr-span data-index="41-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Jan 12, 2013 at 15:24" data-translation="12 января 2013 года в 15:24" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">12 января 2013 года в 15:24</ya-tr-span></span></a>
        </div>
        
    </div>
    <div class="user-gravatar32">
        <a href="/users/383124/phant0m"><div class="gravatar-wrapper-32"><img src="https://www.gravatar.com/avatar/bbe4e19d2e5cb62b356ef503e2577efd?s=64&amp;d=identicon&amp;r=PG" alt="аватар пользователя phant0m" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details">
        <a href="/users/383124/phant0m"><ya-tr-span data-index="42-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="phant0m" data-translation="phant0m" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">phant0m</ya-tr-span></a>
        <div class="-flair">
            <span class="reputation-score" title="оценка репутации 16,885" dir="ltr"><ya-tr-span data-index="43-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="16.9k" data-translation="16,9 тыс." data-ch="0" data-type="trSpan" style="visibility: inherit !important;">16,9 тыс.</ya-tr-span></span><span title="6 золотых значков" aria-hidden="true"><span class="badge1"></span><span class="badgecount"><ya-tr-span data-index="43-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="6" data-translation="6" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">6</ya-tr-span></span></span><span class="v-visible-sr"><ya-tr-span data-index="43-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="6 gold badges" data-translation="6 золотых значков" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">6 золотых значков</ya-tr-span></span><span title="51 серебряный значок" aria-hidden="true"><span class="badge2"></span><span class="badgecount"><ya-tr-span data-index="43-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="51" data-translation="51" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">51</ya-tr-span></span></span><span class="v-visible-sr"><ya-tr-span data-index="43-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="51 silver badges" data-translation="51 серебряный значок" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">51 серебряный значок</ya-tr-span></span><span title="84 бронзовых значка" aria-hidden="true"><span class="badge3"></span><span class="badgecount"><ya-tr-span data-index="43-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="84" data-translation="84" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">84</ya-tr-span></span></span><span class="v-visible-sr"><ya-tr-span data-index="43-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="84 bronze badges" data-translation="84 бронзовых значка" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">84 бронзовых значка</ya-tr-span></span>
        </div>
    </div>
</div>
                </div>
            <div class="post-signature owner flex--item">
                <div class="user-info user-hover ">
    <div class="d-flex ">
        <div class="user-action-time fl-grow1"><ya-tr-span data-index="44-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" asked " data-translation=" спросил " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  спросил </ya-tr-span><span title="2013-01-12 13:40:54Z" class="relativetime"><ya-tr-span data-index="44-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Jan 12, 2013 at 13:40" data-translation="12 января 2013 года в 13:40" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">12 января 2013 года в 13:40</ya-tr-span></span>
        </div>
        
    </div>
    <div class="user-gravatar32">
        <a href="/users/432913/will"><div class="gravatar-wrapper-32"><img src="https://www.gravatar.com/avatar/2fe7355b33d1b0bd79b1224691b00841?s=64&amp;d=identicon&amp;r=PG" alt="аватар пользователя уилла" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope="" itemtype="http://schema.org/Person">
        <a href="/users/432913/will"><ya-tr-span data-index="45-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="will" data-translation="будет" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">будет</ya-tr-span></a><span class="d-none" itemprop="name"><ya-tr-span data-index="45-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="will" data-translation="будет" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">будет</ya-tr-span></span>
        <div class="-flair">
            <span class="reputation-score" title="оценка репутации 10,600" dir="ltr"><ya-tr-span data-index="46-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="10.6k" data-translation="10,6 тыс." data-ch="0" data-type="trSpan" style="visibility: inherit !important;">10,6 тыс.</ya-tr-span></span><span title="7 золотых значков" aria-hidden="true"><span class="badge1"></span><span class="badgecount"><ya-tr-span data-index="46-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="7" data-translation="7" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">7</ya-tr-span></span></span><span class="v-visible-sr"><ya-tr-span data-index="46-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="7 gold badges" data-translation="7 золотых значков" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">7 золотых значков</ya-tr-span></span><span title="49 серебряных значков" aria-hidden="true"><span class="badge2"></span><span class="badgecount"><ya-tr-span data-index="46-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="49" data-translation="49" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">49</ya-tr-span></span></span><span class="v-visible-sr"><ya-tr-span data-index="46-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="49 silver badges" data-translation="49 серебряных значков" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">49 серебряных значков</ya-tr-span></span><span title="73 бронзовых значка" aria-hidden="true"><span class="badge3"></span><span class="badgecount"><ya-tr-span data-index="46-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="73" data-translation="73" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">73</ya-tr-span></span></span><span class="v-visible-sr"><ya-tr-span data-index="46-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="73 bronze badges" data-translation="73 бронзовых значка" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">73 бронзовых значка</ya-tr-span></span>
        </div>
    </div>
</div>


            </div>
        </div>
    </div>
    
</div>




            <span class="d-none" itemprop="commentCount"></span> 
    <div class="post-layout--right js-post-comments-component">
        <div id="comments-14293869" class="comments js-comments-container bt bc-black-200 mt12  dno" data-post-id="14293869" data-min-length="15">
            <ul class="comments-list js-comments-list" data-remaining-comments-count="0" data-canpost="false" data-cansee="true" data-comments-unavailable="false" data-addlink-disabled="true">

            </ul>
	    </div>

        <div id="comments-link-14293869" data-rep="50" data-anon="true">
                    <a class="js-add-link comments-link disabled-link" title="Используйте комментарии, чтобы запросить дополнительную информацию или предложить улучшения. Не отвечайте на вопросы в комментариях." href="#" role="button"><ya-tr-span data-index="47-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Add a comment" data-translation="Добавить комментарий" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Добавить комментарий</ya-tr-span></a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link dno" title="Разверните, чтобы показать все комментарии к этому сообщению" href="#" onclick="" role="button"></a>
        </div>         
    </div>
    </div>

</div>


<div class="js-zone-container zone-container-responsive">
    <div id="dfp-isb" class="everyonelovesstackoverflow everyoneloves__inline-sidebar mx-auto"></div>
		<div class="js-report-ad-button-container mx-auto" style="width: 300px"></div>
</div>

                
                <div id="answers">
                    <a name="tab-top"></a>
                    <div id="answers-header">
                        <div class="answers-subheader d-flex ai-center mb8">
                            <div class="flex--item fl1">
                                <h2 class="mb0" data-answercount="5"><ya-tr-span data-index="48-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" 5 Answers " data-translation=" 5 Ответов " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  5 Ответов </ya-tr-span><span style="display:none;" itemprop="answerCount"><ya-tr-span data-index="48-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="5" data-translation="5" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">5</ya-tr-span></span>
                                </h2>
                            </div>
                            <div class="flex--item">
                                

<div class="d-flex g4 gsx ai-center sm:fd-column sm:ai-start">
    <div class="d-flex fd-column ai-end sm:ai-start">
        <label class="flex--item fs-caption" for="answer-sort-dropdown-select-menu"><ya-tr-span data-index="49-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Sorted by: " data-translation=" Отсортировано по: " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> Отсортировано по: </ya-tr-span></label>
        <a class="js-sort-preference-change s-link flex--item fs-fine d-none" data-value="ScoreDesc" href="/questions/14293869/what-is-the-pythonic-way-to-loop-through-two-arrays-at-the-same-time?answertab=scoredesc#tab-top"><ya-tr-span data-index="49-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Reset to default " data-translation=" Сброшено значение по умолчанию " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> Сброшено значение по умолчанию </ya-tr-span></a>
    </div>
    <div class="flex--item s-select">
        <select id="answer-sort-dropdown-select-menu">
                    <option value="scoredesc" selected="selected">
                        Highest score (default)
                    </option>
                    <option value="trending">
                        Trending (recent votes count more)
                    </option>
                    <option value="modifieddesc">
                        Date modified (newest first)
                    </option>
                    <option value="createdasc">
                        Date created (oldest first)
                    </option>
        </select>
    </div>
</div>


                            </div>
                        </div>
                            

<div class="js-mfnes-container s-notice s-notice__info">
    <div class="d-flex jc-space-between ai-center">
        <div class="flex--item">
            <p class="js-mfnes-link fs-body2 m0"><ya-tr-span data-index="50-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Не нашли ответ? " data-translation=" Не нашли ответ? " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Не нашли ответ? </ya-tr-span><a href="https://ru.stackoverflow.com/questions/ask?utm=soenseru&amp;fromen=0da1b6d0472b1"><ya-tr-span data-index="50-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Задайте вопрос на Stack Overflow на русском." data-translation="Задайте вопрос на Stack Overflow на русском." data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Задайте вопрос на Stack Overflow на русском.</ya-tr-span></a>
            </p>
        </div>
        <div class="flex--item">
            <button class="js-mfnes-dismiss s-btn p0" type="button" aria-label="Уволить"><svg aria-hidden="true" class="svg-icon iconClearSm" width="14" height="14" viewBox="0 0 14 14"><path d="M12 3.41 10.59 2 7 5.59 3.41 2 2 3.41 5.59 7 2 10.59 3.41 12 7 8.41 10.59 12 12 10.59 8.41 7z"></path></svg></button>
        </div>
    </div>
</div>

<script>
    $(document)
        .ready(function () {
            var notification = $('.js-mfnes-container');
            notification.find('.js-mfnes-dismiss').on('click',
                function () {
                    notification.remove();
                    $.ajax("/mfnes/dismiss/14293869/ru/4");
                });
            notification.find('.js-mfnes-link a').on('click',
                function () {
                    $.ajax("/mfnes/click/14293869/ru/4");
                });
        });
</script>                    </div>


                                    
<a name="14293953"></a>
<div id="answer-14293953" class="answer js-answer accepted-answer js-accepted-answer" data-answerid="14293953" data-parentid="14293869" data-score="62" data-position-on-page="1" data-highest-scored="1" data-question-has-accepted-highest-score="1" itemprop="acceptedAnswer" itemscope="" itemtype="https://schema.org/Answer">
        <div class="post-layout">
            <div class="votecell post-layout--left">
                

<div class="js-voting-container d-flex jc-center fd-column ai-center gs4 fc-black-300" data-post-id="14293953" data-referrer="None">
        <button class="js-vote-up-btn flex--item s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Голосование &quot;За&quot;" data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100" data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200" aria-describedby="--stacks-s-tooltip-89slh803">
            <svg aria-hidden="true" class="svg-icon iconArrowUp" width="18" height="18" viewBox="0 0 18 18"><path d="M1 12h16L9 4z"></path></svg>
        </button><div id="--stacks-s-tooltip-89slh803" class="s-popover s-popover__tooltip" role="tooltip">This answer is useful<div class="s-popover--arrow"></div></div>
        <input type="hidden" id="voteUpHash" value="70:3:31e,16:d368d0d815430eae,10:1734895760,16:9a440eac9dc69b13,8:14293953,4222e2fde25d482d375e7808e6acfefe2ddc55a9bf89ae432b439a5e7179664e">
        <div class="js-vote-count flex--item d-flex fd-column ai-center fc-theme-body-font fw-bold fs-subheading py4" itemprop="upvoteCount" data-value="62">
62        </div>
        <button class="js-vote-down-btn flex--item mb8 s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200" title="Этот ответ бесполезен" aria-pressed="false" aria-label="Голосование против" data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100" data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200">
            <svg aria-hidden="true" class="svg-icon iconArrowDown" width="18" height="18" viewBox="0 0 18 18"><path d="M1 6h16l-8 8z"></path></svg>
        </button>
        <input type="hidden" id="voteDownHash" value="70:3:31e,16:f4e00131731804bb,10:1734895760,16:e2bbf094596b0cbf,8:14293953,ff58f843959a7064f330236188c2be2db46bc7007ab1a01e06f417c4107831e3">


        
<button class="js-saves-btn s-btn s-btn__unset c-pointer py4" type="button" id="saves-btn-14293953" data-controller="s-tooltip" data-s-tooltip-placement="right" data-s-popover-placement="" data-is-saved="false" aria-label="Сохранить" data-post-id="14293953" data-post-type-id="2" data-user-privilege-for-post-click="0" aria-controls="" data-s-popover-auto-show="false" aria-describedby="--stacks-s-tooltip-fmry5wns">
    <svg aria-hidden="true" class="fc-theme-primary-400 js-saves-btn-selected d-none svg-icon iconBookmark" width="18" height="18" viewBox="0 0 18 18"><path d="M3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4z"></path></svg>
    <svg aria-hidden="true" class="js-saves-btn-unselected svg-icon iconBookmarkAlt" width="18" height="18" viewBox="0 0 18 18"><path d="m9 10.6 4 2.66V3H5v10.26zM3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4z"></path></svg>
</button><div id="--stacks-s-tooltip-fmry5wns" class="s-popover s-popover__tooltip" role="tooltip">Save this answer.<div class="s-popover--arrow"></div></div>







            <div class="js-accepted-answer-indicator flex--item fc-green-400 py6 mtn8" data-s-tooltip-placement="right" title="Загрузка, когда этот ответ был принят…" tabindex="0" role="note" aria-label="Принято">
                <div class="ta-center">
                    <svg aria-hidden="true" class="svg-icon iconCheckmarkLg" width="36" height="36" viewBox="0 0 36 36"><path d="m6 14 8 8L30 6v8L14 30l-8-8z"></path></svg>
                </div>
            </div>

    
    <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/14293953/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-label="Временная шкала" aria-describedby="--stacks-s-tooltip-urvq4sv4"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18" viewBox="0 0 19 18"><path d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10z"></path></svg></a><div id="--stacks-s-tooltip-urvq4sv4" class="s-popover s-popover__tooltip" role="tooltip">Show activity on this post.<div class="s-popover--arrow"></div></div>

</div>

            </div>

            

<div class="answercell post-layout--right">
    
    <div class="s-prose js-post-body" itemprop="text">
<p><ya-tr-span data-index="51-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="If the lists " data-translation="Если списки " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Если списки </ya-tr-span><code>a</code><ya-tr-span data-index="51-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" and " data-translation=" и " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> и </ya-tr-span><code>b</code><ya-tr-span data-index="51-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" are short, use " data-translation=" короткие, используйте " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> короткие, используйте </ya-tr-span><a href="http://docs.python.org/2/library/functions.html#zip" rel="noreferrer"><ya-tr-span data-index="51-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="zip" data-translation="zip" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">zip</ya-tr-span></a><ya-tr-span data-index="51-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" (as @Vincenzo Pii showed):" data-translation=" (как показал @Vincenzo Pii):" data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> (как показал @Vincenzo Pii):</ya-tr-span></p>

<pre class="lang-py s-code-block"><code data-highlighted="yes" class="hljs language-python"><span class="hljs-keyword">for</span> x, y <span class="hljs-keyword">in</span> <span class="hljs-built_in">zip</span>(a, b):
    <span class="hljs-built_in">print</span>(x + y)
</code></pre>

<p><ya-tr-span data-index="52-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="If the lists " data-translation="Если списки " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Если списки </ya-tr-span><code>a</code><ya-tr-span data-index="52-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" and " data-translation=" и " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> и </ya-tr-span><code>b</code><ya-tr-span data-index="52-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" are long, then use " data-translation=" длинные, используйте " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> длинные, используйте </ya-tr-span><a href="http://docs.python.org/2/library/itertools.html#itertools.izip" rel="noreferrer"><ya-tr-span data-index="52-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="itertools.izip" data-translation="itertools.izip" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">itertools.izip</ya-tr-span></a><ya-tr-span data-index="52-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" to save memory:" data-translation=" для экономии памяти:" data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> для экономии памяти:</ya-tr-span></p>

<pre class="lang-py s-code-block"><code data-highlighted="yes" class="hljs language-python"><span class="hljs-keyword">import</span> itertools <span class="hljs-keyword">as</span> IT
<span class="hljs-keyword">for</span> x, y <span class="hljs-keyword">in</span> IT.izip(a, b):
    <span class="hljs-built_in">print</span>(x + y)
</code></pre>

<p><code>zip</code><ya-tr-span data-index="53-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" creates a list of tuples. " data-translation=" создаёт список кортежей. " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> создаёт список кортежей. </ya-tr-span><ya-tr-span data-index="53-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="This can be burdensome (memory-wise) if " data-translation="Это может быть обременительно (с точки зрения памяти), если " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Это может быть обременительно (с точки зрения памяти), если </ya-tr-span><code>a</code><ya-tr-span data-index="53-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" and " data-translation=" и " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> и </ya-tr-span><code>b</code><ya-tr-span data-index="53-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" are large." data-translation=" велики." data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> велики.</ya-tr-span></p>

<p><code>itertools.izip</code><ya-tr-span data-index="54-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" returns an iterator. " data-translation=" возвращает итератор. " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> возвращает итератор. </ya-tr-span><ya-tr-span data-index="54-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="The iterator does not generate the complete list of tuples; it only yields each item as it is requested by the for-loop. " data-translation="Итератор не генерирует полный список кортежей, а выдаёт каждый элемент по запросу цикла for. " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Итератор не генерирует полный список кортежей, а выдаёт каждый элемент по запросу цикла for. </ya-tr-span><ya-tr-span data-index="54-2" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Thus it can save you some memory." data-translation="Таким образом, он может сэкономить вам немного памяти." data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Таким образом, он может сэкономить вам немного памяти.</ya-tr-span></p>

<p><ya-tr-span data-index="55-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="In Python2 calling " data-translation="В Python 2 вызов " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">В Python 2 вызов </ya-tr-span><code>zip(a,b)</code><ya-tr-span data-index="55-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" on short lists is quicker than using " data-translation=" для коротких списков выполняется быстрее, чем использование " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> для коротких списков выполняется быстрее, чем использование </ya-tr-span><code>itertools.izip(a,b)</code><ya-tr-span data-index="55-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=". " data-translation=". " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">. </ya-tr-span><ya-tr-span data-index="55-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="But in Python3 note that " data-translation="Но в Python 3 обратите внимание, что " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Но в Python 3 обратите внимание, что </ya-tr-span><code>zip</code><ya-tr-span data-index="55-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" returns an iterator by default (i.e. it is equivalent to " data-translation=" по умолчанию возвращает итератор (то есть он эквивалентен " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> по умолчанию возвращает итератор (то есть он эквивалентен </ya-tr-span><code>itertools.izip</code><ya-tr-span data-index="55-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" in Python2)." data-translation=" в Python 2)." data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> в Python 2).</ya-tr-span></p>

<hr>

<p><ya-tr-span data-index="56-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Other variants of interest:" data-translation="Другие варианты, представляющие интерес:" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Другие варианты, представляющие интерес:</ya-tr-span></p>

<ul>
<li><a href="http://docs.python.org/2/library/future_builtins.html#future_builtins.zip" rel="noreferrer"><ya-tr-span data-index="57-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="from future_builtin import zip" data-translation="from future_builtin import zip" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">from future_builtin import zip</ya-tr-span></a><ya-tr-span data-index="57-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" -- if you wish to program with Python3-style " data-translation=" — если вы хотите программировать в стиле Python3 " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> — если вы хотите программировать в стиле Python3 </ya-tr-span><code>zip</code><ya-tr-span data-index="57-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" while in Python2." data-translation=" в Python2." data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> в Python2.</ya-tr-span></li>
<li><a href="http://docs.python.org/2/library/itertools.html#itertools.izip_longest" rel="noreferrer"><ya-tr-span data-index="58-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="itertools.izip_longest" data-translation="itertools.izip_longest" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">itertools.izip_longest</ya-tr-span></a><ya-tr-span data-index="58-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" -- if " data-translation=" — если " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> — если </ya-tr-span><code>a</code><ya-tr-span data-index="58-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" and " data-translation=" и " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> и </ya-tr-span><code>b</code><ya-tr-span data-index="58-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" are of unequal length." data-translation=" имеют разную длину." data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> имеют разную длину.</ya-tr-span></li>
</ul>
    </div>
    <div class="mt24">
        <div class="d-flex fw-wrap ai-start jc-end gs8 gsy">
            <time itemprop="dateCreated" datetime="2013-01-12T13:51:08"></time>
            <div class="flex--item mr16" style="flex: 1 1 100px;">
                


<div class="js-post-menu pt2" data-post-id="14293953" data-post-type-id="2">

    <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">

        <div class="flex--item">
            <a href="/a/14293953" rel="nofollow" itemprop="url" class="js-share-link js-gps-track" title="Короткая постоянная ссылка на этот ответ" data-gps-track="post.click({ item: 2, priv: 0, post_type: 2 })" data-controller="se-share-sheet s-popover" data-se-share-sheet-title="Share a link to this answer" data-se-share-sheet-subtitle="" data-se-share-sheet-post-type="answer" data-se-share-sheet-social="facebook twitter devto" data-se-share-sheet-location="2" data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f3.0%2f" data-se-share-sheet-license-name="CC BY-SA 3.0" data-s-popover-placement="bottom-start" aria-controls="se-share-sheet-1" data-action=" s-popover#toggle se-share-sheet#preventNavigation s-popover:show->se-share-sheet#willShow s-popover:shown->se-share-sheet#didShow" aria-expanded="false"><ya-tr-span data-index="59-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Share" data-translation="Поделиться" data-ch="1" data-type="trSpan" style="visibility: inherit !important;">Поделиться</ya-tr-span></a><div class="s-popover z-dropdown s-anchors s-anchors__default" style="width: unset; max-width: 28em;" id="se-share-sheet-1"><div class="s-popover--arrow"></div><div><label for="share-sheet-input-se-share-sheet-1"><span class="js-title fw-bold">Share a link to this answer</span> <span class="js-subtitle"></span></label></div><div class="my8"><input type="text" id="share-sheet-input-se-share-sheet-1" class="js-input s-input wmn3 sm:wmn-initial bc-black-300 bg-white fc-black-600" readonly=""></div><div class="d-flex jc-space-between ai-center mbn4"><button class="js-copy-link-btn s-btn s-btn__link js-gps-track" data-gps-track="">Copy link</button><a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="license" class="js-license s-block-link w-auto" target="_blank" title="The current license for this post: CC BY-SA 3.0">CC BY-SA 3.0</a><div class="js-social-container d-none"></div></div></div>
        </div>


                    <div class="flex--item">
                        <a href="/posts/14293953/edit" class="js-suggest-edit-post js-gps-track" data-gps-track="post.click({ item: 6, priv: 0, post_type: 2 })" title=""><ya-tr-span data-index="60-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Improve this answer" data-translation="Улучшите этот ответ" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Улучшите этот ответ</ya-tr-span></a>
                    </div>

                <div class="flex--item">
                    <button type="button" id="btnFollowPost-14293953" class="s-btn s-btn__link js-follow-post js-follow-answer js-gps-track" data-gps-track="post.click({ item: 14, priv: 0, post_type: 2 })" data-controller="s-tooltip " data-s-tooltip-placement="bottom" data-s-popover-placement="bottom" aria-controls="" aria-describedby="--stacks-s-tooltip-md3qh5nw"><ya-tr-span data-index="61-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Follow " data-translation=" Подписаться " data-ch="1" data-type="trSpan" style="visibility: inherit !important;">  Подписаться  </ya-tr-span><input type="hidden" id="voteFollowHash" value="70:3:31e,16:c792019729d930e2,10:1734895760,16:c1e30bacae9892be,8:14293953,51129890b02ac7fb0969ef3d02373231e97e6ba972c99404da836d5de32c3059">
                    </button><div id="--stacks-s-tooltip-md3qh5nw" class="s-popover s-popover__tooltip" role="tooltip">Follow this answer to receive notifications<div class="s-popover--arrow"></div></div>
                </div>






    </div>
    <div class="js-menu-popup-container"></div>
</div>
            </div>
            <div class="post-signature flex--item fl0">
<div class="user-info ">
    <div class="d-flex ">
        <div class="user-action-time fl-grow1">
            <a href="/posts/14293953/revisions" title="показать все правки в этом посте" class="js-gps-track" data-gps-track="post.click({ item: 4, priv: 0, post_type: 2 })"><ya-tr-span data-index="62-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="edited " data-translation="отредактировано " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">отредактировано </ya-tr-span><span title="2013-01-12 14:35:03Z" class="relativetime"><ya-tr-span data-index="62-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Jan 12, 2013 at 14:35" data-translation="12 января 2013 года в 14:35" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">12 января 2013 года в 14:35</ya-tr-span></span></a>
        </div>
        
    </div>
    <div class="user-gravatar32">
        
    </div>
    <div class="user-details">
        
        <div class="-flair">
            
        </div>
    </div>
</div>
            </div>


            <div class="post-signature flex--item fl0">
                <div class="user-info user-hover ">
    <div class="d-flex ">
        <div class="user-action-time fl-grow1"><ya-tr-span data-index="63-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" answered " data-translation=" ответил " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  ответил </ya-tr-span><span title="2013-01-12 13:51:08Z" class="relativetime"><ya-tr-span data-index="63-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Jan 12, 2013 at 13:51" data-translation="12 января 2013 года в 13:51" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">12 января 2013 года в 13:51</ya-tr-span></span>
        </div>
        
    </div>
    <div class="user-gravatar32">
        <a href="/users/190597/unutbu"><div class="gravatar-wrapper-32"><img src="https://www.gravatar.com/avatar/8f7683207b9fcc8e77120265517f7ce9?s=64&amp;d=identicon&amp;r=PG&amp;f=y&amp;so-version=2" alt="аватар пользователя unutbu" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope="" itemtype="http://schema.org/Person">
        <a href="/users/190597/unutbu"><ya-tr-span data-index="64-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="unutbu" data-translation="унутбу" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">унутбу</ya-tr-span></a><span class="d-none" itemprop="name"><ya-tr-span data-index="64-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="unutbu" data-translation="унутбу" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">унутбу</ya-tr-span></span>
        <div class="-flair">
            <span class="reputation-score" title="оценка репутации 877,551" dir="ltr"><ya-tr-span data-index="65-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="878k" data-translation="878k" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">878k</ya-tr-span></span><span title="194 золотых значка" aria-hidden="true"><span class="badge1"></span><span class="badgecount"><ya-tr-span data-index="65-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="194" data-translation="194" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">194</ya-tr-span></span></span><span class="v-visible-sr"><ya-tr-span data-index="65-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="194 gold badges" data-translation="194 золотых значка" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">194 золотых значка</ya-tr-span></span><span title="1,8 тыс. серебряных значков" aria-hidden="true"><span class="badge2"></span><span class="badgecount"><ya-tr-span data-index="65-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="1.8k" data-translation="1,8k" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">1,8k</ya-tr-span></span></span><span class="v-visible-sr"><ya-tr-span data-index="65-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="1.8k silver badges" data-translation="1,8k серебряных значков" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">1,8k серебряных значков</ya-tr-span></span><span title="1.7 тыс. бронзовых значков" aria-hidden="true"><span class="badge3"></span><span class="badgecount"><ya-tr-span data-index="65-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="1.7k" data-translation="1,7k" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">1,7k</ya-tr-span></span></span><span class="v-visible-sr"><ya-tr-span data-index="65-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="1.7k bronze badges" data-translation="1,7k бронзовых значков" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">1,7k бронзовых значков</ya-tr-span></span>
        </div>
    </div>
</div>


            </div>
        </div>
        
    
    </div>
    
</div>




                <span class="d-none" itemprop="commentCount">3</span> 
    <div class="post-layout--right js-post-comments-component">
        <div id="comments-14293953" class="comments js-comments-container bt bc-black-200 mt12 " data-post-id="14293953" data-min-length="15">
            <ul class="comments-list js-comments-list" data-remaining-comments-count="0" data-canpost="false" data-cansee="true" data-comments-unavailable="false" data-addlink-disabled="true">

                        <li id="comment-19852012" class="comment js-comment " data-comment-id="19852012" data-comment-owner-id="989121" data-comment-score="1">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-score js-comment-edit-hide">
                    <span title="количество полученных голосов за &quot;полезный комментарий&quot;" class="cool">1</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy"><ya-tr-span data-index="66-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="To make this complete, I'd also mention " data-translation="Для полноты картины я бы также упомянул " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Для полноты картины я бы также упомянул </ya-tr-span><code>future_builtins</code><ya-tr-span data-index="66-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="." data-translation="." data-ch="0" data-type="trSpan" style="visibility: inherit !important;">.</ya-tr-span></span>
                
                <div class="d-inline-flex ai-center"><ya-tr-span data-index="67-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" – " data-translation=" – " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> – </ya-tr-span><a href="/users/989121/georg" title="214,711 репутация" class="comment-user"><ya-tr-span data-index="67-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="georg" data-translation="georg" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">georg</ya-tr-span></a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment19852012_14293953">
                    <span class="v-visible-sr"><ya-tr-span data-index="68-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Commented" data-translation="Опубликовано" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Опубликовано</ya-tr-span></span>
                    <span title="2013-01-12 14:01:54Z, Лицензия: CC BY-SA 3.0" class="relativetime-clean"><ya-tr-span data-index="68-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Jan 12, 2013 at 14:01" data-translation="12 января 2013 года в 14:01" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">12 января 2013 года в 14:01</ya-tr-span></span>
                </a></span>
            </div>
        </div>
    </li>
    <li id="comment-19852151" class="comment js-comment " data-comment-id="19852151" data-comment-owner-id="432913" data-comment-score="0">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-score js-comment-edit-hide">
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy"><ya-tr-span data-index="69-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="So in zip in python3 is the same as itertools.izip? " data-translation="То есть в Python 3 zip — это то же самое, что itertools.izip? " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">То есть в Python 3 zip — это то же самое, что itertools.izip? </ya-tr-span><ya-tr-span data-index="69-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Or does it change depending on the size of the lists?" data-translation="Или это зависит от размера списков?" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Или это зависит от размера списков?</ya-tr-span></span>
                
                <div class="d-inline-flex ai-center"><ya-tr-span data-index="70-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" – " data-translation=" – " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> – </ya-tr-span><a href="/users/432913/will" title="репутация 10,600" class="comment-user owner"><ya-tr-span data-index="70-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="will" data-translation="будет" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">будет</ya-tr-span></a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment19852151_14293953">
                    <span class="v-visible-sr"><ya-tr-span data-index="71-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Commented" data-translation="Опубликовано" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Опубликовано</ya-tr-span></span>
                    <span title="2013-01-12 14:10:49Z, Лицензия: CC BY-SA 3.0" class="relativetime-clean"><ya-tr-span data-index="71-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Jan 12, 2013 at 14:10" data-translation="12 января 2013 года в 14:10" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">12 января 2013 года в 14:10</ya-tr-span></span>
                </a></span>
            </div>
        </div>
    </li>
    <li id="comment-19852266" class="comment js-comment " data-comment-id="19852266" data-comment-owner-id="190597" data-comment-score="3">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-score js-comment-edit-hide">
                    <span title="количество полученных голосов за &quot;полезный комментарий&quot;" class="cool">3</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy"><ya-tr-span data-index="72-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="@will: Yes, " data-translation="@will: Да, " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">@will: Да, </ya-tr-span><code>zip</code><ya-tr-span data-index="72-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" in Python3 is the same as " data-translation=" в Python3 работает так же, как " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> в Python3 работает так же, как </ya-tr-span><code>itertools.izip</code><ya-tr-span data-index="72-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" in Python2. " data-translation=" в Python2. " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> в Python2. </ya-tr-span><ya-tr-span data-index="72-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="(It does not change behavior with the size of the list.) " data-translation="(Размер списка не влияет на поведение.) " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">(Размер списка не влияет на поведение.) </ya-tr-span><ya-tr-span data-index="72-2" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="To get the old " data-translation="Чтобы получить старое поведение " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Чтобы получить старое поведение </ya-tr-span><code>zip</code><ya-tr-span data-index="72-2" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" behavior in Python3, use " data-translation=" в Python3, используйте " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> в Python3, используйте </ya-tr-span><code>list(zip(a,b))</code><ya-tr-span data-index="72-2" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="." data-translation="." data-ch="0" data-type="trSpan" style="visibility: inherit !important;">.</ya-tr-span></span>
                
                <div class="d-inline-flex ai-center"><ya-tr-span data-index="73-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" – " data-translation=" – " data-ch="0" data-type="trSpan" style="visibility: inherit !important;"> – </ya-tr-span><a href="/users/190597/unutbu" title="репутация 877,551" class="comment-user"><ya-tr-span data-index="73-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="unutbu" data-translation="унутбу" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">унутбу</ya-tr-span></a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment19852266_14293953">
                    <span class="v-visible-sr"><ya-tr-span data-index="74-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Commented" data-translation="Опубликовано" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Опубликовано</ya-tr-span></span>
                    <span title="2013-01-12 14:20:32Z, Лицензия: CC BY-SA 3.0" class="relativetime-clean"><ya-tr-span data-index="74-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Jan 12, 2013 at 14:20" data-translation="12 января 2013 года в 14:20" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">12 января 2013 года в 14:20</ya-tr-span></span>
                </a></span>
            </div>
        </div>
    </li>

            </ul>
	    </div>

        <div id="comments-link-14293953" data-rep="50" data-anon="true">
                    <a class="js-add-link comments-link disabled-link" title="Используйте комментарии, чтобы запросить дополнительную информацию или предложить улучшения. Избегайте таких комментариев, как «+1» или «спасибо»." href="#" role="button"><ya-tr-span data-index="75-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Add a comment" data-translation="Добавить комментарий" data-ch="1" data-type="trSpan" style="visibility: inherit !important;">Добавить комментарий</ya-tr-span></a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link dno" title="Разверните, чтобы показать все комментарии к этому сообщению" href="#" onclick="" role="button"></a>
        </div>         
    </div>
        </div>
</div>
<div class="js-zone-container zone-container-main">
    <div id="dfp-mlb" class="everyonelovesstackoverflow everyoneloves__mid-leaderboard everyoneloves__leaderboard"></div>
		<div class="js-report-ad-button-container " style="width: 728px"></div>
</div>
                                    
<a name="14293895"></a>
<div id="answer-14293895" class="answer js-answer" data-answerid="14293895" data-parentid="14293869" data-score="13" data-position-on-page="2" data-highest-scored="0" data-question-has-accepted-highest-score="1" itemprop="suggestedAnswer" itemscope="" itemtype="https://schema.org/Answer">
        <div class="post-layout">
            <div class="votecell post-layout--left">
                

<div class="js-voting-container d-flex jc-center fd-column ai-center gs4 fc-black-300" data-post-id="14293895" data-referrer="None">
        <button class="js-vote-up-btn flex--item s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Up vote" data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100" data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200" aria-describedby="--stacks-s-tooltip-ol11utbp">
            <svg aria-hidden="true" class="svg-icon iconArrowUp" width="18" height="18" viewBox="0 0 18 18"><path d="M1 12h16L9 4z"></path></svg>
        </button><div id="--stacks-s-tooltip-ol11utbp" class="s-popover s-popover__tooltip" role="tooltip">This answer is useful<div class="s-popover--arrow"></div></div>
        <input type="hidden" id="voteUpHash" value="70:3:31e,16:261739c5ff5fa7f3,10:1734895760,16:87de056287cd4d3e,8:14293895,fcca7579f1a0ebea09ceb08f4b5d00bfc7fa0290b2068642f319040a9ddc39d4">
        <div class="js-vote-count flex--item d-flex fd-column ai-center fc-theme-body-font fw-bold fs-subheading py4" itemprop="upvoteCount" data-value="13">
13        </div>
        <button class="js-vote-down-btn flex--item mb8 s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200" title="This answer is not useful" aria-pressed="false" aria-label="Down vote" data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100" data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200">
            <svg aria-hidden="true" class="svg-icon iconArrowDown" width="18" height="18" viewBox="0 0 18 18"><path d="M1 6h16l-8 8z"></path></svg>
        </button>
        <input type="hidden" id="voteDownHash" value="70:3:31e,16:995eedd3a10b2ff8,10:1734895760,16:d47bb7a057ab520e,8:14293895,c6d5f573400b7697229a63a6be0d98e625bd50f223993a9e40683847d70bcc46">


        
<button class="js-saves-btn s-btn s-btn__unset c-pointer py4" type="button" id="saves-btn-14293895" data-controller="s-tooltip" data-s-tooltip-placement="right" data-s-popover-placement="" data-is-saved="false" aria-label="Save" data-post-id="14293895" data-post-type-id="2" data-user-privilege-for-post-click="0" aria-controls="" data-s-popover-auto-show="false" aria-describedby="--stacks-s-tooltip-hbilvcno">
    <svg aria-hidden="true" class="fc-theme-primary-400 js-saves-btn-selected d-none svg-icon iconBookmark" width="18" height="18" viewBox="0 0 18 18"><path d="M3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4z"></path></svg>
    <svg aria-hidden="true" class="js-saves-btn-unselected svg-icon iconBookmarkAlt" width="18" height="18" viewBox="0 0 18 18"><path d="m9 10.6 4 2.66V3H5v10.26zM3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4z"></path></svg>
</button><div id="--stacks-s-tooltip-hbilvcno" class="s-popover s-popover__tooltip" role="tooltip">Save this answer.<div class="s-popover--arrow"></div></div>







            <div class="js-accepted-answer-indicator flex--item fc-green-400 py6 mtn8 d-none" data-s-tooltip-placement="right" title="Loading when this answer was accepted…" tabindex="0" role="note" aria-label="Accepted">
                <div class="ta-center">
                    <svg aria-hidden="true" class="svg-icon iconCheckmarkLg" width="36" height="36" viewBox="0 0 36 36"><path d="m6 14 8 8L30 6v8L14 30l-8-8z"></path></svg>
                </div>
            </div>

    
    <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/14293895/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-label="Timeline" aria-describedby="--stacks-s-tooltip-ta2qrzv2"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18" viewBox="0 0 19 18"><path d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10z"></path></svg></a><div id="--stacks-s-tooltip-ta2qrzv2" class="s-popover s-popover__tooltip" role="tooltip">Show activity on this post.<div class="s-popover--arrow"></div></div>

</div>

            </div>

            

<div class="answercell post-layout--right">
    
    <div class="s-prose js-post-body" itemprop="text">
<p>A possible solution is using <code>zip</code>, as you mentioned yourself, but slightly differently than how you wrote it in the question:</p>

<pre class="lang-py s-code-block"><code data-highlighted="yes" class="hljs language-python"><span class="hljs-keyword">for</span> x, y <span class="hljs-keyword">in</span> <span class="hljs-built_in">zip</span>(a, b):
    <span class="hljs-built_in">print</span> x, y
</code></pre>

<p>Notice that the length of the list of tuples returned by <code>zip()</code> will be equal to the minimum between the lengths of <code>a</code> and <code>b</code>. This impacts when <code>a</code> and <code>b</code> are not of the same length.</p>
    </div>
    <div class="mt24">
        <div class="d-flex fw-wrap ai-start jc-end gs8 gsy">
            <time itemprop="dateCreated" datetime="2013-01-12T13:44:43"></time>
            <div class="flex--item mr16" style="flex: 1 1 100px;">
                


<div class="js-post-menu pt2" data-post-id="14293895" data-post-type-id="2">

    <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">

        <div class="flex--item">
            <a href="/a/14293895" rel="nofollow" itemprop="url" class="js-share-link js-gps-track" title="Short permalink to this answer" data-gps-track="post.click({ item: 2, priv: 0, post_type: 2 })" data-controller="se-share-sheet s-popover" data-se-share-sheet-title="Share a link to this answer" data-se-share-sheet-subtitle="" data-se-share-sheet-post-type="answer" data-se-share-sheet-social="facebook twitter devto" data-se-share-sheet-location="2" data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f3.0%2f" data-se-share-sheet-license-name="CC BY-SA 3.0" data-s-popover-placement="bottom-start" aria-controls="se-share-sheet-2" data-action=" s-popover#toggle se-share-sheet#preventNavigation s-popover:show->se-share-sheet#willShow s-popover:shown->se-share-sheet#didShow" aria-expanded="false">Share</a><div class="s-popover z-dropdown s-anchors s-anchors__default" style="width: unset; max-width: 28em;" id="se-share-sheet-2"><div class="s-popover--arrow"></div><div><label for="share-sheet-input-se-share-sheet-2"><span class="js-title fw-bold">Share a link to this answer</span> <span class="js-subtitle"></span></label></div><div class="my8"><input type="text" id="share-sheet-input-se-share-sheet-2" class="js-input s-input wmn3 sm:wmn-initial bc-black-300 bg-white fc-black-600" readonly=""></div><div class="d-flex jc-space-between ai-center mbn4"><button class="js-copy-link-btn s-btn s-btn__link js-gps-track" data-gps-track="">Copy link</button><a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="license" class="js-license s-block-link w-auto" target="_blank" title="The current license for this post: CC BY-SA 3.0">CC BY-SA 3.0</a><div class="js-social-container d-none"></div></div></div>
        </div>


                    <div class="flex--item">
                        <a href="/posts/14293895/edit" class="js-suggest-edit-post js-gps-track" data-gps-track="post.click({ item: 6, priv: 0, post_type: 2 })" title="">Improve this answer</a>
                    </div>

                <div class="flex--item">
                    <button type="button" id="btnFollowPost-14293895" class="s-btn s-btn__link js-follow-post js-follow-answer js-gps-track" data-gps-track="post.click({ item: 14, priv: 0, post_type: 2 })" data-controller="s-tooltip " data-s-tooltip-placement="bottom" data-s-popover-placement="bottom" aria-controls="" aria-describedby="--stacks-s-tooltip-gm9vor2x">
                        Follow
                        <input type="hidden" id="voteFollowHash" value="70:3:31e,16:98866235d0781976,10:1734895760,16:ae5b63919eaadb9e,8:14293895,e0876a75794817b4765226fc15ad2174dc34f32c28eadc06a8e50d4ed718a244">
                    </button><div id="--stacks-s-tooltip-gm9vor2x" class="s-popover s-popover__tooltip" role="tooltip">Follow this answer to receive notifications<div class="s-popover--arrow"></div></div>
                </div>






    </div>
    <div class="js-menu-popup-container"></div>
</div>
            </div>
            <div class="post-signature flex--item fl0">
<div class="user-info ">
    <div class="d-flex ">
        <div class="user-action-time fl-grow1">
            <a href="/posts/14293895/revisions" title="show all edits to this post" class="js-gps-track" data-gps-track="post.click({ item: 4, priv: 0, post_type: 2 })">edited <span title="2013-01-12 13:51:17Z" class="relativetime">Jan 12, 2013 at 13:51</span></a>
        </div>
        
    </div>
    <div class="user-gravatar32">
        
    </div>
    <div class="user-details">
        
        <div class="-flair">
            
        </div>
    </div>
</div>
            </div>


            <div class="post-signature flex--item fl0">
                <div class="user-info ">
    <div class="d-flex ">
        <div class="user-action-time fl-grow1">
            answered <span title="2013-01-12 13:44:43Z" class="relativetime">Jan 12, 2013 at 13:44</span>
        </div>
        
    </div>
    <div class="user-gravatar32">
        <a href="/users/528313/vincenzo-pii"><div class="gravatar-wrapper-32"><img src="https://www.gravatar.com/avatar/4e655003114fdb9b556a9bcda11caa5f?s=64&amp;d=identicon&amp;r=PG" alt="Vincenzo Pii's user avatar" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope="" itemtype="http://schema.org/Person">
        <a href="/users/528313/vincenzo-pii">Vincenzo Pii</a><span class="d-none" itemprop="name">Vincenzo Pii</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score 19,795" dir="ltr">19.8k</span><span title="9 gold badges" aria-hidden="true"><span class="badge1"></span><span class="badgecount">9</span></span><span class="v-visible-sr">9 gold badges</span><span title="41 silver badges" aria-hidden="true"><span class="badge2"></span><span class="badgecount">41</span></span><span class="v-visible-sr">41 silver badges</span><span title="50 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">50</span></span><span class="v-visible-sr">50 bronze badges</span>
        </div>
    </div>
</div>


            </div>
        </div>
        
    
    </div>
    
</div>




                <span class="d-none" itemprop="commentCount">2</span> 
    <div class="post-layout--right js-post-comments-component">
        <div id="comments-14293895" class="comments js-comments-container bt bc-black-200 mt12 " data-post-id="14293895" data-min-length="15">
            <ul class="comments-list js-comments-list" data-remaining-comments-count="0" data-canpost="false" data-cansee="true" data-comments-unavailable="false" data-addlink-disabled="true">

                        <li id="comment-19851825" class="comment js-comment " data-comment-id="19851825" data-comment-owner-id="432913" data-comment-score="1">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="cool">1</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">This does look very familiar from various examples and documentation pages</span>
                
                <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/432913/will" title="10,600 reputation" class="comment-user owner">will</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment19851825_14293895">
                    <span class="v-visible-sr">Commented</span>
                    <span title="2013-01-12 13:46:05Z, License: CC BY-SA 3.0" class="relativetime-clean">Jan 12, 2013 at 13:46</span>
                </a></span>
            </div>
        </div>
    </li>
    <li id="comment-19851839" class="comment js-comment " data-comment-id="19851839" data-comment-owner-id="528313" data-comment-score="1">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="cool">1</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">That confirms it's pythonic :)!</span>
                
                <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/528313/vincenzo-pii" title="19,795 reputation" class="comment-user">Vincenzo Pii</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment19851839_14293895">
                    <span class="v-visible-sr">Commented</span>
                    <span title="2013-01-12 13:46:54Z, License: CC BY-SA 3.0" class="relativetime-clean">Jan 12, 2013 at 13:46</span>
                </a></span>
            </div>
        </div>
    </li>

            </ul>
	    </div>

        <div id="comments-link-14293895" data-rep="50" data-anon="true">
                    <a class="js-add-link comments-link disabled-link" title="Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”." href="#" role="button">Add a comment</a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link dno" title="Expand to show all comments on this post" href="#" onclick="" role="button"></a>
        </div>         
    </div>
        </div>
</div>
                                    
<a name="14294522"></a>
<div id="answer-14294522" class="answer js-answer" data-answerid="14294522" data-parentid="14293869" data-score="9" data-position-on-page="3" data-highest-scored="0" data-question-has-accepted-highest-score="1" itemprop="suggestedAnswer" itemscope="" itemtype="https://schema.org/Answer">
        <div class="post-layout">
            <div class="votecell post-layout--left">
                

<div class="js-voting-container d-flex jc-center fd-column ai-center gs4 fc-black-300" data-post-id="14294522" data-referrer="None">
        <button class="js-vote-up-btn flex--item s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Up vote" data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100" data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200" aria-describedby="--stacks-s-tooltip-xgja5vl4">
            <svg aria-hidden="true" class="svg-icon iconArrowUp" width="18" height="18" viewBox="0 0 18 18"><path d="M1 12h16L9 4z"></path></svg>
        </button><div id="--stacks-s-tooltip-xgja5vl4" class="s-popover s-popover__tooltip" role="tooltip">This answer is useful<div class="s-popover--arrow"></div></div>
        <input type="hidden" id="voteUpHash" value="70:3:31e,16:46868f7484f8a234,10:1734895760,16:4d53d623d0b970c9,8:14294522,a9d4a892a2c966ea8ef99f09a8001e3da9d41b4d2bfe8f39d09cc5575ac2bdfb">
        <div class="js-vote-count flex--item d-flex fd-column ai-center fc-theme-body-font fw-bold fs-subheading py4" itemprop="upvoteCount" data-value="9">
9        </div>
        <button class="js-vote-down-btn flex--item mb8 s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200" title="This answer is not useful" aria-pressed="false" aria-label="Down vote" data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100" data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200">
            <svg aria-hidden="true" class="svg-icon iconArrowDown" width="18" height="18" viewBox="0 0 18 18"><path d="M1 6h16l-8 8z"></path></svg>
        </button>
        <input type="hidden" id="voteDownHash" value="70:3:31e,16:e970d50c8480c62e,10:1734895760,16:fc7398bf0f0a2c74,8:14294522,3f8baf7f6abc54a9387e43e12e27cbf485544f34c9a476ad980d789a314f491b">


        
<button class="js-saves-btn s-btn s-btn__unset c-pointer py4" type="button" id="saves-btn-14294522" data-controller="s-tooltip" data-s-tooltip-placement="right" data-s-popover-placement="" data-is-saved="false" aria-label="Save" data-post-id="14294522" data-post-type-id="2" data-user-privilege-for-post-click="0" aria-controls="" data-s-popover-auto-show="false" aria-describedby="--stacks-s-tooltip-8mvkqxkj">
    <svg aria-hidden="true" class="fc-theme-primary-400 js-saves-btn-selected d-none svg-icon iconBookmark" width="18" height="18" viewBox="0 0 18 18"><path d="M3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4z"></path></svg>
    <svg aria-hidden="true" class="js-saves-btn-unselected svg-icon iconBookmarkAlt" width="18" height="18" viewBox="0 0 18 18"><path d="m9 10.6 4 2.66V3H5v10.26zM3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4z"></path></svg>
</button><div id="--stacks-s-tooltip-8mvkqxkj" class="s-popover s-popover__tooltip" role="tooltip">Save this answer.<div class="s-popover--arrow"></div></div>







            <div class="js-accepted-answer-indicator flex--item fc-green-400 py6 mtn8 d-none" data-s-tooltip-placement="right" title="Loading when this answer was accepted…" tabindex="0" role="note" aria-label="Accepted">
                <div class="ta-center">
                    <svg aria-hidden="true" class="svg-icon iconCheckmarkLg" width="36" height="36" viewBox="0 0 36 36"><path d="m6 14 8 8L30 6v8L14 30l-8-8z"></path></svg>
                </div>
            </div>

    
    <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/14294522/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-label="Timeline" aria-describedby="--stacks-s-tooltip-gy0c77bc"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18" viewBox="0 0 19 18"><path d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10z"></path></svg></a><div id="--stacks-s-tooltip-gy0c77bc" class="s-popover s-popover__tooltip" role="tooltip">Show activity on this post.<div class="s-popover--arrow"></div></div>

</div>

            </div>

            

<div class="answercell post-layout--right">
    
    <div class="s-prose js-post-body" itemprop="text">
<p>Instead of using <code>zip</code> you could use <a href="http://www.numpy.org/" rel="noreferrer">Numpy</a>, especially if speed is important and you have long arrays. Its much faster and once you're using numpy arrays you don't need a loop, and can just write:</p>

<pre class="lang-py s-code-block"><code data-highlighted="yes" class="hljs language-python"><span class="hljs-built_in">print</span> a + b
</code></pre>

<p>Graph showing averaged timings for summing different length lists using zip, izip, and numpy:
<img src="https://i.sstatic.net/RF0M0.png" alt="enter image description here"></p>
    </div>
    <div class="mt24">
        <div class="d-flex fw-wrap ai-start jc-end gs8 gsy">
            <time itemprop="dateCreated" datetime="2013-01-12T14:57:35"></time>
            <div class="flex--item mr16" style="flex: 1 1 100px;">
                


<div class="js-post-menu pt2" data-post-id="14294522" data-post-type-id="2">

    <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">

        <div class="flex--item">
            <a href="/a/14294522" rel="nofollow" itemprop="url" class="js-share-link js-gps-track" title="Short permalink to this answer" data-gps-track="post.click({ item: 2, priv: 0, post_type: 2 })" data-controller="se-share-sheet s-popover" data-se-share-sheet-title="Share a link to this answer" data-se-share-sheet-subtitle="" data-se-share-sheet-post-type="answer" data-se-share-sheet-social="facebook twitter devto" data-se-share-sheet-location="2" data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f3.0%2f" data-se-share-sheet-license-name="CC BY-SA 3.0" data-s-popover-placement="bottom-start" aria-controls="se-share-sheet-3" data-action=" s-popover#toggle se-share-sheet#preventNavigation s-popover:show->se-share-sheet#willShow s-popover:shown->se-share-sheet#didShow" aria-expanded="false">Share</a><div class="s-popover z-dropdown s-anchors s-anchors__default" style="width: unset; max-width: 28em;" id="se-share-sheet-3"><div class="s-popover--arrow"></div><div><label for="share-sheet-input-se-share-sheet-3"><span class="js-title fw-bold">Share a link to this answer</span> <span class="js-subtitle"></span></label></div><div class="my8"><input type="text" id="share-sheet-input-se-share-sheet-3" class="js-input s-input wmn3 sm:wmn-initial bc-black-300 bg-white fc-black-600" readonly=""></div><div class="d-flex jc-space-between ai-center mbn4"><button class="js-copy-link-btn s-btn s-btn__link js-gps-track" data-gps-track="">Copy link</button><a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="license" class="js-license s-block-link w-auto" target="_blank" title="The current license for this post: CC BY-SA 3.0">CC BY-SA 3.0</a><div class="js-social-container d-none"></div></div></div>
        </div>


                    <div class="flex--item">
                        <a href="/posts/14294522/edit" class="js-suggest-edit-post js-gps-track" data-gps-track="post.click({ item: 6, priv: 0, post_type: 2 })" title="">Improve this answer</a>
                    </div>

                <div class="flex--item">
                    <button type="button" id="btnFollowPost-14294522" class="s-btn s-btn__link js-follow-post js-follow-answer js-gps-track" data-gps-track="post.click({ item: 14, priv: 0, post_type: 2 })" data-controller="s-tooltip " data-s-tooltip-placement="bottom" data-s-popover-placement="bottom" aria-controls="" aria-describedby="--stacks-s-tooltip-uatn02br">
                        Follow
                        <input type="hidden" id="voteFollowHash" value="70:3:31e,16:a359d188481f6cce,10:1734895760,16:cd5da7c413148456,8:14294522,c8f405eb36b537ab910bb4192dc97cc704149e1b397f22f5cd68cf634850a917">
                    </button><div id="--stacks-s-tooltip-uatn02br" class="s-popover s-popover__tooltip" role="tooltip">Follow this answer to receive notifications<div class="s-popover--arrow"></div></div>
                </div>






    </div>
    <div class="js-menu-popup-container"></div>
</div>
            </div>


            <div class="post-signature flex--item fl0">
                <div class="user-info user-hover ">
    <div class="d-flex ">
        <div class="user-action-time fl-grow1">
            answered <span title="2013-01-12 14:57:35Z" class="relativetime">Jan 12, 2013 at 14:57</span>
        </div>
        
    </div>
    <div class="user-gravatar32">
        <a href="/users/1175101/fraxel"><div class="gravatar-wrapper-32"><img src="https://www.gravatar.com/avatar/574a1e69c572acc1f946a4ebea5f7037?s=64&amp;d=identicon&amp;r=PG" alt="fraxel's user avatar" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope="" itemtype="http://schema.org/Person">
        <a href="/users/1175101/fraxel">fraxel</a><span class="d-none" itemprop="name">fraxel</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score 35,199" dir="ltr">35.2k</span><span title="11 gold badges" aria-hidden="true"><span class="badge1"></span><span class="badgecount">11</span></span><span class="v-visible-sr">11 gold badges</span><span title="100 silver badges" aria-hidden="true"><span class="badge2"></span><span class="badgecount">100</span></span><span class="v-visible-sr">100 silver badges</span><span title="103 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">103</span></span><span class="v-visible-sr">103 bronze badges</span>
        </div>
    </div>
</div>


            </div>
        </div>
        
    
    </div>
    
</div>




                <span class="d-none" itemprop="commentCount">1</span> 
    <div class="post-layout--right js-post-comments-component">
        <div id="comments-14294522" class="comments js-comments-container bt bc-black-200 mt12 " data-post-id="14294522" data-min-length="15">
            <ul class="comments-list js-comments-list" data-remaining-comments-count="0" data-canpost="false" data-cansee="true" data-comments-unavailable="false" data-addlink-disabled="true">

                        <li id="comment-19855689" class="comment js-comment " data-comment-id="19855689" data-comment-owner-id="432913" data-comment-score="1">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="cool">1</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">Yah i know about numpy. It's definitely applicable in this instance, but the example i gave was just a contrived one. What i really want it for is when you have two lists of objects, and you want to access the nth object of both.  It became apparent to me when i wanted to add a <code>hatch</code> pattern to <code>wedges</code> in a <code>matplotlib</code> piechart. The end use would be something like <code>for pattern, wedge in zip(patterns, wedges): wedge.set_hatch(pattern)</code></span>
                
                <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/432913/will" title="10,600 reputation" class="comment-user owner">will</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment19855689_14294522">
                    <span class="v-visible-sr">Commented</span>
                    <span title="2013-01-12 17:45:36Z, License: CC BY-SA 3.0" class="relativetime-clean">Jan 12, 2013 at 17:45</span>
                </a></span>
            </div>
        </div>
    </li>

            </ul>
	    </div>

        <div id="comments-link-14294522" data-rep="50" data-anon="true">
                    <a class="js-add-link comments-link disabled-link" title="Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”." href="#" role="button">Add a comment</a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link dno" title="Expand to show all comments on this post" href="#" onclick="" role="button"></a>
        </div>         
    </div>
        </div>
</div>
<div class="js-zone-container zone-container-main">
    <div id="dfp-smlb" class="everyonelovesstackoverflow everyoneloves__mid-second-leaderboard everyoneloves__leaderboard"></div>
		<div class="js-report-ad-button-container " style="width: 728px"></div>
</div>
                                    
<a name="45082250"></a>
<div id="answer-45082250" class="answer js-answer" data-answerid="45082250" data-parentid="14293869" data-score="2" data-position-on-page="4" data-highest-scored="0" data-question-has-accepted-highest-score="1" itemprop="suggestedAnswer" itemscope="" itemtype="https://schema.org/Answer">
        <div class="post-layout">
            <div class="votecell post-layout--left">
                

<div class="js-voting-container d-flex jc-center fd-column ai-center gs4 fc-black-300" data-post-id="45082250" data-referrer="None">
        <button class="js-vote-up-btn flex--item s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Up vote" data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100" data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200" aria-describedby="--stacks-s-tooltip-u6olj3yf">
            <svg aria-hidden="true" class="svg-icon iconArrowUp" width="18" height="18" viewBox="0 0 18 18"><path d="M1 12h16L9 4z"></path></svg>
        </button><div id="--stacks-s-tooltip-u6olj3yf" class="s-popover s-popover__tooltip" role="tooltip">This answer is useful<div class="s-popover--arrow"></div></div>
        <input type="hidden" id="voteUpHash" value="70:3:31e,16:c0a4fe5fb83da966,10:1734895760,16:504a6031d98fd2cc,8:45082250,5d4a6e19b234bc38142ee6fbebb8921537a24a8dddcb29c37eceb00cabef0b5a">
        <div class="js-vote-count flex--item d-flex fd-column ai-center fc-theme-body-font fw-bold fs-subheading py4" itemprop="upvoteCount" data-value="2">
2        </div>
        <button class="js-vote-down-btn flex--item mb8 s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200" title="This answer is not useful" aria-pressed="false" aria-label="Down vote" data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100" data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200">
            <svg aria-hidden="true" class="svg-icon iconArrowDown" width="18" height="18" viewBox="0 0 18 18"><path d="M1 6h16l-8 8z"></path></svg>
        </button>
        <input type="hidden" id="voteDownHash" value="70:3:31e,16:3a75ed5a64a45f51,10:1734895760,16:1d5616ce5f80915d,8:45082250,3eb700c4ab9e117f1d09bbf456a59a0a4b3ef81ea2df06a7c1ba8ddc44c68415">


        
<button class="js-saves-btn s-btn s-btn__unset c-pointer py4" type="button" id="saves-btn-45082250" data-controller="s-tooltip" data-s-tooltip-placement="right" data-s-popover-placement="" data-is-saved="false" aria-label="Save" data-post-id="45082250" data-post-type-id="2" data-user-privilege-for-post-click="0" aria-controls="" data-s-popover-auto-show="false" aria-describedby="--stacks-s-tooltip-vc070fao">
    <svg aria-hidden="true" class="fc-theme-primary-400 js-saves-btn-selected d-none svg-icon iconBookmark" width="18" height="18" viewBox="0 0 18 18"><path d="M3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4z"></path></svg>
    <svg aria-hidden="true" class="js-saves-btn-unselected svg-icon iconBookmarkAlt" width="18" height="18" viewBox="0 0 18 18"><path d="m9 10.6 4 2.66V3H5v10.26zM3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4z"></path></svg>
</button><div id="--stacks-s-tooltip-vc070fao" class="s-popover s-popover__tooltip" role="tooltip">Save this answer.<div class="s-popover--arrow"></div></div>







            <div class="js-accepted-answer-indicator flex--item fc-green-400 py6 mtn8 d-none" data-s-tooltip-placement="right" title="Loading when this answer was accepted…" tabindex="0" role="note" aria-label="Accepted">
                <div class="ta-center">
                    <svg aria-hidden="true" class="svg-icon iconCheckmarkLg" width="36" height="36" viewBox="0 0 36 36"><path d="m6 14 8 8L30 6v8L14 30l-8-8z"></path></svg>
                </div>
            </div>

    
    <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/45082250/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-label="Timeline" aria-describedby="--stacks-s-tooltip-l6hf9o76"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18" viewBox="0 0 19 18"><path d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10z"></path></svg></a><div id="--stacks-s-tooltip-l6hf9o76" class="s-popover s-popover__tooltip" role="tooltip">Show activity on this post.<div class="s-popover--arrow"></div></div>

</div>

            </div>

            

<div class="answercell post-layout--right">
    
    <div class="s-prose js-post-body" itemprop="text">
<p>Offering this answer for completeness since <code>numpy</code> has been discussed in another answer, and it is often useful to pair values together from higher ranked arrays. </p>

<p>The <a href="https://stackoverflow.com/a/14293953/2437514">accepted answer</a> works great for any sequence/array of rank 1. However, if the sequence is of multiple levels (such as a <code>numpy</code> array of rank 2 or more, but also such as in a <code>list</code> of <code>list</code>s, or <code>tuple</code> of <code>tuple</code>s), one needs to iterate through each rank. Below is an example with a 2D <code>numpy</code> array: </p>

<pre class="lang-py s-code-block"><code data-highlighted="yes" class="hljs language-python"><span class="hljs-keyword">import</span> numpy <span class="hljs-keyword">as</span> np
a = np.array([[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>], [<span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>], [<span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>]])
b = np.array([<span class="hljs-built_in">list</span>(<span class="hljs-string">'abc'</span>), <span class="hljs-built_in">list</span>(<span class="hljs-string">'pdq'</span>), <span class="hljs-built_in">list</span>(<span class="hljs-string">'xyz'</span>)])
c = np.array([[frobnicate(aval, bval) <span class="hljs-keyword">for</span> aval, bval <span class="hljs-keyword">in</span> <span class="hljs-built_in">zip</span>(arow, brow)] <span class="hljs-keyword">for</span> arow, brow <span class="hljs-keyword">in</span> <span class="hljs-built_in">zip</span>(a, b)])
</code></pre>

<p>And the same concept will work for any set of two dimensional nested sequences of the same shape:</p>

<pre class="lang-py s-code-block"><code data-highlighted="yes" class="hljs language-python">a = [[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>], [<span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>], [<span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>]]
b = [<span class="hljs-built_in">list</span>(<span class="hljs-string">'abc'</span>), <span class="hljs-built_in">list</span>(<span class="hljs-string">'pdq'</span>), <span class="hljs-built_in">list</span>(<span class="hljs-string">'xyz'</span>)]
c = [[frobnicate(aval, bval) <span class="hljs-keyword">for</span> aval, bval <span class="hljs-keyword">in</span> <span class="hljs-built_in">zip</span>(arow, brow)] <span class="hljs-keyword">for</span> arow, brow <span class="hljs-keyword">in</span> <span class="hljs-built_in">zip</span>(a, b)]
</code></pre>

<p>If one or both of the nested sequences has "holes" in it, use <a href="https://docs.python.org/2/library/itertools.html#itertools.izip_longest" rel="nofollow noreferrer"><code>itertools.zip_longest</code></a> to fill in the holes (the fill value defaults to <code>None</code> but can be specified):</p>

<pre class="lang-py s-code-block"><code data-highlighted="yes" class="hljs language-python"><span class="hljs-keyword">from</span> itertools <span class="hljs-keyword">import</span> zip_longest <span class="hljs-keyword">as</span> zipl
a = [[], [<span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>], [<span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>]] <span class="hljs-comment"># empty list in the first row</span>
b = [<span class="hljs-built_in">list</span>(<span class="hljs-string">'abc'</span>), <span class="hljs-built_in">list</span>(<span class="hljs-string">'pdq'</span>), []] <span class="hljs-comment"># empty list in the last row</span>
c = [[frobnicate(aval, bval) <span class="hljs-keyword">for</span> aval, bval <span class="hljs-keyword">in</span> zipl(arow, brow)] <span class="hljs-keyword">for</span> arow, brow <span class="hljs-keyword">in</span> zipl(a, b)]
</code></pre>
    </div>
    <div class="mt24">
        <div class="d-flex fw-wrap ai-start jc-end gs8 gsy">
            <time itemprop="dateCreated" datetime="2017-07-13T13:34:55"></time>
            <div class="flex--item mr16" style="flex: 1 1 100px;">
                


<div class="js-post-menu pt2" data-post-id="45082250" data-post-type-id="2">

    <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">

        <div class="flex--item">
            <a href="/a/45082250" rel="nofollow" itemprop="url" class="js-share-link js-gps-track" title="Short permalink to this answer" data-gps-track="post.click({ item: 2, priv: 0, post_type: 2 })" data-controller="se-share-sheet s-popover" data-se-share-sheet-title="Share a link to this answer" data-se-share-sheet-subtitle="" data-se-share-sheet-post-type="answer" data-se-share-sheet-social="facebook twitter devto" data-se-share-sheet-location="2" data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f3.0%2f" data-se-share-sheet-license-name="CC BY-SA 3.0" data-s-popover-placement="bottom-start" aria-controls="se-share-sheet-4" data-action=" s-popover#toggle se-share-sheet#preventNavigation s-popover:show->se-share-sheet#willShow s-popover:shown->se-share-sheet#didShow" aria-expanded="false">Share</a><div class="s-popover z-dropdown s-anchors s-anchors__default" style="width: unset; max-width: 28em;" id="se-share-sheet-4"><div class="s-popover--arrow"></div><div><label for="share-sheet-input-se-share-sheet-4"><span class="js-title fw-bold">Share a link to this answer</span> <span class="js-subtitle"></span></label></div><div class="my8"><input type="text" id="share-sheet-input-se-share-sheet-4" class="js-input s-input wmn3 sm:wmn-initial bc-black-300 bg-white fc-black-600" readonly=""></div><div class="d-flex jc-space-between ai-center mbn4"><button class="js-copy-link-btn s-btn s-btn__link js-gps-track" data-gps-track="">Copy link</button><a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="license" class="js-license s-block-link w-auto" target="_blank" title="The current license for this post: CC BY-SA 3.0">CC BY-SA 3.0</a><div class="js-social-container d-none"></div></div></div>
        </div>


                    <div class="flex--item">
                        <a href="/posts/45082250/edit" class="js-suggest-edit-post js-gps-track" data-gps-track="post.click({ item: 6, priv: 0, post_type: 2 })" title="">Improve this answer</a>
                    </div>

                <div class="flex--item">
                    <button type="button" id="btnFollowPost-45082250" class="s-btn s-btn__link js-follow-post js-follow-answer js-gps-track" data-gps-track="post.click({ item: 14, priv: 0, post_type: 2 })" data-controller="s-tooltip " data-s-tooltip-placement="bottom" data-s-popover-placement="bottom" aria-controls="" aria-describedby="--stacks-s-tooltip-1uj53srj">
                        Follow
                        <input type="hidden" id="voteFollowHash" value="70:3:31e,16:f648ae812edeb859,10:1734895760,16:c06e0ae56c70f017,8:45082250,b527f9aa25562a41655d3077698e3d194753a9011fc801c5ffd86dbc6f8c5929">
                    </button><div id="--stacks-s-tooltip-1uj53srj" class="s-popover s-popover__tooltip" role="tooltip">Follow this answer to receive notifications<div class="s-popover--arrow"></div></div>
                </div>






    </div>
    <div class="js-menu-popup-container"></div>
</div>
            </div>
            <div class="post-signature flex--item fl0">
<div class="user-info ">
    <div class="d-flex ">
        <div class="user-action-time fl-grow1">
            <a href="/posts/45082250/revisions" title="show all edits to this post" class="js-gps-track" data-gps-track="post.click({ item: 4, priv: 0, post_type: 2 })">edited <span title="2017-07-13 13:41:28Z" class="relativetime">Jul 13, 2017 at 13:41</span></a>
        </div>
        
    </div>
    <div class="user-gravatar32">
        
    </div>
    <div class="user-details">
        
        <div class="-flair">
            
        </div>
    </div>
</div>
            </div>


            <div class="post-signature flex--item fl0">
                <div class="user-info user-hover ">
    <div class="d-flex ">
        <div class="user-action-time fl-grow1">
            answered <span title="2017-07-13 13:34:55Z" class="relativetime">Jul 13, 2017 at 13:34</span>
        </div>
        
    </div>
    <div class="user-gravatar32">
        <a href="/users/2437514/rick"><div class="gravatar-wrapper-32"><img src="https://i.sstatic.net/8QN0K.jpg?s=64" alt="Rick's user avatar" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope="" itemtype="http://schema.org/Person">
        <a href="/users/2437514/rick">Rick</a><span class="d-none" itemprop="name">Rick</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score 45,121" dir="ltr">45.1k</span><span title="16 gold badges" aria-hidden="true"><span class="badge1"></span><span class="badgecount">16</span></span><span class="v-visible-sr">16 gold badges</span><span title="81 silver badges" aria-hidden="true"><span class="badge2"></span><span class="badgecount">81</span></span><span class="v-visible-sr">81 silver badges</span><span title="121 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">121</span></span><span class="v-visible-sr">121 bronze badges</span>
        </div>
    </div>
</div>


            </div>
        </div>
        
    
    </div>
    
</div>




                <span class="d-none" itemprop="commentCount"></span> 
    <div class="post-layout--right js-post-comments-component">
        <div id="comments-45082250" class="comments js-comments-container bt bc-black-200 mt12  dno" data-post-id="45082250" data-min-length="15">
            <ul class="comments-list js-comments-list" data-remaining-comments-count="0" data-canpost="false" data-cansee="true" data-comments-unavailable="false" data-addlink-disabled="true">

            </ul>
	    </div>

        <div id="comments-link-45082250" data-rep="50" data-anon="true">
                    <a class="js-add-link comments-link disabled-link" title="Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”." href="#" role="button">Add a comment</a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link dno" title="Expand to show all comments on this post" href="#" onclick="" role="button"></a>
        </div>         
    </div>
        </div>
</div>
                                    
<a name="77794472"></a>
<div id="answer-77794472" class="answer js-answer" data-answerid="77794472" data-parentid="14293869" data-score="2" data-position-on-page="5" data-highest-scored="0" data-question-has-accepted-highest-score="1" itemprop="suggestedAnswer" itemscope="" itemtype="https://schema.org/Answer">
        <div class="post-layout">
            <div class="votecell post-layout--left">
                

<div class="js-voting-container d-flex jc-center fd-column ai-center gs4 fc-black-300" data-post-id="77794472" data-referrer="None">
        <button class="js-vote-up-btn flex--item s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Up vote" data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100" data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200" aria-describedby="--stacks-s-tooltip-ek2z2aae">
            <svg aria-hidden="true" class="svg-icon iconArrowUp" width="18" height="18" viewBox="0 0 18 18"><path d="M1 12h16L9 4z"></path></svg>
        </button><div id="--stacks-s-tooltip-ek2z2aae" class="s-popover s-popover__tooltip" role="tooltip">This answer is useful<div class="s-popover--arrow"></div></div>
        <input type="hidden" id="voteUpHash" value="70:3:31e,16:08ac208723334b40,10:1734895760,16:b402a4fbcb7bf052,8:77794472,1fc52c92923e4d0c73e702ec708111daaeae4eb5b58c3d0a34d96c87866dcd61">
        <div class="js-vote-count flex--item d-flex fd-column ai-center fc-theme-body-font fw-bold fs-subheading py4" itemprop="upvoteCount" data-value="2">
2        </div>
        <button class="js-vote-down-btn flex--item mb8 s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200" title="This answer is not useful" aria-pressed="false" aria-label="Down vote" data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100" data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200">
            <svg aria-hidden="true" class="svg-icon iconArrowDown" width="18" height="18" viewBox="0 0 18 18"><path d="M1 6h16l-8 8z"></path></svg>
        </button>
        <input type="hidden" id="voteDownHash" value="70:3:31e,16:235a21a1d9ec5c72,10:1734895760,16:7f28c08b4d94a98f,8:77794472,0fb8206d17f570f9db0bde58641d03ef3f5d4e75a95392384aa828a29e6c2c4c">


        
<button class="js-saves-btn s-btn s-btn__unset c-pointer py4" type="button" id="saves-btn-77794472" data-controller="s-tooltip" data-s-tooltip-placement="right" data-s-popover-placement="" data-is-saved="false" aria-label="Save" data-post-id="77794472" data-post-type-id="2" data-user-privilege-for-post-click="0" aria-controls="" data-s-popover-auto-show="false" aria-describedby="--stacks-s-tooltip-u4sp0y2b">
    <svg aria-hidden="true" class="fc-theme-primary-400 js-saves-btn-selected d-none svg-icon iconBookmark" width="18" height="18" viewBox="0 0 18 18"><path d="M3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4z"></path></svg>
    <svg aria-hidden="true" class="js-saves-btn-unselected svg-icon iconBookmarkAlt" width="18" height="18" viewBox="0 0 18 18"><path d="m9 10.6 4 2.66V3H5v10.26zM3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4z"></path></svg>
</button><div id="--stacks-s-tooltip-u4sp0y2b" class="s-popover s-popover__tooltip" role="tooltip">Save this answer.<div class="s-popover--arrow"></div></div>







            <div class="js-accepted-answer-indicator flex--item fc-green-400 py6 mtn8 d-none" data-s-tooltip-placement="right" title="Loading when this answer was accepted…" tabindex="0" role="note" aria-label="Accepted">
                <div class="ta-center">
                    <svg aria-hidden="true" class="svg-icon iconCheckmarkLg" width="36" height="36" viewBox="0 0 36 36"><path d="m6 14 8 8L30 6v8L14 30l-8-8z"></path></svg>
                </div>
            </div>

    
    <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/77794472/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-label="Timeline" aria-describedby="--stacks-s-tooltip-rvhjipdy"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18" viewBox="0 0 19 18"><path d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10z"></path></svg></a><div id="--stacks-s-tooltip-rvhjipdy" class="s-popover s-popover__tooltip" role="tooltip">Show activity on this post.<div class="s-popover--arrow"></div></div>

</div>

            </div>

            

<div class="answercell post-layout--right">
    
    <div class="s-prose js-post-body" itemprop="text">
<p>You can utilize a <code>while loop</code> to iterate over both arrays simultaneously.</p>
<pre class="lang-py s-code-block"><code data-highlighted="yes" class="hljs language-python">i,j = <span class="hljs-number">0</span>,<span class="hljs-number">0</span>
<span class="hljs-keyword">while</span> i &lt; <span class="hljs-built_in">len</span>(a) <span class="hljs-keyword">and</span> j &lt; <span class="hljs-built_in">len</span>(b):
    <span class="hljs-built_in">print</span>(a[i] + n[j])
    i += <span class="hljs-number">1</span> 
    j += <span class="hljs-number">1</span> 
</code></pre>
<p><strong>Note that</strong> this loop is repeated for the <strong>shortest number</strong> of arrays.</p>
    </div>
    <div class="mt24">
        <div class="d-flex fw-wrap ai-start jc-end gs8 gsy">
            <time itemprop="dateCreated" datetime="2024-01-10T15:22:45"></time>
            <div class="flex--item mr16" style="flex: 1 1 100px;">
                


<div class="js-post-menu pt2" data-post-id="77794472" data-post-type-id="2">

    <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">

        <div class="flex--item">
            <a href="/a/77794472" rel="nofollow" itemprop="url" class="js-share-link js-gps-track" title="Short permalink to this answer" data-gps-track="post.click({ item: 2, priv: 0, post_type: 2 })" data-controller="se-share-sheet s-popover" data-se-share-sheet-title="Share a link to this answer" data-se-share-sheet-subtitle="" data-se-share-sheet-post-type="answer" data-se-share-sheet-social="facebook twitter devto" data-se-share-sheet-location="2" data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f4.0%2f" data-se-share-sheet-license-name="CC BY-SA 4.0" data-s-popover-placement="bottom-start" aria-controls="se-share-sheet-5" data-action=" s-popover#toggle se-share-sheet#preventNavigation s-popover:show->se-share-sheet#willShow s-popover:shown->se-share-sheet#didShow" aria-expanded="false">Share</a><div class="s-popover z-dropdown s-anchors s-anchors__default" style="width: unset; max-width: 28em;" id="se-share-sheet-5"><div class="s-popover--arrow"></div><div><label for="share-sheet-input-se-share-sheet-5"><span class="js-title fw-bold">Share a link to this answer</span> <span class="js-subtitle"></span></label></div><div class="my8"><input type="text" id="share-sheet-input-se-share-sheet-5" class="js-input s-input wmn3 sm:wmn-initial bc-black-300 bg-white fc-black-600" readonly=""></div><div class="d-flex jc-space-between ai-center mbn4"><button class="js-copy-link-btn s-btn s-btn__link js-gps-track" data-gps-track="">Copy link</button><a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="license" class="js-license s-block-link w-auto" target="_blank" title="The current license for this post: CC BY-SA 4.0">CC BY-SA 4.0</a><div class="js-social-container d-none"></div></div></div>
        </div>


                    <div class="flex--item">
                        <a href="/posts/77794472/edit" class="js-suggest-edit-post js-gps-track" data-gps-track="post.click({ item: 6, priv: 0, post_type: 2 })" title="">Improve this answer</a>
                    </div>

                <div class="flex--item">
                    <button type="button" id="btnFollowPost-77794472" class="s-btn s-btn__link js-follow-post js-follow-answer js-gps-track" data-gps-track="post.click({ item: 14, priv: 0, post_type: 2 })" data-controller="s-tooltip " data-s-tooltip-placement="bottom" data-s-popover-placement="bottom" aria-controls="" aria-describedby="--stacks-s-tooltip-rtbdmabz">
                        Follow
                        <input type="hidden" id="voteFollowHash" value="70:3:31e,16:33b59b8c9c24164d,10:1734895760,16:37674c0d4adeae2d,8:77794472,749c19399d0e3845858df32ba600b71a6f68527ef07279791441fdc06ea9b346">
                    </button><div id="--stacks-s-tooltip-rtbdmabz" class="s-popover s-popover__tooltip" role="tooltip">Follow this answer to receive notifications<div class="s-popover--arrow"></div></div>
                </div>






    </div>
    <div class="js-menu-popup-container"></div>
</div>
            </div>
            <div class="post-signature flex--item fl0">
<div class="user-info ">
    <div class="d-flex ">
        <div class="user-action-time fl-grow1">
            <a href="/posts/77794472/revisions" title="show all edits to this post" class="js-gps-track" data-gps-track="post.click({ item: 4, priv: 0, post_type: 2 })">edited <span title="2024-01-10 15:30:23Z" class="relativetime">Jan 10 at 15:30</span></a>
        </div>
        
    </div>
    <div class="user-gravatar32">
        
    </div>
    <div class="user-details">
        
        <div class="-flair">
            
        </div>
    </div>
</div>
            </div>


            <div class="post-signature flex--item fl0">
                <div class="user-info ">
    <div class="d-flex ">
        <div class="user-action-time fl-grow1">
            answered <span title="2024-01-10 15:22:45Z" class="relativetime">Jan 10 at 15:22</span>
        </div>
        
    </div>
    <div class="user-gravatar32">
        <a href="/users/14612108/muhammad-ali-malekzadeh"><div class="gravatar-wrapper-32"><img src="https://i.sstatic.net/bnyyj.jpg?s=64" alt="Muhammad Ali Malekzadeh's user avatar" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope="" itemtype="http://schema.org/Person">
        <a href="/users/14612108/muhammad-ali-malekzadeh">Muhammad Ali Malekzadeh</a><span class="d-none" itemprop="name">Muhammad Ali Malekzadeh</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score " dir="ltr">184</span><span title="2 silver badges" aria-hidden="true"><span class="badge2"></span><span class="badgecount">2</span></span><span class="v-visible-sr">2 silver badges</span><span title="10 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">10</span></span><span class="v-visible-sr">10 bronze badges</span>
        </div>
    </div>
</div>


            </div>
        </div>
        
    
    </div>
    
</div>




                <span class="d-none" itemprop="commentCount"></span> 
    <div class="post-layout--right js-post-comments-component">
        <div id="comments-77794472" class="comments js-comments-container bt bc-black-200 mt12  dno" data-post-id="77794472" data-min-length="15">
            <ul class="comments-list js-comments-list" data-remaining-comments-count="0" data-canpost="false" data-cansee="true" data-comments-unavailable="false" data-addlink-disabled="true">

            </ul>
	    </div>

        <div id="comments-link-77794472" data-rep="50" data-anon="true">
                    <a class="js-add-link comments-link disabled-link" title="Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”." href="#" role="button">Add a comment</a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link dno" title="Expand to show all comments on this post" href="#" onclick="" role="button"></a>
        </div>         
    </div>
        </div>
</div>

                        <a name="new-answer"></a>
                            <form id="post-form" action="/questions/14293869/answer/submit" method="post" class="js-add-answer-component post-form">
                                <input type="hidden" id="post-id" value="14293869">
                                <input type="hidden" id="qualityBanWarningShown" name="qualityBanWarningShown" value="false">
                                <input type="hidden" name="referrer" value="https://yandex.ru/">
                                <h2 class="space" id="your-answer-header">
                                    Your Answer
                                </h2>
                                    

    <script>
        StackExchange.ifUsing("editor", function () {
            StackExchange.using("externalEditor", function () {
                StackExchange.using("snippets", function () {
                    StackExchange.snippets.init();
                });
            });
        }, "code-snippets");
    </script>


<script>
    StackExchange.ready(function() {
        var channelOptions = {
            tags: "".split(" "),
            id: "1"
        };
        initTagRenderer("".split(" "), "".split(" "), channelOptions);

        StackExchange.using("externalEditor", function() {
            // Have to fire editor after snippets, if snippets enabled
            if (StackExchange.settings.snippets.snippetsEnabled) {
                StackExchange.using("snippets", function() {
                    createEditor();
                });
            }
            else {
                createEditor();
            }
        });

        function createEditor() {   
            StackExchange.prepareEditor({
                useStacksEditor: false,
                heartbeatType: 'answer',
                autoActivateHeartbeat: false,
                convertImagesToLinks: true,
                noModals: true,
                showLowRepImageUploadWarning: true,
                reputationToPostImages: 10,
                bindNavPrevention: true,
                postfix: "",
                imageUploadEnabled: false,
                imageUploader: {
                    brandingHtml: "",
                    contentPolicyHtml: "User contributions licensed under \u003ca href=\"https://stackoverflow.com/help/licensing\"\u003eCC BY-SA\u003c/a\u003e \u003ca href=\"https://stackoverflow.com/legal/acceptable-use-policy\"\u003e(content policy)\u003c/a\u003e",
                    allowUrls: true,
                },
                onDemand: true,
                discardSelector: ".discard-answer",
                enableTables: true,
                isStacksEditorPreviewEnabled: false
                ,enableTables:true,enableSnippets:true
            });
                    }
    });
</script>
<div id="post-editor" class="post-editor js-post-editor d-flex fd-column g4">


        <div class="ps-relative">
            <div class="wmd-container mb8">
                <div id="wmd-button-bar" class="wmd-button-bar btr-sm"><ul id="wmd-button-row" class="wmd-button-row"><li id="wmd-bold-button" class="wmd-button" style="left: 0px;"><span style="background-position: 0px -20px;"></span></li><li id="wmd-italic-button" class="wmd-button" style="left: 25px;"><span style="background-position: -20px -20px;"></span></li><li id="wmd-spacer1" class="wmd-spacer" style="left: 50px;"><span style="background-position: -40px -20px;"></span></li><li id="wmd-link-button" class="wmd-button" style="left: 75px;"><span style="background-position: -40px -20px;"></span></li><li id="wmd-quote-button" class="wmd-button" style="left: 100px;"><span style="background-position: -60px -20px;"></span></li><li id="wmd-code-button" class="wmd-button" style="left: 125px;"><span style="background-position: -80px -20px;"></span></li><li id="wmd-spacer2" class="wmd-spacer" style="left: 150px;"><span style="background-position: -100px -20px;"></span></li><li id="wmd-olist-button" class="wmd-button" style="left: 175px;"><span style="background-position: -100px -20px;"></span></li><li id="wmd-ulist-button" class="wmd-button" style="left: 200px;"><span style="background-position: -120px -20px;"></span></li><li id="wmd-heading-button" class="wmd-button" style="left: 225px;"><span style="background-position: -140px -20px;"></span></li><li id="wmd-hr-button" class="wmd-button" style="left: 250px;"><span style="background-position: -160px -20px;"></span></li><li id="wmd-spacer3" class="wmd-spacer" style="left: 275px;"><span style="background-position: -180px -20px;"></span></li><li id="wmd-undo-button" class="wmd-button" style="left: 300px;"><span style="background-position: -180px -20px;"></span></li><li id="wmd-redo-button" class="wmd-button" style="left: 325px;"><span style="background-position: -200px -20px;"></span></li><li class="wmd-spacer wmd-spacer-max"></li></ul></div>
                    <div class="ai-content-policy-notice js-ai-policy-notice fc-black p8 bl br bc-black-300 d-none" aria-hidden="true">
                        <div class="d-flex jc-space-between ac-center gsx gs2">
                            <p class="flex--item as-center"><b>Reminder:</b> Answers generated by artificial intelligence tools are not allowed on Stack Overflow. <a href="/help/gen-ai-policy">Learn more</a></p>
                            <button class="flex--item js-dismiss-ai-banner s-btn s-btn__sm s-btn__icon fc-black"><svg aria-hidden="true" class="svg-icon iconClearSm" width="14" height="14" viewBox="0 0 14 14"><path d="M12 3.41 10.59 2 7 5.59 3.41 2 2 3.41 5.59 7 2 10.59 3.41 12 7 8.41 10.59 12 12 10.59 8.41 7z"></path></svg></button>
                        </div>
                    </div>
                    <input type="hidden" name="AIPolicyNoticeShown" value="true">
                <div class="js-stacks-validation">
                    <div class="ps-relative">
                        <textarea id="wmd-input" name="post-text" class="wmd-input s-input bar0 js-post-body-field" data-editor-type="wmd" data-post-type-id="2" cols="92" rows="15" aria-labelledby="your-answer-header" tabindex="101" data-min-length=""></textarea>
                    </div>
                    <div class="s-input-message mt4 d-none js-stacks-validation-message"></div>
                </div>
            </div>
        </div>

    <aside class="d-flex ai-start jc-space-between js-answer-help s-notice s-notice__warning pb0 pr4 pt4 mb8 d-none" role="status" aria-hidden="true">
    <div class="flex--item pt8">
        <p>Thanks for contributing an answer to Stack Overflow!</p><ul><li>Please be sure to <em>answer the question</em>. Provide details and share your research!</li></ul><p>But <em>avoid</em> …</p><ul><li>Asking for help, clarification, or responding to other answers.</li><li>Making statements based on opinion; back them up with references or personal experience.</li></ul><p>To learn more, see our <a href="/help/how-to-answer">tips on writing great answers</a>.</p>
    </div>
    <button class="flex--item js-answer-help-close-btn s-btn s-btn__muted fc-black-600">
        <svg aria-hidden="true" class="svg-icon iconClear" width="18" height="18" viewBox="0 0 18 18"><path d="M15 4.41 13.59 3 9 7.59 4.41 3 3 4.41 7.59 9 3 13.59 4.41 15 9 10.41 13.59 15 15 13.59 10.41 9z"></path></svg>
    </button>
</aside>



    <div>
        <div id="draft-saved" class="fc-success h24" style="display:none;">Draft saved</div>
        <div id="draft-discarded" class="fc-error h24" style="display:none;">Draft discarded</div>
    </div>


            <div id="wmd-preview" class="s-prose mb16 wmd-preview js-wmd-preview"></div>
            <div></div>

        <div class="edit-block">
            <input id="fkey" name="fkey" type="hidden" value="d75a38c9f46387c074e42866b21fab101776168769fc53229633006b67a9d8d5">
            <input id="author" name="author" type="text">
        </div>

</div>


                                <div class="ps-relative">
                                               <div class="form-item new-post-login p0 my16">
                <div class="d-flex gs16 md:fd-column new-login-form">
                    <div class="d-flex fd-column w50 md:w-auto gsy gs8 jc-space-between new-login-left">
                        <h3 class="flex--item fs-title">Sign up or <a id="login-link" href="/users/login?ssrc=question_page&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f14293869%2fwhat-is-the-pythonic-way-to-loop-through-two-arrays-at-the-same-time%23new-answer">log in</a></h3>
                        <script>
                            StackExchange.ready(function () {
                                StackExchange.helpers.onClickDraftSave('#login-link');
                            });
                        </script>
                        <div class="flex--item s-btn s-btn__muted s-btn__outlined s-btn__icon google-login" data-ga="[&quot;sign up&quot;,&quot;Sign Up Started - Google&quot;,&quot;New Post&quot;,null,null]">
                            <svg aria-hidden="true" class="native svg-icon iconGoogle" width="18" height="18" viewBox="0 0 18 18"><path fill="#4285F4" d="M16.51 8H8.98v3h4.3c-.18 1-.74 1.48-1.6 2.04v2.01h2.6a7.8 7.8 0 0 0 2.38-5.88c0-.57-.05-.66-.15-1.18"></path><path fill="#34A853" d="M8.98 17c2.16 0 3.97-.72 5.3-1.94l-2.6-2a4.8 4.8 0 0 1-7.18-2.54H1.83v2.07A8 8 0 0 0 8.98 17"></path><path fill="#FBBC05" d="M4.5 10.52a4.8 4.8 0 0 1 0-3.04V5.41H1.83a8 8 0 0 0 0 7.18z"></path><path fill="#EA4335" d="M8.98 4.18c1.17 0 2.23.4 3.06 1.2l2.3-2.3A8 8 0 0 0 1.83 5.4L4.5 7.49a4.8 4.8 0 0 1 4.48-3.3"></path></svg> Sign up using Google
                        </div>
                        <div class="flex--item s-btn s-btn__muted s-btn__outlined s-btn__icon stackexchange-login" data-ga="[&quot;sign up&quot;,&quot;Sign Up Navigation&quot;,&quot;New Post&quot;,null,null]">
                            <svg aria-hidden="true" class="native svg-icon iconGlyphXSm" width="18" height="18" viewBox="0 0 18 18"><path fill="#BCBBBB" d="M14 16v-5h2v7H2v-7h2v5z"></path><path fill="#F48024" d="m12.09.72-1.21.9 4.5 6.07 1.22-.9zM5 15h8v-2H5zm9.15-5.87L8.35 4.3l.96-1.16 5.8 4.83zm-7.7-1.47 6.85 3.19.63-1.37-6.85-3.2zm6.53 5L5.4 11.39l.38-1.67 7.42 1.48z"></path></svg> Sign up using Email and Password
                        </div>
                    </div>
                    <input type="hidden" name="use-facebook" class="use-facebook" value="false">
                    <input type="hidden" name="use-google" class="use-google" value="false">
                    <button type="button" class="d-none js-submit-openid">Submit</button>
                    <div class="d-flex gsy gs8 fd-column w50 md:w-auto new-login-right form-item p0">
                                <h3 class="flex--item fs-title">Post as a guest</h3>
            <div class="flex--item">
                <div class="d-flex gs4 gsy fd-column">
                    <label class="s-label" for="display-name">Name</label>
                    <div class="d-flex ps-relative">
                        <input class="s-input" id="display-name" name="display-name" maxlength="30" type="text" value="" tabindex="105" placeholder="">
                    </div>
                </div>
            </div>
            <div class="flex--item">
                <div class="d-flex gs4 gsy fd-column">
                    <div class="flex--item">
                        <div class="d-flex gs2 gsy fd-column">
                            <label class="flex--item s-label" for="m-address">Email</label>
                            <p class="flex--item s-description">Required, but never shown</p>
                        </div>
                    </div>
                    <div class="d-flex ps-relative">
                        <input class="s-input js-post-email-field" id="m-address" name="m-address" type="text" value="" size="40" tabindex="106" placeholder="">
                    </div>
                </div>
            </div>

                    </div>
                </div>
            </div>
            <script>
                StackExchange.ready(
                    function () {
                        StackExchange.openid.initPostLogin('.new-post-login', 'https%3a%2f%2fstackoverflow.com%2fquestions%2f14293869%2fwhat-is-the-pythonic-way-to-loop-through-two-arrays-at-the-same-time%23new-answer', 'question_page');
                    }
                );
            </script>
            <noscript>
                        <h3 class="flex--item fs-title">Post as a guest</h3>
            <div class="flex--item">
                <div class="d-flex gs4 gsy fd-column">
                    <label class="s-label" for="display-name">Name</label>
                    <div class="d-flex ps-relative">
                        <input class="s-input" id="display-name" name="display-name" maxlength="30" type="text" value="" tabindex="105" placeholder="" />
                    </div>
                </div>
            </div>
            <div class="flex--item">
                <div class="d-flex gs4 gsy fd-column">
                    <div class="flex--item">
                        <div class="d-flex gs2 gsy fd-column">
                            <label class="flex--item s-label" for="m-address">Email</label>
                            <p class="flex--item s-description">Required, but never shown</p>
                        </div>
                    </div>
                    <div class="d-flex ps-relative">
                        <input class="s-input js-post-email-field" id="m-address" name="m-address" type="text" value="" size="40" tabindex="106" placeholder="" />
                    </div>
                </div>
            </div>

            </noscript>

                                </div>

                                    <div class="form-submit clear-both d-flex sm:fd-column sm:jc-stretch gs4 ai-center">
                                        <button id="submit-button" class="flex--item fl-shrink0 s-btn s-btn__filled sm:w100" type="submit" tabindex="120" autocomplete="off">
                                            Post Your Answer
                                        </button>
                                        <button class="flex--item s-btn s-btn__danger fl-shrink0 sm:w100 discard-answer d-none">
                                            Discard
                                        </button>
                                            <p class="flex--item mb0 fs-italic ml12 sm:ml0">
                                                By clicking “Post Your Answer”, you agree to our <a href="https://stackoverflow.com/legal/terms-of-service/public" name="tos" target="_blank" class="-link">terms of service</a> and acknowledge you have read our <a href="https://stackoverflow.com/legal/privacy-policy" name="privacy" target="_blank" class="-link">privacy policy</a>.<input type="hidden" name="legalLinksShown" value="1">
                                            </p>
                                    </div>
                                    <div class="js-general-error general-error clear-both d-none" aria-live="polite"></div>
                            </form>


                            <h2 class="bottom-notice" data-loc="1">
                                <div>
Not the answer you're looking for? Browse other questions tagged <ul class="ml0 list-ls-none js-post-tag-list-wrapper d-inline"><li class="d-inline mr4 js-post-tag-list-item"><a href="/questions/tagged/python" class="s-tag post-tag js-gps-track" title="show questions tagged 'python'" aria-label="show questions tagged 'python'" rel="tag" aria-labelledby="tag-python-tooltip-container" data-tag-menu-origin="Unknown">python</a></li></ul> or <a href="/questions/ask">ask your own question</a>.                                </div>
                            </h2>
                </div>
            </div>

            
<div id="sidebar" class="show-votes" role="complementary" aria-label="боковая панель">
        

    
    <div class="s-sidebarwidget s-sidebarwidget__yellow s-anchors s-anchors__grayscale mb16" data-tracker="cb=1">
            <ul class="s-sidebarwidget--content s-sidebarwidget__items p0">
                        <li class="s-sidebarwidget--header">
                            The Overflow Blog
                        </li>
        <li class="s-sidebarwidget--item d-flex px16">
            <div class="flex--item1 fl-shrink0">
<svg aria-hidden="true" class="va-text-top svg-icon iconPencilSm" width="14" height="14" viewBox="0 0 14 14"><path fill="#F1B600" d="m2 10.12 6.37-6.43 1.88 1.88L3.88 12H2z"></path><path fill="#E87C87" d="m11.1 1.71 1.13 1.12c.2.2.2.51 0 .71L11.1 4.7 9.21 2.86l1.17-1.15c.2-.2.51-.2.71 0"></path></svg>            </div>
            <div class="flex--item wmn0 ow-break-word">
                <a href="https://stackoverflow.blog/2024/12/19/developers-hate-documentation-ai-generated-toil-work/?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;The Overflow Blog&quot;,&quot;https://stackoverflow.blog/2024/12/19/developers-hate-documentation-ai-generated-toil-work/&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 1, position: 0, location: questionpage })">Why do developers love clean code but hate writing documentation? </a>
            </div>
        </li>
        <li class="s-sidebarwidget--item d-flex px16">
            <div class="flex--item1 fl-shrink0">
<svg aria-hidden="true" class="va-text-top svg-icon iconPencilSm" width="14" height="14" viewBox="0 0 14 14"><path fill="#F1B600" d="m2 10.12 6.37-6.43 1.88 1.88L3.88 12H2z"></path><path fill="#E87C87" d="m11.1 1.71 1.13 1.12c.2.2.2.51 0 .71L11.1 4.7 9.21 2.86l1.17-1.15c.2-.2.51-.2.71 0"></path></svg>            </div>
            <div class="flex--item wmn0 ow-break-word">
                <a href="https://stackoverflow.blog/2024/12/20/this-developer-tool-is-40-years-old-can-it-be-improved/?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;The Overflow Blog&quot;,&quot;https://stackoverflow.blog/2024/12/20/this-developer-tool-is-40-years-old-can-it-be-improved/&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 1, position: 1, location: questionpage })">This developer tool is 40 years old: can it be improved?</a>
            </div>
        </li>
                        <li class="s-sidebarwidget--header">
                            Featured on Meta
                        </li>
        <li class="s-sidebarwidget--item d-flex px16">
            <div class="flex--item1 fl-shrink0">
<div class="favicon favicon-stackexchangemeta" title="Meta Stack Exchange"></div>            </div>
            <div class="flex--item wmn0 ow-break-word">
                <a href="https://meta.stackexchange.com/questions/404724/the-december-2024-community-asks-sprint-has-been-moved-to-march-2025-and-length?cb=1" class="js-gps-track" title="The December 2024 Community Asks Sprint has been moved to March 2025 (and lengthened to 2 weeks to compensate)" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackexchange.com/questions/404724/the-december-2024-community-asks-sprint-has-been-moved-to-march-2025-and-length&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 3, position: 2, location: questionpage })">The December 2024 Community Asks Sprint has been moved to March 2025 (and...</a>
            </div>
        </li>
        <li class="s-sidebarwidget--item d-flex px16">
            <div class="flex--item1 fl-shrink0">
<div class="favicon favicon-stackexchangemeta" title="Meta Stack Exchange"></div>            </div>
            <div class="flex--item wmn0 ow-break-word">
                <a href="https://meta.stackexchange.com/questions/404909/stack-overflow-jobs-is-expanding-to-more-countries?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackexchange.com/questions/404909/stack-overflow-jobs-is-expanding-to-more-countries&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 3, position: 3, location: questionpage })">Stack Overflow Jobs is expanding to more countries</a>
            </div>
        </li>
        </ul>
    </div>


<div class="js-zone-container zone-container-sidebar">
    <div id="dfp-tsb" class="everyonelovesstackoverflow everyoneloves__top-sidebar"></div>
		<div class="js-report-ad-button-container " style="width: 300px"></div>
</div>
<div class="js-zone-container zone-container-sidebar">
    <div id="dfp-msb" class="everyonelovesstackoverflow everyoneloves__mid-sidebar"></div>
		<div class="js-report-ad-button-container " style="width: 300px"></div>
</div>
<div id="hireme"></div>        <div class="module sidebar-linked">
	<h4 id="h-linked">Linked</h4>
	    <div class="linked" data-tracker="lq=1">
            <div class="spacer js-gps-track" data-gps-track="linkedquestion.click({ source_post_id: 14293869, target_question_id: 52551309, position: 0 })">
				<a href="https://stackoverflow.com/q/52551309?lq=1" title="Question score (upvotes - downvotes)">
					<div class="answer-votes  default">1</div>
				</a>
				<a href="https://stackoverflow.com/questions/52551309/how-to-vectorize-a-class-instantiation-to-allow-numpy-arrays-as-input?noredirect=1&amp;lq=1" class="question-hyperlink">How to vectorize a class instantiation to allow NumPy arrays as input?</a>
			</div>
	</div>
</div>


    


        <div class="module sidebar-related">
            <h4 id="h-related">Related</h4>
            <div class="related js-gps-related-questions" data-tracker="rq=3">
                    <div class="spacer" data-question-id="12243891">
                        <a href="https://stackoverflow.com/q/12243891?rq=3" title="Question score (upvotes - downvotes)">
                            <div class="answer-votes answered-accepted default">1</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/12243891/looping-through-a-mutidimentional-array-in-python?rq=3" class="question-hyperlink">Looping through a mutidimentional array in python</a>
                    </div>
                    <div class="spacer" data-question-id="17935524">
                        <a href="https://stackoverflow.com/q/17935524?rq=3" title="Question score (upvotes - downvotes)">
                            <div class="answer-votes answered-accepted default">0</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/17935524/running-through-two-arrays-python?rq=3" class="question-hyperlink">Running through two arrays python</a>
                    </div>
                    <div class="spacer" data-question-id="21804871">
                        <a href="https://stackoverflow.com/q/21804871?rq=3" title="Question score (upvotes - downvotes)">
                            <div class="answer-votes default">1</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/21804871/loop-through-two-multidimensional-arrays?rq=3" class="question-hyperlink">loop through two multidimensional arrays</a>
                    </div>
                    <div class="spacer" data-question-id="40846137">
                        <a href="https://stackoverflow.com/q/40846137?rq=3" title="Question score (upvotes - downvotes)">
                            <div class="answer-votes answered-accepted default">1</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/40846137/iterate-through-2-lists-at-once-in-python?rq=3" class="question-hyperlink">Iterate through 2 lists at once in Python</a>
                    </div>
                    <div class="spacer" data-question-id="48641425">
                        <a href="https://stackoverflow.com/q/48641425?rq=3" title="Question score (upvotes - downvotes)">
                            <div class="answer-votes answered-accepted default">5</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/48641425/going-through-2-lists-with-array-data?rq=3" class="question-hyperlink">Going through 2 lists with array data</a>
                    </div>
                    <div class="spacer" data-question-id="54581654">
                        <a href="https://stackoverflow.com/q/54581654?rq=3" title="Question score (upvotes - downvotes)">
                            <div class="answer-votes answered-accepted default">3</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/54581654/looking-for-an-elegant-way-for-looping-simultaneously-over-two-list-with-differe?rq=3" class="question-hyperlink">Looking for an elegant way for looping simultaneously over two list with different lengths</a>
                    </div>
                    <div class="spacer" data-question-id="54723315">
                        <a href="https://stackoverflow.com/q/54723315?rq=3" title="Question score (upvotes - downvotes)">
                            <div class="answer-votes answered-accepted default">1</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/54723315/how-do-i-loop-through-2-arrays?rq=3" class="question-hyperlink">How do I loop through 2 arrays?</a>
                    </div>
                    <div class="spacer" data-question-id="54907591">
                        <a href="https://stackoverflow.com/q/54907591?rq=3" title="Оценка вопроса (положительные - отрицательные)">
                            <div class="answer-votes default">0</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/54907591/how-to-use-nested-loops-for-iterating-two-arrays-in-python?rq=3" class="question-hyperlink"><ya-tr-span data-index="81-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="how to use nested loops for iterating two arrays in Python?" data-translation="как использовать вложенные циклы для перебора двух массивов в Python?" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">как использовать вложенные циклы для перебора двух массивов в Python?</ya-tr-span></a>
                    </div>
                    <div class="spacer" data-question-id="55383149">
                        <a href="https://stackoverflow.com/q/55383149?rq=3" title="Оценка вопроса (положительные - отрицательные)">
                            <div class="answer-votes answered-accepted default">1</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/55383149/looping-through-two-lists-one-element-at-a-time?rq=3" class="question-hyperlink"><ya-tr-span data-index="82-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Looping through two lists one element at a time" data-translation="Перебор двух списков по одному элементу за раз" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Перебор двух списков по одному элементу за раз</ya-tr-span></a>
                    </div>
                    <div class="spacer" data-question-id="71832602">
                        <a href="https://stackoverflow.com/q/71832602?rq=3" title="Оценка вопроса (положительные - отрицательные)">
                            <div class="answer-votes answered-accepted default">2</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/71832602/quick-way-to-iterate-through-two-arrays-python?rq=3" class="question-hyperlink"><ya-tr-span data-index="83-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Quick way to iterate through two arrays python" data-translation="Быстрый способ перебора двух массивов python" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Быстрый способ перебора двух массивов python</ya-tr-span></a>
                    </div>
            </div>
        </div>
        <script type="text/javascript">
                 $(function() {
                     $(".js-gps-related-questions .spacer").on("click", function () {
                        fireRelatedEvent($(this).index() + 1, $(this).data('question-id'));
                     });

                 function fireRelatedEvent(position, questionId) {
                     StackExchange.using("gps", function() {
                         StackExchange.gps.track('related_questions.click',
                         {
                             position: position,
                             originQuestionId: 14293869,
                             relatedQuestionId: +questionId,
                             location: 'sidebar',
                             source: 'Baseline'
                         });    
                     });
                 }
             });
         </script>


    
    

    <div id="hot-network-questions" class="module tex2jax_ignore">
    <h4>
        <a href="https://stackexchange.com/questions?tab=hot" class="js-gps-track s-link s-link__inherit" data-gps-track="posts_hot_network.click({ item_type:1, location:11 })"><ya-tr-span data-index="84-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Hot Network Questions " data-translation=" Горячие Сетевые Вопросы " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Горячие Сетевые Вопросы  </ya-tr-span></a>
    </h4>
    <ul>
            <li>
                <div class="favicon favicon-rpg" title="Обмен стеком ролевых игр"></div><a href="https://rpg.stackexchange.com/questions/214256/what-do-messy-weapons-do-exactly" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:122 }); posts_hot_network.click({ item_type:2, location:11 })"><ya-tr-span data-index="85-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" What do &quot;messy&quot; weapons do, exactly? " data-translation=" Что именно делает «грязное» оружие? " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Что именно делает «грязное» оружие?  </ya-tr-span></a>

            </li>
            <li>
                <div class="favicon favicon-electronics" title="Замена стека электротехники"></div><a href="https://electronics.stackexchange.com/questions/733956/swr-measurement-what-is-considered-to-be-my-load" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:135 }); posts_hot_network.click({ item_type:2, location:11 })"><ya-tr-span data-index="86-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" SWR measurement: what is considered to be my Load? " data-translation=" Измерение КСВ: что считается моей нагрузкой? " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Измерение КСВ: что считается моей нагрузкой?  </ya-tr-span></a>

            </li>
            <li>
                <div class="favicon favicon-electronics" title="Замена стека электротехники"></div><a href="https://electronics.stackexchange.com/questions/733963/is-there-a-relation-between-sample-hold-capacitor-value-and-system-clock-speed" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:135 }); posts_hot_network.click({ item_type:2, location:11 })"><ya-tr-span data-index="87-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Is there a relation between sample &amp; hold capacitor value and system clock speed? " data-translation=" Существует ли связь между ёмкостью конденсатора выборки и хранения и тактовой частотой системы? " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Существует ли связь между ёмкостью конденсатора выборки и хранения и тактовой частотой системы?  </ya-tr-span></a>

            </li>
            <li>
                <div class="favicon favicon-stats" title="Перекрестная Проверка"></div><a href="https://stats.stackexchange.com/questions/659067/how-to-account-for-disproportionate-group-sizes" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:65 }); posts_hot_network.click({ item_type:2, location:11 })"><ya-tr-span data-index="88-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" How to account for disproportionate group sizes? " data-translation=" Как учесть непропорциональные размеры группы? " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Как учесть непропорциональные размеры группы?  </ya-tr-span></a>

            </li>
            <li>
                <div class="favicon favicon-unix" title="Обмен стеками Unix и Linux"></div><a href="https://unix.stackexchange.com/questions/788534/tar-having-much-larger-size-than-the-containing-files-can-i-make-it-smaller" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:106 }); posts_hot_network.click({ item_type:2, location:11 })"><ya-tr-span data-index="89-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" tar having much larger size than the containing files, can I make it smaller? " data-translation=" tar имеет гораздо больший размер, чем содержащие его файлы, можно ли сделать его меньше? " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  tar имеет гораздо больший размер, чем содержащие его файлы, можно ли сделать его меньше?  </ya-tr-span></a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-mathematica" title="Обмен стеком Mathematica"></div><a href="https://mathematica.stackexchange.com/questions/309594/more-efficient-way-to-color-code-cycle-permutation-list" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:387 }); posts_hot_network.click({ item_type:2, location:11 })"><ya-tr-span data-index="90-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" More efficient way to color-code cycle permutation list " data-translation=" Более эффективный способ создания списка перестановок циклов цветового кода " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Более эффективный способ создания списка перестановок циклов цветового кода  </ya-tr-span></a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-security" title="Обмен стеком информационной безопасности"></div><a href="https://security.stackexchange.com/questions/279921/best-practices-for-managing-open-source-vulnerabilities-in-enterprise-deployment" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:162 }); posts_hot_network.click({ item_type:2, location:11 })"><ya-tr-span data-index="91-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Best Practices for Managing Open-Source Vulnerabilities in Enterprise Deployments " data-translation=" Рекомендации по управлению уязвимостями с открытым исходным кодом в корпоративных развертываниях " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Рекомендации по управлению уязвимостями с открытым исходным кодом в корпоративных развертываниях  </ya-tr-span></a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-gaming" title="Аркаде"></div><a href="https://gaming.stackexchange.com/questions/410492/how-do-i-get-steam-points" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:41 }); posts_hot_network.click({ item_type:2, location:11 })"><ya-tr-span data-index="92-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" How do I get Steam points? " data-translation=" Как я могу получить баллы Steam? " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Как я могу получить баллы Steam?  </ya-tr-span></a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-academia" title="Академический Обмен стеками"></div><a href="https://academia.stackexchange.com/questions/215683/do-experimental-projects-harm-my-theoretical-profile" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:415 }); posts_hot_network.click({ item_type:2, location:11 })"><ya-tr-span data-index="93-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Do experimental projects harm my theoretical profile? " data-translation=" Вредят ли экспериментальные проекты моему теоретическому профилю? " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Вредят ли экспериментальные проекты моему теоретическому профилю?  </ya-tr-span></a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-astronomy" title="Обмен Астрономическим Стеком"></div><a href="https://astronomy.stackexchange.com/questions/59132/odds-of-hitting-a-star-with-a-laser-shone-in-a-random-direction" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:514 }); posts_hot_network.click({ item_type:2, location:11 })"><ya-tr-span data-index="94-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Odds of hitting a star with a laser shone in a random direction " data-translation=" Вероятность попадания лазера в звезду, направленную в случайном направлении " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Вероятность попадания лазера в звезду, направленную в случайном направлении  </ya-tr-span></a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-physics" title="Обмен стеком физики"></div><a href="https://physics.stackexchange.com/questions/837806/why-does-a-rod-move-faster-when-struck-at-the-center-rather-than-the-edge-despi" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:151 }); posts_hot_network.click({ item_type:2, location:11 })"><ya-tr-span data-index="95-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Why does a rod move faster when struck at the center rather than the edge, despite Newton's second law indicating the same acceleration?&quot; " data-translation=" Почему стержень движется быстрее, если ударить по его центру, а не по краю, несмотря на то, что второй закон Ньютона указывает на то же ускорение? " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Почему стержень движется быстрее, если ударить по его центру, а не по краю, несмотря на то, что второй закон Ньютона указывает на то же ускорение?  </ya-tr-span></a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-tex" title="Обмен стеками TeX - LaTeX"></div><a href="https://tex.stackexchange.com/questions/733354/how-to-simplify-refactor-this-code-even-more" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:85 }); posts_hot_network.click({ item_type:2, location:11 })"><ya-tr-span data-index="96-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" How to simplify/refactor this code even more? " data-translation=" Как еще больше упростить / рефакторинговать этот код? " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Как еще больше упростить / рефакторинговать этот код?  </ya-tr-span></a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-philosophy" title="Философия Обмена стеком"></div><a href="https://philosophy.stackexchange.com/questions/120708/thoughts-and-analogy-in-cognition" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:265 }); posts_hot_network.click({ item_type:2, location:11 })"><ya-tr-span data-index="97-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Thoughts and analogy in cognition " data-translation=" Мысли и аналогии в познании " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Мысли и аналогии в познании  </ya-tr-span></a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-unix" title="Обмен стеками Unix и Linux"></div><a href="https://unix.stackexchange.com/questions/788498/network-activity-halting-at-every-45s" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:106 }); posts_hot_network.click({ item_type:2, location:11 })"><ya-tr-span data-index="98-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Network activity halting at every 45s " data-translation=" Сетевая активность прекращается каждые 45 секунд " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Сетевая активность прекращается каждые 45 секунд  </ya-tr-span></a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-askubuntu" title="Спросите Убунту"></div><a href="https://askubuntu.com/questions/1536093/scp-with-sshpass-does-not-work-with-custom-identity-file-and-custom-port" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:89 }); posts_hot_network.click({ item_type:2, location:11 })"><ya-tr-span data-index="99-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" scp with sshpass does not work (with custom identity file and custom port) " data-translation=" scp с sshpass не работает (с пользовательским файлом идентификации и пользовательским портом) " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  scp с sshpass не работает (с пользовательским файлом идентификации и пользовательским портом)  </ya-tr-span></a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-literature" title="Обмен стеком литературы"></div><a href="https://literature.stackexchange.com/questions/28398/meaning-of-second-line-of-shakespeares-sonnet-66" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:668 }); posts_hot_network.click({ item_type:2, location:11 })"><ya-tr-span data-index="100-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Meaning of Second line of Shakespeare's Sonnet 66 " data-translation=" Значение второй строки сонета Шекспира 66 " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Значение второй строки сонета Шекспира 66  </ya-tr-span></a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-worldbuilding" title="Worldbuilding Stack Exchange"></div><a href="https://worldbuilding.stackexchange.com/questions/263646/permanent-night-on-a-portion-of-a-planet" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:579 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Permanent night on a portion of a planet
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-apple" title="Ask Different"></div><a href="https://apple.stackexchange.com/questions/477543/ping-from-script-launched-by-cron" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:118 }); posts_hot_network.click({ item_type:2, location:11 })">
                    ping from script launched by cron
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-superuser" title="Super User"></div><a href="https://superuser.com/questions/1866969/why-did-my-linux-ssd-start-to-have-significantly-slow-write-speed-what-can-be-d" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:3 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Why did my Linux SSD start to have significantly slow write speed? What can be done to improve the write speed?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-hermeneutics" title="Biblical Hermeneutics Stack Exchange"></div><a href="https://hermeneutics.stackexchange.com/questions/99996/in-daniel-8-12-how-can-the-messiah-and-michael-both-be-our-prince" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:320 }); posts_hot_network.click({ item_type:2, location:11 })">
                    In Daniel 8-12, how can the Messiah and Michael both be our Prince?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-quantumcomputing" title="Quantum Computing Stack Exchange"></div><a href="https://quantumcomputing.stackexchange.com/questions/40727/what-is-expected-behavior-of-cz-in-the-hadamard-basis" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:694 }); posts_hot_network.click({ item_type:2, location:11 })">
                    What is expected behavior of CZ in the Hadamard basis?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-bicycles" title="Bicycles Stack Exchange"></div><a href="https://bicycles.stackexchange.com/questions/96011/bolt-of-rear-derailleur-rounded-out-and-broke-off-repair-wire-thread" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:126 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Bolt of rear derailleur rounded out and broke off - repair wire thread
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-buddhism" title="Buddhism Stack Exchange"></div><a href="https://buddhism.stackexchange.com/questions/51719/mastering-the-inner-game-of-bullying-harrassment" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:565 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Mastering the inner game of bullying/harrassment
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-stats" title="Cross Validated"></div><a href="https://stats.stackexchange.com/questions/659043/exploiting-mse-for-fast-search" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:65 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Exploiting MSE for fast search
                </a>

            </li>
    </ul>

        
</div>

                <div id="feed-link" class="js-feed-link">
        <a href="/feeds/question/14293869" title="Feed of this question and its answers">
            <svg aria-hidden="true" class="fc-orange-400 svg-icon iconRss" width="18" height="18" viewBox="0 0 18 18"><path d="M3 1a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2zm0 1.5c6.9 0 12.5 5.6 12.5 12.5H13C13 9.55 8.45 5 3 5zm0 5c4.09 0 7.5 3.41 7.5 7.5H8c0-2.72-2.28-5-5-5zm0 5c1.36 0 2.5 1.14 2.5 2.5H3z"></path></svg>
            Question feed
        </a>
    </div>
    <aside class="s-modal js-feed-link-modal" tabindex="-1" role="dialog" aria-labelledby="feed-modal-title" aria-describedby="feed-modal-description" aria-hidden="true">
        <div class="s-modal--dialog js-modal-dialog wmx4" role="document" data-controller="se-draggable">
            <h1 class="s-modal--header fw-bold js-first-tabbable c-move" id="feed-modal-title" data-se-draggable-target="handle" tabindex="0"><ya-tr-span data-index="76-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Subscribe to RSS " data-translation=" Подписка на RSS " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Подписка на RSS  </ya-tr-span></h1>
            <div class="d-flex gs4 gsy fd-column">
                <div class="flex--item">
                    <label class="d-block s-label c-default" for="feed-url"><ya-tr-span data-index="77-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value=" Question feed " data-translation=" Подача вопросов " data-ch="0" data-type="trSpan" style="visibility: inherit !important;">  Подача вопросов  </ya-tr-span><p class="s-description mt2" id="feed-modal-description"><ya-tr-span data-index="78-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="To subscribe to this RSS feed, copy and paste this URL into your RSS reader." data-translation="Чтобы подписаться на эту RSS-ленту, скопируйте и вставьте этот URL в программу для чтения RSS." data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Чтобы подписаться на эту RSS-ленту, скопируйте и вставьте этот URL в программу для чтения RSS.</ya-tr-span></p>
                    </label>
                </div>
                <div class="d-flex ps-relative">
                    <input class="s-input" type="text" name="feed-url" id="feed-url" readonly="readonly" value="https://stackoverflow.com/feeds/question/14293869">
                    <svg aria-hidden="true" class="s-input-icon fc-orange-400 svg-icon iconRss" width="18" height="18" viewBox="0 0 18 18"><path d="M3 1a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2zm0 1.5c6.9 0 12.5 5.6 12.5 12.5H13C13 9.55 8.45 5 3 5zm0 5c4.09 0 7.5 3.41 7.5 7.5H8c0-2.72-2.28-5-5-5zm0 5c1.36 0 2.5 1.14 2.5 2.5H3z"></path></svg>
                </div>
            </div>
            <a class="s-modal--close s-btn s-btn__muted js-modal-close js-last-tabbable" href="#" aria-label="Закрыть">
                <svg aria-hidden="true" class="svg-icon iconClearSm" width="14" height="14" viewBox="0 0 14 14"><path d="M12 3.41 10.59 2 7 5.59 3.41 2 2 3.41 5.59 7 2 10.59 3.41 12 7 8.41 10.59 12 12 10.59 8.41 7z"></path></svg>
            </a>
        </div>
    </aside>

</div>

    </div>
<script>StackExchange.ready(function(){$.get('/posts/14293869/ivc/03e5?prg=1e4ff1dc-df73-4bf2-ab96-1fc7beda2128');});</script>
<noscript><div><img src="/posts/14293869/ivc/03e5?prg=1e4ff1dc-df73-4bf2-ab96-1fc7beda2128" class="dno" alt="" width="0" height="0"></div></noscript><div style="display:none" id="js-codeblock-lang">lang-py</div></div>


<script>console.error(`Unable to load nonexistent manifest entry 'recent-posts'. Check that your file path is correct.`)</script>

                        


        </div>
    </div>

    

        
    <script type="text/javascript">
    var cam = cam || { opt: {} };
    var clcGamLoaderOptions = cam || { opt: {} };
    var opt = clcGamLoaderOptions.opt;

    opt.omni = 'BwoLCOqXxfSestE9EAUY7bboBiACKAI6CHxweXRob258QAFIAVoSCQvD0_GeTdZMEaLmMUiGARoTzzqeqg7szH8ipQ';
    opt.refresh = !1;
    opt.refreshInterval = 90;
    opt.sf = !0;
    opt.hb = !1;
    opt.ll = !0;
    opt.tlb_position = 0;
    opt.personalization_consent = !0;
    opt.targeting_consent = !0;
    opt.performance_consent = !0;

    opt.targeting = {Registered:['false'],Reputation:['new'],'so-tag':['python'],'tag-reportable':['python'],'so_tag':['python'],NumberOfAnswers:['5'],cf_bot_score:'2 - 29'};
    opt.adReportEnabled = !0;
    opt.adReportUrl = '/ads/report-ad';
    opt.adReportText = 'Report this ad';
	opt.adReportFileTypeErrorMessage = 'Please select a PNG or JPG file.';
    opt.adReportFileSizeErrorMessage = 'The file must be under 2 MiB.';
	opt.adReportErrorText = 'Error uploading ad report.';
	opt.adReportThanksText = 'Thanks for your feedback. We’ll review this against our code of conduct and take action if necessary.';
    opt.adReportLoginExpiredMessage = 'Your login session has expired, please login and try again.';
    opt.adReportLoginErrorMessage = 'An error occurred when loading the report form - please try again';
	opt.adReportModalClass = 'js-ad-report';
    opt.countryCode = 'RU';
    opt.qualtricsSurveyData = '{"isRegistered":"False","repBucket":"new","referrer":"https%3a%2f%2fstackoverflow.com%2fquestions%2f14293869%2fwhat-is-the-pythonic-way-to-loop-through-two-arrays-at-the-same-time","accountAge":"0"}';

        opt.brandSurveyEnabled = true;
            opt.brandSurveySettings = [{"brandId":7,"lineItemIds":[6170355049,6170355058,6170355244,6168829383,6170355787,6170355799,6168829803,6170356261,6170356282,6170984786,6170985065,6168833181,6170358871,6170360326,6170360578,6168834204,6170361016,6170986253,6377604184,6378262502,6378262511,6377604211,6377604223,6377604700,6318450889,6318453241,6318453259,6318453310],"mode":"Collect"},{"brandId":8,"lineItemIds":[6389119380,6389119404,6389119347],"mode":"Collect"},{"brandId":9,"lineItemIds":[6695878301,6695879039,6695879168,6695879174,6695879186],"mode":"Collect"},{"brandId":10,"lineItemIds":[6456294147,6456294228,6456294381,6456294396,6456294633,6456294714,6456294906,6458534116,6458539435,6458540062,6459217607,6459218636,6459219038,6459219551,6458539678,6458539864,6458539918,6459217100,6459218396,6459218846,6459219500,6459219983,6456293469,6456293664,6456293949,6459216860,6459217889,6459217904,6459218117,6459218306],"mode":"Collect"}];
    opt.perRequestGuid = '1e4ff1dc-df73-4bf2-ab96-1fc7beda2128';
    opt.responseHash = 'eSWWG3/uc/V37PCLFDMAWdi&#x2B;m3wUM/5QlVOWuRPnZPo=';


    opt.targeting.TargetingConsent = ['True'];
    opt.allowAccountTargetingForThisRequest = !1;

    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('dfptestads')) {
        const dfptestads = urlParams.get('dfptestads');
        opt.targeting.DfpTestAds = dfptestads;
    }
</script>
<script>;(()=>{"use strict";var __webpack_modules__={23:(e,t,s)=>{s.d(t,{Z7:()=>c,eq:()=>l,kG:()=>d});const n="248424177",o=(a=location.pathname,/^\/tags\//.test(a)||/^\/questions\/tagged\//.test(a)?"tag-pages":/^\/discussions\//.test(a)||/^\/beta\/discussions/.test(a)?"discussions":/^\/$/.test(a)||/^\/home/.test(a)?"home-page":/^\/jobs$/.test(a)||/^\/jobs\//.test(a)?"jobs":"question-pages");var a;let i=location.hostname;const r={slots:{lb:[[728,90]],mlb:[[728,90]],smlb:[[728,90]],bmlb:[[728,90]],sb:e=>"dfp-tsb"===e?[[300,250],[300,600]]:[[300,250]],"tag-sponsorship":[[730,135]],"mobile-below-question":[[320,50],[300,250]],msb:[[300,250],[300,600]],"talent-conversion-tracking":[[1,1]],"site-sponsorship":[[230,60]]},ids:{"dfp-tlb":"lb","dfp-mlb":"mlb","dfp-smlb":"smlb","dfp-bmlb":"bmlb","dfp-tsb":"sb","dfp-isb":"sb","dfp-tag":"tag-sponsorship","dfp-msb":"msb","dfp-sspon":"site-sponsorship","dfp-m-aq":"mobile-below-question"},idsToExcludeFromAdReports:["dfp-sspon"]};function d(){return Object.keys(r.ids)}function l(e){return r.idsToExcludeFromAdReports.indexOf(e)<0}function c(e){var t=e.split("_")[0];const s=r.ids[t];let a=r.slots[s];return"function"==typeof a&&(a=a(t)),{path:`/${n}/${i}/${s}/${o}`,sizes:a,zone:s}}},865:(e,t,s)=>{function n(e){return"string"==typeof e?document.getElementById(e):e}function o(e){return!!(e=n(e))&&"none"===getComputedStyle(e).display}function a(e){return!o(e)}function i(e){return!!e}function r(e){return/^\s*$/.test(n(e).innerHTML)}function d(e){const{style:t}=e;t.height=t.maxHeight=t.minHeight="auto",t.display="none"}function l(e){const{style:t}=e;t.height=t.maxHeight=t.minHeight="auto",t.display="none",[].forEach.call(e.children,l)}function c(e){const{style:t}=e;t.height=t.maxHeight=t.minHeight="auto",t.removeProperty("display")}function g(e){const t=document.createElement("script");t.src=e,document.body.appendChild(t)}function p(e){return s=e,(t=[]).push=function(e){return s(),delete this.push,this.push(e)},t;var t,s}function h(e){let t="function"==typeof HTMLTemplateElement;var s=document.createElement(t?"template":"div");return e=e.trim(),s.innerHTML=e,t?s.content.firstChild:s.firstChild}s.d(t,{$Z:()=>c,Bv:()=>h,Gx:()=>g,Nj:()=>n,QZ:()=>p,cf:()=>d,pn:()=>a,wo:()=>l,xb:()=>r,xj:()=>o,yb:()=>i})},763:(__unused_webpack_module,__webpack_exports__,__webpack_require__)=>{__webpack_require__.d(__webpack_exports__,{t:()=>AdReports});var _common_helper__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(865),_console__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(276),_ad_units__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(23);class AdReports{constructor(e,t){if(this.googletag=e,this.cam=t,this.allowedFileTypes=["image/png","image/jpg","image/jpeg"],this.ignoreValidation=!1,_console__WEBPACK_IMPORTED_MODULE_1__.cM("Ad reporting init"),this.cam=t,this.callOnButtonClick=e=>this.onButtonClick(e),this.googletag.pubads().addEventListener("slotRenderEnded",e=>this.handleSlotRendered(e)),Array.isArray(t.slotsRenderedEvents)){_console__WEBPACK_IMPORTED_MODULE_1__.cM("Adding report button to "+t.slotsRenderedEvents.length+" events that have transpired");for(var s=0;s<t.slotsRenderedEvents.length;s++)this.handleSlotRendered(t.slotsRenderedEvents[s])}}handleSlotRendered(e){if(e&&e.slot&&!e.isEmpty&&(e.creativeId||e.lineItemId||!e.isEmpty)){var t=e.slot.getSlotElementId();if(t){var s=document.getElementById(t);if(s)if((0,_ad_units__WEBPACK_IMPORTED_MODULE_0__.eq)(t)){var n=s?.closest(".js-zone-container")?.querySelector(".js-report-ad-button-container");n?(n.innerHTML="",n.append(this.createButton(e)),n.style.height="24px",_console__WEBPACK_IMPORTED_MODULE_1__.cM("Added report button to the bottom of "+t)):_console__WEBPACK_IMPORTED_MODULE_1__.cM("Ad report button not found, may be intentional, element: "+t)}else _console__WEBPACK_IMPORTED_MODULE_1__.cM("Not adding report button to the bottom of "+t+": shouldHaveReportButton = false");else _console__WEBPACK_IMPORTED_MODULE_1__.cM("Not adding report button to the bottom of "+t+": resolved invalid adUnit element")}else _console__WEBPACK_IMPORTED_MODULE_1__.cM("Not adding report button to the bottom of element: invalid adUnitElementId")}else _console__WEBPACK_IMPORTED_MODULE_1__.cM("Not adding report button to the bottom of element: invalid SlotRenderEndedEvent")}async onButtonClick(e){e.preventDefault();let t=e.target;const s=t.dataset.modalUrl,n=t.dataset.googleEventData;return await this.loadModal(s,t,n),!1}createButton(e){let t=document.createElement("button");var s=JSON.stringify(e);return t.dataset.googleEventData=s,t.dataset.modalUrl=this.cam.opt.adReportUrl,t.dataset.adUnit=e.slot.getSlotElementId(),t.classList.add("js-report-ad","s-btn","s-btn__link","fs-fine","mt2","float-right"),t.append(document.createTextNode(this.cam.opt.adReportText)),t.removeEventListener("click",this.callOnButtonClick),t.addEventListener("click",this.callOnButtonClick),t}async loadModal(url,$link,googleEventData){try{await window.StackExchange.helpers.loadModal(url,{returnElements:window.$($link)}),this.initForm(googleEventData)}catch(e){var message="",response=e.responseText?eval(`(${e.responseText})`):null;message=response&&response.isLoggedOut?this.cam.opt.adReportLoginExpiredMessage:this.cam.opt.adReportLoginErrorMessage,window.StackExchange.helpers.showToast(message,{type:"danger"})}}removeModal(){window.StackExchange.helpers.closePopups(document.querySelectorAll("."+this.cam.opt.adReportModalClass),"dismiss")}initForm(e,t=!1){this.ignoreValidation=t,this.$form=document.querySelector(".js-ad-report-form"),this.$googleEventData=this.$form.querySelector(".js-json-data"),this.$adReportReasons=this.$form.querySelectorAll(".js-ad-report-reason"),this.$adReportReasonOther=this.$form.querySelector(".js-ad-report-reason-other"),this.$fileUploaderInput=this.$form.querySelector(".js-file-uploader-input"),this.$imageUploader=this.$form.querySelector(".js-image-uploader"),this.$clearImageUpload=this.$form.querySelector(".js-clear-image-upload"),this.$imageUploaderText=this.$form.querySelector(".js-image-uploader-text"),this.$imageUploaderPreview=this.$form.querySelector(".js-image-uploader-preview"),this.$fileErrorMessage=this.$form.querySelector(".js-file-error");const s=this.$form.querySelector(".js-drag-drop-enabled"),n=this.$form.querySelector(".js-drag-drop-disabled");this.$googleEventData.value=e,this.$adReportReasons.forEach((e,t)=>e.addEventListener("change",e=>{this.$adReportReasonOther.classList.toggle("d-none","3"!==e.target.value)})),this.$fileUploaderInput.addEventListener("change",()=>{this.validateFileInput()&&this.updateImagePreview(this.$fileUploaderInput.files)}),this.$clearImageUpload.addEventListener("click",e=>{e.preventDefault(),this.clearImageUpload()});try{this.$fileUploaderInput[0].value="",this.$imageUploader.addEventListener("dragenter dragover dragleave drop",this.preventDefaults),this.$imageUploader.addEventListener("dragenter dragover",this.handleDragStart),this.$imageUploader.addEventListener("dragleave drop",this.handleDragEnd),this.$imageUploader.addEventListener("drop",this.handleDrop)}catch(e){s.classList.add("d-none"),n.classList.remove("d-none")}this.$form.removeEventListener("",this.handleDragEnd),this.$form.addEventListener("submit",async e=>(e.preventDefault(),this.submitForm(),!1))}clearImageUpload(){this.$fileUploaderInput.value="",this.$imageUploaderPreview.setAttribute("src",""),this.$imageUploaderPreview.classList.add("d-none"),this.$clearImageUpload.classList.add("d-none"),this.$imageUploaderText.classList.remove("d-none"),this.$imageUploader.classList.add("p16","ba","bas-dashed","bc-black-100")}preventDefaults(e){e.preventDefault(),e.stopPropagation()}handleDragStart(e){this.$imageUploader.classList.remove("bas-dashed"),this.$imageUploader.classList.add("bas-solid","bc-black-100")}handleDragEnd(e){this.$imageUploader.classList.remove("bas-solid","bc-black-100"),this.$imageUploader.classList.add("bas-dashed")}handleDrop(e){var t=e.originalEvent.dataTransfer.files;FileReader&&t&&1===t.length&&(this.$fileUploaderInput.files=t,this.validateFileInput()&&this.updateImagePreview(t))}setError(e){this.$fileErrorMessage.parentElement.classList.toggle("has-error",e)}updateImagePreview(e){this.$imageUploader.classList.remove("p16","ba","bas-dashed","bc-black-100"),this.$clearImageUpload.classList.remove("d-none"),this.$imageUploaderText.classList.add("d-none");var t=new FileReader;t.onload=e=>{null!=e.target&&(this.$imageUploaderPreview.setAttribute("src",e.target.result),this.$imageUploaderPreview.classList.remove("d-none"))},t.readAsDataURL(e[0])}validateFileInput(){if(this.ignoreValidation)return!0;const e=this.cam.opt.adReportFileTypeErrorMessage,t=this.cam.opt.adReportFileSizeErrorMessage;if(null==this.$fileUploaderInput.files)return!1;var s=this.$fileUploaderInput.files[0];return null==s?(this.setError(!0),!1):this.allowedFileTypes.indexOf(s.type)<0?(this.$fileErrorMessage.textContent=e,this.$fileErrorMessage.classList.remove("d-none"),this.setError(!0),!1):s.size>2097152?(this.$fileErrorMessage.textContent=t,this.$fileErrorMessage.classList.remove("d-none"),this.setError(!0),!1):(this.$fileErrorMessage.classList.add("d-none"),this.setError(!1),!0)}async gatherDiagnosticInfo(){return{BrowserVersion:await this.getBrowserVersion()}}getElementSource(e){return e.outerHTML}getNestedIFrameElement(e){var t=e.querySelector("iframe");return t.contentDocument?t.contentDocument.documentElement:t.contentWindow.document.documentElement}async getBrowserVersion(){return await navigator.userAgentData.getHighEntropyValues(["fullVersionList"]).then(e=>JSON.stringify(e.fullVersionList))}async submitForm(){if(!this.validateFileInput())return!1;this.$form.querySelector("[type=submit]").setAttribute("disabled","true");var e=JSON.parse(this.$googleEventData.value||"{}");e.Reason=parseInt(this.$form.querySelector(".js-ad-report-reason:checked").value,10),e.Description=this.$adReportReasonOther.value,this.$googleEventData.value=JSON.stringify(e);var t=new FormData(this.$form);if("1"===t.get("shareDiagnosticInfo")){var s=await this.gatherDiagnosticInfo();Object.keys(s).forEach(e=>t.append(e,s[e]))}try{const e=await window.fetch(this.$form.getAttribute("action"),{method:this.$form.getAttribute("method"),body:t,cache:"no-cache"}),s=e.headers.get("content-type")||"",o=await e.text();if(!e.ok)throw new Error("response not valid");if(0===s.indexOf("text/html")){var n=(0,_common_helper__WEBPACK_IMPORTED_MODULE_2__.Bv)(o);const e=n?n.querySelector(".js-modal-content"):null;if(_console__WEBPACK_IMPORTED_MODULE_1__.cM("$popupContent"),_console__WEBPACK_IMPORTED_MODULE_1__.cM(e),!e)throw new Error(`Could not find .js-modal-content in response from ${this.$form.getAttribute("action")}`);document.querySelector(".js-modal-content").replaceWith(e)}else window.StackExchange.helpers.showToast(this.cam.opt.adReportThanksText,{type:"success"}),this.removeModal()}catch(e){window.StackExchange.helpers.showToast(this.cam.opt.adReportErrorText,{type:"danger"})}finally{let e=this.$form.querySelector("[type=submit]");e&&e.removeAttribute("disabled")}}}},276:(e,t,s)=>{function n(...e){}function o(...e){}s.d(t,{cM:()=>n,vU:()=>o})}},__webpack_module_cache__={};function __webpack_require__(e){var t=__webpack_module_cache__[e];if(void 0!==t)return t.exports;var s=__webpack_module_cache__[e]={exports:{}};return __webpack_modules__[e](s,s.exports,__webpack_require__),s.exports}__webpack_require__.d=(e,t)=>{for(var s in t)__webpack_require__.o(t,s)&&!__webpack_require__.o(e,s)&&Object.defineProperty(e,s,{enumerable:!0,get:t[s]})},__webpack_require__.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t);var __webpack_exports__={};(()=>{var e=__webpack_require__(276),t=(e=>(e[e.Above=0]="Above",e[e.Below=1]="Below",e))(t||{});const s=Object.assign({},{"lib":"https://clc.stackoverflow.com/Content/bundles/js/gam_loader_script.bundle.741.25e3e63be9a306287d9f.js?v=d5f908ccaade","style":null,"u":null,"wa":true,"kt":2000,"tto":true,"h":"clc.stackoverflow.com","allowed":"^(((talent\\.)?stackoverflow)|(blog\\.codinghorror)|(.*\\.googlesyndication)|(serverfault|askubuntu|superuser)|([^\\.]+\\.stackexchange))\\.com$","wv":true,"al":false,"abd":true,"cpa_liid":[5882654614],"cpa_cid":[138377597667],"dp":false,"tgt_to":1000,"tgt_u":"https://clc.stackoverflow.com/get-user-acct-tgt","tgt_e":true,"tgt_p":100,"dv_enabled":false});var n=__webpack_require__(23),o=__webpack_require__(865),a=__webpack_require__(763);class i{constructor(t,s){this.googletag=t,this.interval=s,e.cM("Ad refresh init. interval: "+s),this.googletag.pubads().addEventListener("impressionViewable",e=>this.onImpressionViewable(e)),e.cM("done enabling ad refresh")}onImpressionViewable(t){var s=t.slot;e.cM("ad refresh - slot "+s.getSlotElementId()+" is viewable, initializing refresh"),this.scheduleRefresh(s)}scheduleRefresh(e){setTimeout(()=>this.refreshAdSlot(e),1e3*this.interval)}static refreshMyAd(t,s){let n=t.pubads().getSlots().find(e=>e.getSlotElementId()===s);n&&(e.cM("refreshMyAd - refreshing ad slot "+s),t.pubads().refresh([n]))}static removeMyAd(t,s){let n=t.pubads().getSlots().find(e=>e.getSlotElementId()===s);n&&(e.cM("removeMyAd - destroying ad slot "+s),t.destroySlots([n]))}refreshAdSlot(t){var s=t.getSlotElementId();this.isElementVisibleInBrowser(s)?(e.cM("refreshing ad slot "+s),googletag.pubads().refresh([t])):(e.cM("refresh skipped this time; ad slot not viewable:"+s),this.scheduleRefresh(t))}isElementVisibleInBrowser(e){var t=document.getElementById(e);if(null!==t){var s=t.getBoundingClientRect();if(s.top>=0&&s.left>=0&&s.bottom<=(window.innerHeight||document.documentElement.clientHeight)&&s.right<=(window.innerWidth||document.documentElement.clientWidth))return!0}return!1}}var r=(e=>(e.Off="Off",e.PreSurvey="PreSurvey",e.Collect="Collect",e.PostSurvey="PostSurvey",e))(r||{});class d{constructor(e,t){this.lineItemImpressions=[],this.surveysIdsCompleted=[],this.lineItemImpressions=e,this.surveysIdsCompleted=t}addImpression(e,t){let s={brandId:e,lineItemId:t,timestamp:new Date};this.lineItemImpressions.push(s)}addBrandSurveyCompleted(e){-1===this.surveysIdsCompleted.indexOf(e)&&this.surveysIdsCompleted.push(e)}getTotalBrandImpressions(){let e=new Map;for(let t of this.lineItemImpressions)if(e.has(t.brandId)){let s=e.get(t.brandId);e.set(t.brandId,s+1)}else e.set(t.brandId,1);return e}getBrandLineItemImpressions(e){let t={};for(let s of this.lineItemImpressions)if(s.brandId==e)if(void 0!==t[s.lineItemId]){let e=t[s.lineItemId];t[s.lineItemId]=e+1}else t[s.lineItemId]=1;return t}}class l{constructor(){this.surveyEngagementLocalStorageKey="clc-survey-engagement"}getBrandSurveyEngagement(){let e=localStorage.getItem(this.surveyEngagementLocalStorageKey);if(null===e)return new d([],[]);let t=JSON.parse(e);return new d(t.lineItemImpressions,t.surveysIdsCompleted)}saveBrandSurveyEngagement(e){let t=JSON.stringify(e);localStorage.setItem(this.surveyEngagementLocalStorageKey,t)}}class c{constructor(){this.surveyRepository=new l}getBrandSurveyEngagement(){return this.surveyRepository.getBrandSurveyEngagement()}recordImpression(e,t){let s=this.getBrandSurveyEngagement();s.addImpression(e,t),this.surveyRepository.saveBrandSurveyEngagement(s)}recordBrandSurveyCompleted(e){let t=this.getBrandSurveyEngagement();t.addBrandSurveyCompleted(e),this.surveyRepository.saveBrandSurveyEngagement(t)}}class g{constructor(t,s){this.googletag=t,this.brandSettings=s,this.brandSlotMap=new Map,this.brandSurveyEngagementService=new c,e.cM("Brand Survey init: "+JSON.stringify(s)),void 0!==s?(this.googletag.pubads().addEventListener("slotRenderEnded",e=>this.handleSlotRendered(e)),this.googletag.pubads().addEventListener("impressionViewable",e=>this.onImpressionViewable(e)),e.cM("done enabling Brand Survey")):e.cM("Brand Survey init: brandSettings is undefined, not initializing")}handleSlotRendered(t){e.cM("Brand Survey - slot rendered - slot:"+JSON.stringify(t.slot.getSlotElementId())+" lineItem: "+t.lineItemId);let s=this.findItemWithId(t.lineItemId);if(null===s||s.mode!==r.Collect)this.brandSlotMap.delete(t.slot.getSlotElementId());else{let e={brandId:s.brandId,lineItemId:t.lineItemId};this.brandSlotMap.set(t.slot.getSlotElementId(),e)}}onImpressionViewable(t){let s=t.slot;if(e.cM("ad - Brand Survey - impression viewable.  Details: "+JSON.stringify(s.getSlotElementId())),e.cM("ad - Brand Survey - slot "+s.getSlotElementId()+" is viewable"),this.brandSlotMap.has(s.getSlotElementId())){let t=this.brandSlotMap.get(s.getSlotElementId());e.cM("Brand Survey - brand "+t.brandId+" is viewable"),this.recordImpression(this.brandSlotMap.get(s.getSlotElementId()))}}recordImpression(t){e.cM("ad - Brand Survey - recording impression for brand "+t.brandId),this.brandSurveyEngagementService.recordImpression(t.brandId,t.lineItemId)}findItemWithId(t){return e.cM("brand settings: "+JSON.stringify(this.brandSettings)),this.brandSettings.find(e=>e.lineItemIds.includes(t))||null}}const p="response-brand-survey-submit|",h="request-brand-survey-metadata|",m="record-metric-on-server|",u="request-dsp-tags",f="response-dsp-tags|";class v{static refreshAdIfBrandSurveyIsDuplicated(e,t,s){if(this.alreadyCompletedThisBrandSurvey(t)){var n=document.getElementById(s).closest(".js-zone-container");i.removeMyAd(e,s),n&&n.remove()}}static alreadyCompletedThisBrandSurvey(e){return(new c).getBrandSurveyEngagement().surveysIdsCompleted.includes(e)}}window.cam=new class{constructor(t=null){if(this.gptImported=!1,this.slotsRenderedEvents=[],this.collapsed={},e.cM("constructor"),this.clc_options=s,window.clcGamLoaderOptions)Object.assign(this,window.clcGamLoaderOptions);else if(void 0===this.opt){let e=window.opt;e&&(this.opt=e)}}init(){if(e.cM("init"),void 0===this.opt)throw new Error("opt not set, required by GAM Loader");e.cM("init brand survey service"),this.getUserMetaPromise=this.getUserMeta(),e.cM("setup message handler"),window.addEventListener("message",e=>{this.onmessage(e)})}handleSlotRenderedNoAdReport(){if(googletag.pubads().addEventListener("slotRenderEnded",e=>this.applyExtraMarginBottom(e)),Array.isArray(this.slotsRenderedEvents))for(var e=0;e<this.slotsRenderedEvents.length;e++)this.applyExtraMarginBottom(this.slotsRenderedEvents[e])}onmessage(t){let s="omni";if(t.data&&("string"==typeof t.data||t.data instanceof String))if(0===t.data.indexOf("get-omni-")){e.cM("Recevied get-omni message, sending back omni");var n=t.source,a=this.opt.omni,i="string"==typeof a?a:"";n.postMessage([s,i,this.opt.perRequestGuid].join("|"),"*")}else if(0===t.data.indexOf("collapse-")){e.cM("Recevied collapse message, collapse ad iframe"),e.cM(t);for(var r=t.source.window,d=document.getElementsByTagName("IFRAME"),l=0;l<d.length;l++){var g=d[l];if(g.contentWindow==r)return void(0,o.wo)(g.parentElement.parentElement.parentElement)}}else if(0===t.data.indexOf("resize|")){e.cM("Recevied resize message, resize ad iframe"),e.cM(t);let s=this._getFrameByEvent(t),n=t.data.indexOf("|")+1,o=t.data.slice(n),a=parseFloat(o)+.5;e.cM("New iframe height "+a),s.height=a.toString(),s.parentElement.style.height=a.toString()+"px"}else if(0===t.data.indexOf("getmarkup|")){let s=t.data.indexOf("|")+1,n=t.data.slice(s);e.cM("Recevied get markup message: "+n);let o=this._getFrameByEvent(t).closest(".everyonelovesstackoverflow");const a=document.createElement("script");a.dataset.adZoneId=o.id,a.src=n,document.body.appendChild(a)}else if(0===t.data.indexOf("window-location|")){let s=t.data.indexOf("|")+1,n=t.data.slice(s);e.cM("Recevied window location message: "+n),n.startsWith("/")||(n="/"+n),window.open(window.location.protocol+"//"+window.location.host+n,"_blank")}else if(0===t.data.indexOf("request-brand-survey-submit|")){let s=t.data.split("|"),n=s[1],o=s[2],a=s[3],i=JSON.parse(a);e.cM(n),e.cM(o),e.cM(a),e.cM("Received brand survey "+n+" response message: "+o);var _=new FormData;for(var b in i)_.append(b,i[b]);let r=this._getFrameByEvent(t);if(v.alreadyCompletedThisBrandSurvey(+n))return e.cM("Already completed this brand survey.  Not submitting duplicate to server."),void r.contentWindow.postMessage("response-brand-survey-submit-duplicate|","*");e.cM("Send the brand survey to the server"),fetch(o,{method:"POST",body:_}).then(e=>e.json()).then(e=>r.contentWindow.postMessage({messageType:p},"*")).catch(e=>r.contentWindow.postMessage({messageType:p},"*"))}else if(0===t.data.indexOf("brand-survey-completed-store|")){let s=t.data.split("|"),n=(s[1],s[2]);if(e.cM("Received brand survey completed store message for survey ID "+n),v.alreadyCompletedThisBrandSurvey(+n))return void e.cM("Already completed this brand survey.  Not recording duplicate locally.");e.cM("Record brand survey completion locally"),(new c).recordBrandSurveyCompleted(+n)}else if(0===t.data.indexOf(h)){let s=t.data.split("|"),n=s[1],o=s[2];e.cM("Received message: "+h+" with Brand Survey ID "+o);let a=(new c).getBrandSurveyEngagement().getBrandLineItemImpressions(+n),i=JSON.stringify(a),r=this._getFrameByEvent(t);e.cM("sending impression data: "+i),r.contentWindow.postMessage("response-brand-survey-metadata|"+this.opt.responseHash+"|"+this.opt.perRequestGuid+"|"+i+"|"+this.opt.countryCode+"|"+this.opt.qualtricsSurveyData,"*")}else if(0===t.data.indexOf("refresh-if-duplicate-brand-survey|")){let e=t.data.split("|")[1],s=this.getSlotElementIdByEvent(t);v.refreshAdIfBrandSurveyIsDuplicated(googletag,+e,s)}else if(0===t.data.indexOf(m)){e.cM("Received message: "+m+" with args: "+t.data);let s=t.data.split("|"),n=s[1],o=s[2],a=s[3],i=s[4],r=new FormData;r.append("brandSurveyId",a.toString()),r.append("responseHash",this.opt.responseHash),r.append("perRequestGuid",this.opt.perRequestGuid),r.append("questionNumber",n.toString()),r.append("metricType",i.toString()),fetch(o,{method:"POST",body:r}).then(e=>e.ok).catch(t=>{e.cM("SendMetricToServer: Error sending metric to server: "+t)})}else if(0===t.data.indexOf(u)){e.cM("Received message: "+u+" with args: "+t.data);let s=this._getFrameByEvent(t);if(!this.opt.targeting["so-tag"])return void s.contentWindow.postMessage(f,"*");const n=this.opt.targeting["so-tag"].join(",");e.cM("sending targeting tags: "+n),s.contentWindow.postMessage(f+n,"*")}else e.cM("Received unhandled message")}getSlotElementIdByEvent(e){let t=this._getFrameByEvent(e),s=t.parentElement?.parentElement?.id;return s||""}_getFrameByEvent(e){return Array.from(document.getElementsByTagName("iframe")).filter(t=>t.contentWindow===e.source)[0]}classifyZoneIds(e){const t=e.map(o.Nj).filter(o.yb);return{eligible:t.filter(o.xb).filter(o.pn),ineligible:t.filter(o.xj)}}applyExtraMarginBottom(t){if(t&&t.slot&&!t.isEmpty&&(t.creativeId||t.lineItemId||!t.isEmpty)){var s=t.slot.getSlotElementId();if(s){var o=document.getElementById(s);if(o)if((0,n.eq)(s)){var a=o?.closest(".js-zone-container");a.style.marginBottom="24px",e.cM("Applied extra margin to the bottom of "+s)}else e.cM("Not applying extra margin to the bottom of "+s+": shouldHaveReportButton = false");else e.cM("Not applying extra margin to the bottom of "+s+": resolved invalid adUnit element")}else e.cM("Not applying extra margin to the bottom of element: invalid adUnitElementId")}else e.cM("Not applying extra margin to the bottom of element: invalid SlotRenderEndedEvent")}async load(s=(0,n.kG)()){const r=this.opt.tlb_position===t.Above?["dfp-mlb","dfp-smlb"]:["dfp-mlb","dfp-smlb","dfp-tlb"];if(!this.isGptReady())return e.cM("Initializing..."),this.initGpt(),void googletag.cmd.push(()=>this.load(s));this.opt.adReportEnabled?(e.cM("Ad reporting enabled"),this.adReports=new a.t(googletag,this)):(e.cM("Ad reporting not enabled"),this.handleSlotRenderedNoAdReport()),this.opt.refresh?(e.cM("Ad refresh enabled"),this.adRefresh=new i(googletag,this.opt.refreshInterval)):e.cM("Ad refresh not enabled"),this.opt.brandSurveyEnabled&&(e.cM("Brand Survey enabled"),this.brandSurvey=new g(googletag,this.opt.brandSurveySettings)),e.cM("Attempting to load ads into ids: ",s);const{eligible:d,ineligible:l}=this.classifyZoneIds(s);if(this.initDebugPanel(googletag,d.concat(l)),d.forEach(e=>(0,o.cf)(e)),l.forEach(o.wo),0===d.length)return void e.cM("Found no ad ids on page");e.cM("Eligible ids:",d),this.opt.abd&&this.appendAdblockDetector();var c=googletag.pubads().getSlots();if(c){var p=c.filter(e=>s.indexOf(e.getSlotElementId())>=0);googletag.destroySlots(p)}this.opt.sf&&(googletag.pubads().setForceSafeFrame(!0),googletag.pubads().setSafeFrameConfig({allowOverlayExpansion:!0,allowPushExpansion:!0,sandbox:!0})),e.cM("Targeting consent: Checking...");let h=!1,m=!1;void 0!==this.opt.targeting_consent&&(m=!0,e.cM("Targeting consent: Parameter set"),e.cM("Targeting consent: Consent given? ",this.opt.targeting_consent),h=this.opt.targeting_consent),void 0!==this.opt.personalization_consent&&(e.cM("Personalization consent: Parameter set"),e.cM("Personalization consent: Consent given? ",this.opt.personalization_consent),h=h&&this.opt.personalization_consent),h=h&&m,this.setPrivacySettings(h),this.opt.ll||googletag.pubads().enableSingleRequest(),cam.sreEvent||(googletag.pubads().addEventListener("slotRenderEnded",e=>this.onSlotRendered(e)),cam.sreEvent=!0),await this.setTargeting();var u=d.filter(e=>!this.opt.ll||r.indexOf(e.id)<0),f=d.filter(e=>!!this.opt.ll&&r.indexOf(e.id)>=0);e.cM("Up front ids:",u),e.cM("Lazy loaded ids:",f),u.forEach(t=>{e.cM(`Defining ad for element ${t.id}`),this.defineSlot(t.id,googletag),t.setAttribute("data-dfp-zone","true")}),googletag.enableServices(),u.forEach(t=>{e.cM(`Displaying ad for element ${t.id}`),this.clc_options.dv_enabled?window.onDvtagReady(function(){googletag.display(t.id)}):googletag.cmd.push(()=>googletag.display(t.id))}),this.opt.ll&&(e.cM("Enabling lazy loading for GAM"),googletag.pubads().enableLazyLoad({fetchMarginPercent:0,renderMarginPercent:0}),e.cM("Setting up lazy loaded ad units"),f.forEach(t=>{e.cM(`Lazy loading - Defining Slot ${t.id}`),this.defineSlot(t.id,googletag)}),f.forEach(t=>{e.cM(`Lazy loading - Displaying ad for element ${t.id}`),this.clc_options.dv_enabled?window.onDvtagReady(function(){googletag.display(t.id)}):googletag.cmd.push(()=>googletag.display(t.id))}))}setPrivacySettings(e){e||googletag.pubads().setPrivacySettings({nonPersonalizedAds:!0})}async setTargeting(){if(!googletag)throw new Error("googletag not defined");let t=this.opt.targeting;if(!t)throw new Error("Targeting not defined (is "+typeof t+")");Object.keys(t).forEach(s=>{e.cM(`-> targeting - ${s}: ${t[s]}`),googletag.pubads().setTargeting(s,t[s])});let s=!1;if(void 0!==this.opt.targeting_consent&&(s=this.opt.targeting_consent),s){let t=(new c).getBrandSurveyEngagement();if(t.getTotalBrandImpressions().forEach((t,s)=>{e.cM(`-> targeting - BrandImpressions: ${s}: ${t}`),googletag.pubads().setTargeting("brand_"+s.toString()+"_impressions",t.toString())}),t.surveysIdsCompleted.forEach(t=>{e.cM(`-> targeting - SurveysTaken: ${t}`),googletag.pubads().setTargeting("survey_"+t+"_taken","true")}),this.clc_options.tgt_e&&this.getUserMetaPromise){let t=await this.getUserMetaPromise;t&&t.tgt_acct?(e.cM("-> targeting - User Account: "+t.tgt_acct),googletag.pubads().setTargeting("user-acct",t.tgt_acct.company_name),googletag.pubads().setTargeting("user_acct_top",t.tgt_acct.company_name),googletag.pubads().setTargeting("user_industry",t.tgt_acct.industry),googletag.pubads().setTargeting("user_employee_count",t.tgt_acct.employee_range)):e.cM("-> targeting - User Account: Not Found"),t&&Object.prototype.hasOwnProperty.call(t,"is_high_rep_earner")?(e.cM("-> targeting - High Rep Earner: "+t.is_high_rep_earner),googletag.pubads().setTargeting("IsHighRepEarner",t.is_high_rep_earner?"true":"false")):e.cM("-> targeting - High Rep Earner: not found")}if(localStorage){e.cM('Checking local storage for "jobs-last-clicked" key.');let t=localStorage.getItem("jobs-last-clicked")?"true":"false";e.cM(`-> targeting - jobs_clicked: ${t}`),googletag.pubads().setTargeting("jobs_clicked",t)}}}appendAdblockDetector(){const e=document.createElement("div");e.className="adsbox",e.id="clc-abd",e.style.position="absolute",e.style.pointerEvents="none",e.innerHTML="&nbsp;",document.body.appendChild(e)}onSlotRendered(s){try{const i=s.slot.getSlotElementId();let r=[];i||r.push("id=0");const d=document.getElementById(i);if(i&&!d&&r.push("el=0"),0!==r.length)return void this.stalled(r.join("&"));const{path:l,sizes:c,zone:g}=(0,n.Z7)(i);if(this.collapsed[g]&&s.isEmpty)return e.cM(`No line item for the element #${d.id}... collapsing.`),void(0,o.wo)(d);if(this.slotsRenderedEvents.push(s),s.lineItemId||s.creativeId||!s.isEmpty){e.cM(`Rendered ad for element #${d.id} [line item #${s.lineItemId}]`),e.cM(s);var a=d.parentElement;if(a.classList.contains("js-zone-container")){switch((0,o.cf)(a),i){case"dfp-tlb":this.opt.tlb_position===t.Above?a.classList.add("mb8"):a.classList.add("mt16");break;case"dfp-tag":a.classList.add("mb8");break;case"dfp-msb":a.classList.add("mt16");break;case"dfp-mlb":case"dfp-smlb":case"dfp-bmlb":a.classList.add("my8");break;case"dfp-isb":a.classList.add("mt24");break;case"dfp-m-aq":a.classList.add("my12"),a.classList.add("mx-auto")}(0,o.$Z)(a),(0,o.$Z)(d)}else e.cM(`No ad for element #${d.id}, collapsing`),e.cM(s),(0,o.wo)(d)}}catch(t){e.cM("Exception thrown onSlotRendered"),e.cM(t),this.stalled("e=1")}}stalled(e){(new Image).src=`https://${this.clc_options.h}/stalled.gif?${e}`}defineSlot(t,s){"dfp-isb"===t&&(e.cM("-> targeting - Sidebar: Inline"),s.pubads().setTargeting("Sidebar",["Inline"])),"dfp-tsb"===t&&(e.cM("-> targeting - Sidebar: Right"),s.pubads().setTargeting("Sidebar",["Right"]));const{path:o,sizes:a,zone:i}=(0,n.Z7)(t);e.cM(`Defining slot for ${t}: ${o}, sizes: ${JSON.stringify(a)}`),s.defineSlot(o,a,t).addService(s.pubads())}importGptLibrary(){this.gptImported||(this.gptImported=!0,void 0===this.opt.targeting_consent||this.opt.targeting_consent?(0,o.Gx)("https://securepubads.g.doubleclick.net/tag/js/gpt.js"):(0,o.Gx)("https://pagead2.googlesyndication.com/tag/js/gpt.js"))}importDvLibrary(){this.clc_options.dv_enabled&&(e.cM("Adding DoubleVerify library"),(0,o.Gx)("https://pub.doubleverify.com/dvtag/21569774/DV1289064/pub.js"),e.cM("Adding DoubleVerify onDvtagReady handler"),window.onDvtagReady=function(t,s=750){e.cM("DoubleVerify onDvtagReady called"),window.dvtag=window.dvtag||{},dvtag.cmd=dvtag.cmd||[];const n={callback:t,timeout:s,timestamp:(new Date).getTime()};dvtag.cmd.push(function(){dvtag.queueAdRequest(n)}),setTimeout(function(){const e=n.callback;n.callback=null,e&&e()},s)})}isGptReady(){return"undefined"!=typeof googletag&&!!googletag.apiReady}initGpt(){"undefined"==typeof googletag&&(window.googletag={cmd:(0,o.QZ)(()=>{this.importGptLibrary(),this.importDvLibrary()})})}getUserMeta(){if(this.opt.allowAccountTargetingForThisRequest&&this.clc_options.tgt_e&&this.clc_options.tgt_p>0){if(e.cM("Targeting enabled."),this.clc_options.tgt_p<100){e.cM("Targeting rate limit enabled.  Rolling the dice...");const t=Math.floor(100*Math.random())+1;if(e.cM("Rolled "+t+" and the max is "+this.clc_options.tgt_p),t>this.clc_options.tgt_p)return void e.cM("Will not request targeting.")}return e.cM("Will request targeting."),function(e,t,s,n){if(t){const t=new Headers;return t.append("Accept","application/json"),async function(e,t={},s=5e3){if("number"!=typeof s&&null!=s&&!1!==s){if("string"!=typeof s)throw new Error("fetchWithTimeout: timeout must be a number");if(s=parseInt(s),isNaN(s))throw new Error("fetchWithTimeout: timeout must be a number (or string that can be parsed to a number)")}const n=new AbortController,{signal:o}=n,a=fetch(e,{...t,signal:o}),i=setTimeout(()=>n.abort(),s);try{const e=await a;return clearTimeout(i),e}catch(e){throw clearTimeout(i),e}}(s+"?"+new URLSearchParams({omni:e}),{method:"GET",mode:"cors",headers:t},n).then(e=>e.json())}return Promise.reject("No consent")}(this.opt.omni,this.opt.targeting_consent,this.clc_options.tgt_u,this.clc_options.tgt_to).catch(t=>{e.vU("Error fetching user account targeting"),e.vU(t)})}e.cM("Targeting disabled.  Will not request account targeting data.")}initDebugPanel(t,s){e.cM("initDebugPanel"),e.cM("Not showing debug panel.")}},window.clcGamLoaderOptions&&(cam.init(),cam.load())})()})();</script><script src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"></script>
        
    <footer id="footer" class="site-footer js-footer theme-light__forced" role="contentinfo">
        <div class="site-footer--container">
                <div class="site-footer--logo">

                    <a href="https://stackoverflow.com" aria-label="Stack Overflow"><svg aria-hidden="true" class="native svg-icon iconGlyphMd" width="32" height="37" viewBox="0 0 32 37"><path fill="#BCBBBB" d="M26 33v-9h4v13H0V24h4v9z"></path><path fill="#F48024" d="m21.5 0-2.7 2 9.9 13.3 2.7-2zM26 18.4 13.3 7.8l2.1-2.5 12.7 10.6zM9.1 15.2l15 7 1.4-3-15-7zm14 10.79.68-2.95-16.1-3.35L7 23zM23 30H7v-3h16z"></path></svg></a>
                </div>
            <nav class="site-footer--nav" aria-label="Footer">
                    <div class="site-footer--col">
                        <h5 class="-title"><a href="https://stackoverflow.com" class="js-gps-track" data-gps-track="footer.click({ location: 2, link: 15})">Stack Overflow</a></h5>
                        <ul class="-list js-primary-footer-links">
                            <li><a href="/questions" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 16})">Questions</a></li>
                                <li><a href="/help" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 3 })">Help</a></li>
                                <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 5 })" href="https://chat.stackoverflow.com/?tab=site&amp;host=stackoverflow.com">Chat</a></li>
                        </ul>
                    </div>
                    <div class="site-footer--col">
                        <h5 class="-title"><a href="https://stackoverflow.co/" class="js-gps-track" data-gps-track="footer.click({ location: 2, link: 19 })">Products</a></h5>
                        <ul class="-list">
                            <li><a href="https://stackoverflow.co/teams/?utm_medium=referral&amp;utm_source=stackoverflow-community&amp;utm_campaign=footer&amp;utm_content=teams" class="js-gps-track -link" data-ga="[&quot;teams traffic&quot;,&quot;footer - site nav&quot;,&quot;stackoverflow.com/teams&quot;,null,{&quot;dimension4&quot;:&quot;teams&quot;}]" data-gps-track="footer.click({ location: 2, link: 29 })">Teams</a></li>
                            <li><a href="https://stackoverflow.co/advertising/?utm_medium=referral&amp;utm_source=stackoverflow-community&amp;utm_campaign=footer&amp;utm_content=advertising" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 21 })">Advertising</a></li>
                            <li><a href="https://stackoverflow.co/advertising/employer-branding/?utm_medium=referral&amp;utm_source=stackoverflow-community&amp;utm_campaign=footer&amp;utm_content=talent" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 20 })">Talent</a></li>
                        </ul>
                    </div>
                <div class="site-footer--col">
                    <h5 class="-title"><a class="js-gps-track" data-gps-track="footer.click({ location: 2, link: 1 })" href="https://stackoverflow.co/">Company</a></h5>
                    <ul class="-list">
                            <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 1 })" href="https://stackoverflow.co/">About</a></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 27 })" href="https://stackoverflow.co/company/press/">Press</a></li>
                            <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 9 })" href="https://stackoverflow.co/company/work-here/">Work Here</a></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 7 })" href="https://stackoverflow.com/legal">Legal</a></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 8 })" href="https://stackoverflow.com/legal/privacy-policy">Privacy Policy</a></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 37 })" href="https://stackoverflow.com/legal/terms-of-service/public">Terms of Service</a></li>
                            <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 13 })" href="/contact">Contact Us</a></li>
                            <li id="consent-footer-link"><button type="button" data-controller="cookie-settings" data-action="click->cookie-settings#toggle" class="s-btn s-btn__link py4 js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 38 })" data-consent-popup-loader="footer">Cookie Settings</button></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 39 })" href="https://stackoverflow.com/legal/cookie-policy">Cookie Policy</a></li>
                    </ul>
                </div>
                <div class="site-footer--col site-footer--categories-nav">
                    <div>
                        <h5 class="-title"><a href="https://stackexchange.com" data-gps-track="footer.click({ location: 2, link: 30 })">Stack Exchange Network</a></h5>
                        <ul class="-list">
                            <li>
                                <a href="https://stackexchange.com/sites#technology" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Technology
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#culturerecreation" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Culture &amp; recreation
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#lifearts" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Life &amp; arts
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#science" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Science
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#professional" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Professional
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#business" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Business
                                </a>
                            </li>

                            <li class="mt16 md:mt0">
                                <a href="https://api.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    API
                                </a>
                            </li>

                            <li>
                                <a href="https://data.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Data
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
            <div class="site-footer--copyright fs-fine md:mt24">
                <ul class="-list -social md:mb8">
                    <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link:4 })" href="https://stackoverflow.blog?blb=1">Blog</a></li>
                    <li><a href="https://www.facebook.com/officialstackoverflow/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 31 })">Facebook</a></li>
                    <li><a href="https://twitter.com/stackoverflow" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 32 })">Twitter</a></li>
                    <li><a href="https://linkedin.com/company/stack-overflow" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 33 })">LinkedIn</a></li>
                    <li><a href="https://www.instagram.com/thestackoverflow" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 36 })">Instagram</a></li>
                </ul>

                <p class="md:mb0">
                    <span>Site design / logo © 2024 Stack Exchange Inc; </span>
                    <span>user contributions licensed under </span>
                    <a class="-link s-link td-underline" href="https://stackoverflow.com/help/licensing">CC BY-SA</a>
                    <span>. </span>
                    <span id="svnrev">rev&nbsp;2024.12.20.20747</span>
                </p>
            </div>
        </div>

    </footer>


    

            <!-- Google tag (gtag.js) -->
            <script async="" src="https://www.googletagmanager.com/gtag/js?id=G-WCZ03SZFCQ"></script>
            <script>
                window.dataLayer = window.dataLayer || [];
                function gtag() { dataLayer.push(arguments); }
            </script>
            <script>
                (function(i, s, o, g, r, a, m) {
                    i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function() { (i[r].q = i[r].q || []).push(arguments) }, i[r].l = 1 * new Date(); a = s.createElement(o),
                        m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m);
                })(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');
            </script>
        <script>
            StackExchange.ready(function() {

                var ga3Settings = {
                    autoLink: ["stackoverflow.blog","info.stackoverflowsolutions.com","stackoverflowsolutions.com"],
                    sendTitles: true,
                    tracker: window.ga,
                    trackingCodes: [
                        'UA-108242619-1'
                    ],
                    checkDimension: 'dimension42'
                };

                var customGA4Dimensions = {};


                customGA4Dimensions["requestid"] = "1e4ff1dc-df73-4bf2-ab96-1fc7beda2128";

                    customGA4Dimensions["routename"] = "Questions/Show";


                    customGA4Dimensions["post_id"] = "14293869";


                    customGA4Dimensions["tags"] = "|python|";


                var ga4Settings = {
                    tracker: gtag,
                    trackingCodes: [
                        'G-WCZ03SZFCQ'
                    ],
                    consentsToPerformanceCookies: "granted",
                    consentsToTargetingCookies: "granted",
                    eventParameters: customGA4Dimensions,
                    checkForAdBlock: true,
                    sendTitles: true,
                    trackClicks: false,
                };

                StackExchange.ga.init({ GA3: ga3Settings, GA4: ga4Settings });


                StackExchange.ga.setDimension('dimension2', '|python|');


                StackExchange.ga.setDimension('dimension3', 'Questions/Show');


                StackExchange.ga.setDimension('dimension7', "1734895760.1984755123");

                StackExchange.ga.trackPageView();
            });
        </script>
        
            <script src="https://cdn.cookielaw.org/scripttemplates/otSDKStub.js" charset="UTF-8" data-document-language="true" data-domain-script="c3d9f1e3-55f3-4eba-b268-46cee4c6789c"></script>
<script defer="" src="https://cdn.sstatic.net/Js/modules/cookie-consent.en.js?v=36bebc18e04f"></script>

    
    <script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'8f628526df46700b',t:'MTczNDg5NTc2MC4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script><iframe height="1" width="1" style="position: absolute; top: 0px; left: 0px; border: none; visibility: hidden;"></iframe><iframe allow="join-ad-interest-group" data-tagging-id="G-WCZ03SZFCQ" data-load-time="1735226867029" height="0" width="0" src="https://td.doubleclick.net/td/ga/rul?tid=G-WCZ03SZFCQ&amp;gacid=1307499274.1732123043&amp;gtm=45je4cc1v891602898za200&amp;dma=0&amp;gcs=G111&amp;gcd=13r3r3l3l5l1&amp;npa=0&amp;pscdl=noapi&amp;aip=1&amp;fledge=1&amp;frm=0&amp;tag_exp=101925629~102067555~102067808~102081485~102198178&amp;z=480820980" style="display: none; visibility: hidden;"></iframe>
    
<div id="tr-popup" class="tr-popup" translate="no" data-hidden="true" data-invalid="true" data-disabled="false" lang="ru"><div class="tr-popup__block"><span class="tr-popup__title_original">Оригинальный текст:</span> <span class="tr-popup__value"></span></div><div class="tr-popup__block tr-popup__block_a"><span class="tr-popup__link tr-popup__link_suggest" data-action="expand">Предложить перевод</span><a href="https://translate.yandex.ru" class="tr-popup__link tr-popup__link_service" target="_blank" data-action="navigate"><span class="tr-popup__logo tr-popup__logo_company"></span><span class="tr-popup__logo tr-popup__logo_service"></span></a></div><div class="tr-popup__block tr-popup__block_b"><textarea class="tr-popup__input" spellcheck="false" autocapitalize="off" autocorrect="off" autocomplete="off" maxlength="1000"></textarea><div class="tr-popup__block tr-popup__block_submit"><span role="button" class="tr-popup__button tr-popup__button_submit" data-action="send">Отправить</span></div><div class="tr-popup__overlay tr-popup__overlay_submitted">Спасибо, перевод отправлен</div></div><span role="button" class="tr-popup__button tr-popup__button_close" data-action="clickClose"></span><span role="button" class="tr-popup__button tr-popup__button_menu" data-action="clickMenu"><span class="tr-popup__menu" data-action="disablePopup">Отключить подсказку с оригинальным текстом</span></span><span class="tr-popup__arrow"></span></div><div id="onetrust-consent-sdk" data-nosnippet="true"><div class="onetrust-pc-dark-filter ot-hide ot-fade-in"></div></div></body></html>''')