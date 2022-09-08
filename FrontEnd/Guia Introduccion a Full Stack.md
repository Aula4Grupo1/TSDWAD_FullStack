
<!DOCTYPE html>

<html  dir="ltr" lang="es-wp" xml:lang="es-wp">
<head>
    <title>Guía Introducción a Full Stack</title>
    <link rel="shortcut icon" href="https://acceso.ispc.edu.ar/pluginfile.php/1/tool_tenant/favicon/1/favicon-96x96.png" />
    <meta name="apple-itunes-app" content="app-id=1470929705, app-argument=https://acceso.ispc.edu.ar/mod/book/print.php?id=31892&amp;chapterid=0"/><link rel="manifest" href="https://acceso.ispc.edu.ar/admin/tool/mobile/mobile.webmanifest.php" /><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="moodle, Guía Introducción a Full Stack" />
<link rel="stylesheet" type="text/css" href="https://acceso.ispc.edu.ar/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.css" /><script id="firstthemesheet" type="text/css">/** Required in order to fix style inclusion problems in IE with YUI **/</script><link rel="stylesheet" type="text/css" href="https://acceso.ispc.edu.ar/theme/workplace/wpcss.php/workplace/1659990713_1/all-1-1654194304" />
<link rel="stylesheet" type="text/css" href="https://acceso.ispc.edu.ar/mod/book/tool/print/print.css" />
<script>
//<![CDATA[
var M = {}; M.yui = {};
M.pageloadstarttime = new Date();
M.cfg = {"wwwroot":"https:\/\/acceso.ispc.edu.ar","sesskey":"Uzh6OTIEiZ","sessiontimeout":"10800","sessiontimeoutwarning":"1200","themerev":"1659990713","slasharguments":1,"theme":"workplace","iconsystemmodule":"core\/icon_system_fontawesome","jsrev":"1659972264","admin":"admin","svgicons":true,"usertimezone":"Am\u00e9rica\/Argentina\/Buenos_Aires","contextid":77423,"langrev":1661670867,"templaterev":"1658767754"};var yui1ConfigFn = function(me) {if(/-skin|reset|fonts|grids|base/.test(me.name)){me.type='css';me.path=me.path.replace(/\.js/,'.css');me.path=me.path.replace(/\/yui2-skin/,'/assets/skins/sam/yui2-skin')}};
var yui2ConfigFn = function(me) {var parts=me.name.replace(/^moodle-/,'').split('-'),component=parts.shift(),module=parts[0],min='-min';if(/-(skin|core)$/.test(me.name)){parts.pop();me.type='css';min=''}
if(module){var filename=parts.join('-');me.path=component+'/'+module+'/'+filename+min+'.'+me.type}else{me.path=component+'/'+component+'.'+me.type}};
YUI_config = {"debug":false,"base":"https:\/\/acceso.ispc.edu.ar\/lib\/yuilib\/3.17.2\/","comboBase":"https:\/\/acceso.ispc.edu.ar\/theme\/yui_combo.php?","combine":true,"filter":null,"insertBefore":"firstthemesheet","groups":{"yui2":{"base":"https:\/\/acceso.ispc.edu.ar\/lib\/yuilib\/2in3\/2.9.0\/build\/","comboBase":"https:\/\/acceso.ispc.edu.ar\/theme\/yui_combo.php?","combine":true,"ext":false,"root":"2in3\/2.9.0\/build\/","patterns":{"yui2-":{"group":"yui2","configFn":yui1ConfigFn}}},"moodle":{"name":"moodle","base":"https:\/\/acceso.ispc.edu.ar\/theme\/yui_combo.php?m\/1659972264\/","combine":true,"comboBase":"https:\/\/acceso.ispc.edu.ar\/theme\/yui_combo.php?","ext":false,"root":"m\/1659972264\/","patterns":{"moodle-":{"group":"moodle","configFn":yui2ConfigFn}},"filter":null,"modules":{"moodle-core-chooserdialogue":{"requires":["base","panel","moodle-core-notification"]},"moodle-core-notification":{"requires":["moodle-core-notification-dialogue","moodle-core-notification-alert","moodle-core-notification-confirm","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-core-notification-dialogue":{"requires":["base","node","panel","escape","event-key","dd-plugin","moodle-core-widget-focusafterclose","moodle-core-lockscroll"]},"moodle-core-notification-alert":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-confirm":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-exception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-ajaxexception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-formchangechecker":{"requires":["base","event-focus","moodle-core-event"]},"moodle-core-popuphelp":{"requires":["moodle-core-tooltip"]},"moodle-core-lockscroll":{"requires":["plugin","base-build"]},"moodle-core-handlebars":{"condition":{"trigger":"handlebars","when":"after"}},"moodle-core-actionmenu":{"requires":["base","event","node-event-simulate"]},"moodle-core-maintenancemodetimer":{"requires":["base","node"]},"moodle-core-languninstallconfirm":{"requires":["base","node","moodle-core-notification-confirm","moodle-core-notification-alert"]},"moodle-core-event":{"requires":["event-custom"]},"moodle-core-dragdrop":{"requires":["base","node","io","dom","dd","event-key","event-focus","moodle-core-notification"]},"moodle-core-tooltip":{"requires":["base","node","io-base","moodle-core-notification-dialogue","json-parse","widget-position","widget-position-align","event-outside","cache-base"]},"moodle-core-blocks":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification"]},"moodle-core_availability-form":{"requires":["base","node","event","event-delegate","panel","moodle-core-notification-dialogue","json"]},"moodle-backup-confirmcancel":{"requires":["node","node-event-simulate","moodle-core-notification-confirm"]},"moodle-backup-backupselectall":{"requires":["node","event","node-event-simulate","anim"]},"moodle-course-util":{"requires":["node"],"use":["moodle-course-util-base"],"submodules":{"moodle-course-util-base":{},"moodle-course-util-section":{"requires":["node","moodle-course-util-base"]},"moodle-course-util-cm":{"requires":["node","moodle-course-util-base"]}}},"moodle-course-categoryexpander":{"requires":["node","event-key"]},"moodle-course-management":{"requires":["base","node","io-base","moodle-core-notification-exception","json-parse","dd-constrain","dd-proxy","dd-drop","dd-delegate","node-event-delegate"]},"moodle-course-formatchooser":{"requires":["base","node","node-event-simulate"]},"moodle-course-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-course-coursebase","moodle-course-util"]},"moodle-form-dateselector":{"requires":["base","node","overlay","calendar"]},"moodle-form-shortforms":{"requires":["node","base","selector-css3","moodle-core-event"]},"moodle-form-passwordunmask":{"requires":[]},"moodle-question-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-question-searchform":{"requires":["base","node"]},"moodle-question-preview":{"requires":["base","dom","event-delegate","event-key","core_question_engine"]},"moodle-availability_completion-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_date-form":{"requires":["base","node","event","io","moodle-core_availability-form"]},"moodle-availability_grade-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_group-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_grouping-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_lambda_timespent-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_profile-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-mod_assign-history":{"requires":["node","transition"]},"moodle-mod_bigbluebuttonbn-rooms":{"requires":["base","node","datasource-get","datasource-jsonschema","datasource-polling","moodle-core-notification"]},"moodle-mod_bigbluebuttonbn-recordings":{"requires":["base","node","datasource-get","datasource-jsonschema","datasource-polling","moodle-core-notification"]},"moodle-mod_bigbluebuttonbn-modform":{"requires":["base","node"]},"moodle-mod_bigbluebuttonbn-broker":{"requires":["base","node","datasource-get","datasource-jsonschema","datasource-polling","moodle-core-notification"]},"moodle-mod_bigbluebuttonbn-imports":{"requires":["base","node"]},"moodle-mod_quiz-util":{"requires":["node","moodle-core-actionmenu"],"use":["moodle-mod_quiz-util-base"],"submodules":{"moodle-mod_quiz-util-base":{},"moodle-mod_quiz-util-slot":{"requires":["node","moodle-mod_quiz-util-base"]},"moodle-mod_quiz-util-page":{"requires":["node","moodle-mod_quiz-util-base"]}}},"moodle-mod_quiz-modform":{"requires":["base","node","event"]},"moodle-mod_quiz-autosave":{"requires":["base","node","event","event-valuechange","node-event-delegate","io-form"]},"moodle-mod_quiz-quizbase":{"requires":["base","node"]},"moodle-mod_quiz-toolboxes":{"requires":["base","node","event","event-key","io","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-slot","moodle-core-notification-ajaxexception"]},"moodle-mod_quiz-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-base","moodle-mod_quiz-util-page","moodle-mod_quiz-util-slot","moodle-course-util"]},"moodle-mod_quiz-questionchooser":{"requires":["moodle-core-chooserdialogue","moodle-mod_quiz-util","querystring-parse"]},"moodle-message_airnotifier-toolboxes":{"requires":["base","node","io"]},"moodle-filter_glossary-autolinker":{"requires":["base","node","io-base","json-parse","event-delegate","overlay","moodle-core-event","moodle-core-notification-alert","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-filter_mathjaxloader-loader":{"requires":["moodle-core-event"]},"moodle-editor_atto-editor":{"requires":["node","transition","io","overlay","escape","event","event-simulate","event-custom","node-event-html5","node-event-simulate","yui-throttle","moodle-core-notification-dialogue","moodle-core-notification-confirm","moodle-editor_atto-rangy","handlebars","timers","querystring-stringify"]},"moodle-editor_atto-plugin":{"requires":["node","base","escape","event","event-outside","handlebars","event-custom","timers","moodle-editor_atto-menu"]},"moodle-editor_atto-menu":{"requires":["moodle-core-notification-dialogue","node","event","event-custom"]},"moodle-editor_atto-rangy":{"requires":[]},"moodle-report_eventlist-eventfilter":{"requires":["base","event","node","node-event-delegate","datatable","autocomplete","autocomplete-filters"]},"moodle-report_loglive-fetchlogs":{"requires":["base","event","node","io","node-event-delegate"]},"moodle-gradereport_grader-gradereporttable":{"requires":["base","node","event","handlebars","overlay","event-hover"]},"moodle-gradereport_history-userselector":{"requires":["escape","event-delegate","event-key","handlebars","io-base","json-parse","moodle-core-notification-dialogue"]},"moodle-tool_capability-search":{"requires":["base","node"]},"moodle-tool_lp-dragdrop-reorder":{"requires":["moodle-core-dragdrop"]},"moodle-tool_monitor-dropdown":{"requires":["base","event","node"]},"moodle-assignfeedback_editpdf-editor":{"requires":["base","event","node","io","graphics","json","event-move","event-resize","transition","querystring-stringify-simple","moodle-core-notification-dialog","moodle-core-notification-alert","moodle-core-notification-warning","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-atto_accessibilitychecker-button":{"requires":["color-base","moodle-editor_atto-plugin"]},"moodle-atto_accessibilityhelper-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_align-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_bold-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_charmap-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_clear-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_collapse-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_embedquestion-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emojipicker-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emoticon-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_equation-button":{"requires":["moodle-editor_atto-plugin","moodle-core-event","io","event-valuechange","tabview","array-extras"]},"moodle-atto_h5p-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_html-beautify":{},"moodle-atto_html-button":{"requires":["promise","moodle-editor_atto-plugin","moodle-atto_html-beautify","moodle-atto_html-codemirror","event-valuechange"]},"moodle-atto_html-codemirror":{"requires":["moodle-atto_html-codemirror-skin"]},"moodle-atto_image-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_indent-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_italic-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_link-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-usedfiles":{"requires":["node","escape"]},"moodle-atto_managefiles-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_media-button":{"requires":["moodle-editor_atto-plugin","moodle-form-shortforms"]},"moodle-atto_noautolink-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_orderedlist-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_recordrtc-recording":{"requires":["moodle-atto_recordrtc-button"]},"moodle-atto_recordrtc-button":{"requires":["moodle-editor_atto-plugin","moodle-atto_recordrtc-recording"]},"moodle-atto_rtl-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_strike-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_styles-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_subscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_superscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_table-button":{"requires":["moodle-editor_atto-plugin","moodle-editor_atto-menu","event","event-valuechange"]},"moodle-atto_title-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_underline-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_undo-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_unorderedlist-button":{"requires":["moodle-editor_atto-plugin"]}}},"gallery":{"name":"gallery","base":"https:\/\/acceso.ispc.edu.ar\/lib\/yuilib\/gallery\/","combine":true,"comboBase":"https:\/\/acceso.ispc.edu.ar\/theme\/yui_combo.php?","ext":false,"root":"gallery\/1659972264\/","patterns":{"gallery-":{"group":"gallery"}}}},"modules":{"core_filepicker":{"name":"core_filepicker","fullpath":"https:\/\/acceso.ispc.edu.ar\/lib\/javascript.php\/1659972264\/repository\/filepicker.js","requires":["base","node","node-event-simulate","json","async-queue","io-base","io-upload-iframe","io-form","yui2-treeview","panel","cookie","datatable","datatable-sort","resize-plugin","dd-plugin","escape","moodle-core_filepicker","moodle-core-notification-dialogue"]},"core_comment":{"name":"core_comment","fullpath":"https:\/\/acceso.ispc.edu.ar\/lib\/javascript.php\/1659972264\/comment\/comment.js","requires":["base","io-base","node","json","yui2-animation","overlay","escape"]},"mathjax":{"name":"mathjax","fullpath":"https:\/\/cdn.jsdelivr.net\/npm\/mathjax@2.7.9\/MathJax.js?delayStartupUntil=configured"}}};
M.yui.loader = {modules: {}};

//]]>
</script>

<meta name="moodle-validation" content="3fbc3cb4c70850bfcd604354fb23e76f">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-TDEL4Y2XQX"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());

gtag('config', 'G-TDEL4Y2XQX');
</script>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&display=swap" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body  id="page-mod-book-print" class="format-wplist  path-mod path-mod-book chrome dir-ltr lang-es_wp yui-skin-sam yui3-skin-sam acceso-ispc-edu-ar pagelayout-embedded course-1863 context-77423 cmid-31892 category-242 ">
<div class="toast-wrapper mx-auto py-0 fixed-top" role="status" aria-live="polite"></div>

<div>
    <a class="sr-only sr-only-focusable" href="#maincontent">Salta al contenido principal</a>
</div><script src="https://acceso.ispc.edu.ar/lib/javascript.php/1659972264/lib/babel-polyfill/polyfill.min.js"></script>
<script src="https://acceso.ispc.edu.ar/lib/javascript.php/1659972264/lib/polyfills/polyfill.js"></script>
<script src="https://acceso.ispc.edu.ar/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.js"></script><script src="https://acceso.ispc.edu.ar/lib/javascript.php/1659972264/lib/javascript-static.js"></script>
<script>
//<![CDATA[
document.body.className += ' jsenabled';
//]]>
</script>


<div id="page" >
    <section class="embedded-main">
        <div role="main"><span id="maincontent"></span><div class="book p-4">
    <div class="text-right"><a onclick="window.print();return false;" class="hidden-print" href="#"><img class="icon icon" alt="Imprimir el Libro Completo" title="Imprimir el Libro Completo" src="https://acceso.ispc.edu.ar/theme/image.php/workplace/booktool_print/1659990713/book" />Imprimir el Libro Completo</a></div>
    <div class="text-center pb-3 book_title"><h1>Guía Introducción a Full Stack</h1></div>
    <div class="book_info w-100 pt-6 d-inline-block">
        <div class="w-50 float-left">
            <table>
                <tr>
                    <td>
                        Sitio:
                    </td>
                    <td class="pl-3">
                        <a href="https://acceso.ispc.edu.ar">Instituto Superior Politécnico Córdoba</a>
                    </td>
                </tr>
                <tr>
                    <td>
                        Curso:
                    </td>
                    <td class="pl-3">
                        Programador Full Stack - TSDWAD - 2022
                    </td>
                </tr>
                <tr>
                    <td>
                        Libro:
                    </td>
                    <td class="pl-3">
                        Guía Introducción a Full Stack
                    </td>
                </tr>
            </table>
        </div>
        <div class="w-50 float-left">
            <table class="float-right">
                <tr>
                    <td>
                        Imprimido por:
                    </td>
                    <td class="pl-3">
                        Cristian Gonzalo VERA
                    </td>
                </tr>
                <tr>
                    <td>
                        Día:
                    </td>
                    <td class="pl-3">
                        jueves, 8 septiembre 2022, 12:27 
                    </td>
                </tr>
            </table>
        </div>
    </div>
    <div class="w-100">
        <div class="py-5"><div class="book_toc_numbered"><a name="toc"></a><h2 class="text-center pb-5">Tabla de contenidos</h2><ul><li><a title="1. Introducción" class="font-weight-bold text-decoration-none" href="#ch4102">1. Introducción</a></li><li><a title="2. Breve Reseña" class="font-weight-bold text-decoration-none" href="#ch4100">2. Breve Reseña</a></li><li><a title="3. Desarrollo Web Full Stack" class="font-weight-bold text-decoration-none" href="#ch4109">3. Desarrollo Web Full Stack</a></li><li><a title="4. Arquitectura de Aplicaciones Web" class="font-weight-bold text-decoration-none" href="#ch4103">4. Arquitectura de Aplicaciones Web</a><ul><li><a title="4.1. Arquitectura Web de 3 niveles" class="text-decoration-none" href="#ch4104">4.1. Arquitectura Web de 3 niveles</a></li><li><a title="4.2. Elementos de la Arquitectura Web" class="text-decoration-none" href="#ch4105">4.2. Elementos de la Arquitectura Web</a></li></ul></li><li><a title="5. Stacks" class="font-weight-bold text-decoration-none" href="#ch4107">5. Stacks</a><ul><li><a title="5.1. .NET  + Web Api+ IIS + Sql Server + Angular" class="text-decoration-none" href="#ch4106">5.1. .NET  + Web Api+ IIS + Sql Server + Angular</a></li><li><a title="5.2. LAMP" class="text-decoration-none" href="#ch4108">5.2. LAMP</a></li><li><a title="5.3. MEAN" class="text-decoration-none" href="#ch4097">5.3. MEAN</a></li><li><a title="5.4. MEER" class="text-decoration-none" href="#ch4099">5.4. MEER</a></li><li><a title="5.5. BFF" class="text-decoration-none" href="#ch4101">5.5. BFF</a></li><li><a title="5.6. Otros Stacks" class="text-decoration-none" href="#ch4098">5.6. Otros Stacks</a></li></ul></li></ul></div></div>
    </div>
    <div class="w-100">
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4102"><h2 class="text-center pb-5">1. Introducción</h2><p dir="ltr" style="text-align: left;"></p><p>En
esta sección avanzaremos en el concepto de “Arquitectura de las aplicaciones Web”,
su importancia y su aplicación en el desarrollo.</p>

<p>Objetivos:</p>

<p><ul><li>Comprender la
importancia de la arquitectura en el desarrollo de aplicaciones web como así
también sus elementos.</li><li>Identificar
los conceptos pilares de las arquitecturas de aplicaciones web y los stacks más
populares.</li><li>Identificar
los conceptos y tecnologías propias del frontend y backend, así como de la
conexión entre ambas.</li></ul></p>



<br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4100"><h2 class="text-center pb-5">2. Breve Reseña</h2><p dir="ltr" style="text-align: left;"></p>
<p><span style="font-size: 1rem;">Esta
        breve reseña está plagada de términos técnicos. La idea es ampliar estos
        conceptos durante el desarrollo del documento. Para lo cual nos referiremos al
        glosario disponible al final del mismo.</span></p>
<p><span style="font-size: 1rem;">ARPANET,
        The Advanced Research Projects Agency Network, fue el primer proyecto de una
        red </span><strong style="font-size: 1rem;">WAN </strong><span style="font-size: 1rem;">exitoso, en el año 1969. A
        partir de allí empieza un crecimiento vertiginoso del uso de la internet.</span></p>
<p><span style="font-size: 1rem;">Pero
        no fue hasta 1990 que Tim Berners-Lee creó la </span><strong style="font-size: 1rem;">WWW</strong><span style="font-size: 1rem;">, la “WorldWideWeb” que realizó la primera conexión desde un navegador
        a un servidor web mientras trabajaba en el CERN desarrollando así, las tres
        tecnologías fundamentales de la web (hoy estándares) que son:</span></p>
<p></p>
<ul>
    <li><strong>HTML</strong>
        (HyperText Markup Language). Lenguaje de marcado o etiquetado que se emplea
        para escribir los documentos o páginas web.</li>
    <li><strong>URL</strong>
        (Universal Resource Locator). El localizador de recursos uniforme, sistema de
        localización o direccionamiento de los documentos web.</li>
    <li><strong>HTTP</strong>
        (HyperText Transfer Protocol) El lenguaje con el que se comunica el navegador
        con el servidor web y el que se emplea para transmitir los documentos web.</li>
</ul>
<p></p>

<p>Se
    trata entonces de una arquitectura cliente-servidor en la que cada dispositivo
    electrónico en la red (internet, intranet o extranet) actúa como cliente o
    servidor lo que implica la comunicación entre procesos hacen peticiones
    (clientes) y procesos que responden a esas peticiones (servidores). Esta
    comunicación es posible gracias al protocolo HTTP.</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77423/mod_book/chapter/4100/image.png" alt="" role="presentation" class="img-fluid"><br><span style="font-size: 1rem;">Figura:
    Arquitectura cliente/servidor básica<br></span><br>
<p>En
    1994 (1 de octubre) Tim Berners-Lee abandona el CERN y funda la <u><a href="https://www.w3.org/">W3C</a></u>,
    en inglés, “World Wide Web Consortium”, organismo internacional que propone
    recomendaciones y estándares web que aseguran el crecimiento de la World Wide
    Web. </p>
<p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77423/mod_book/chapter/4100/-coffee-container_89755.png" alt="Cafe" width="75" height="75" class="img-fluid atto_image_button_text-bottom">A continuación, te invitamos a tomar un cafecito y mirar la conferencia de <strong>Tim Berners-Lee</strong> dónde cuenta en sus propias palabras cómo nació la web.</p><br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/MEjRFXbqjLc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe><br><br>
<p>A
    continuación te invitamos a visitar el siguiente enlace:&nbsp;<u><a href="http://www.evolutionoftheweb.com/?hl=es">http://www.evolutionoftheweb.com/?hl=es</a></u>&nbsp; dónde se puede observar la evolución de la
    web hasta 2012 y sus hitos más destacados de los cuales se destacan:</p>

<p>
</p><ul>
    <li>En 1991 surge
        <b>HTTP</b> definido como “protocolo de red
        para sistemas de información hipermedia distribuidos”.
    </li>
    <li>Muy próximo
        aparece <b>HTML</b> 1, es el lenguaje de
        marcado predominante de las páginas web.</li>
    <li>En 1995
        Netscape creó<b> JavaScript</b>, un
        lenguaje de secuencias de comandos basado en prototipos y “orientado a
        objetos”. El objetivo de este lenguaje de programación fue darle capacidad de
        ejecución al cliente de esta arquitectura web, o sea, al navegador.</li>
    <li>En 1998
        aparecen las hojas de estilo, en su versión 2. Se denominaron <b>CSS</b>, del inglés “Cascading Style
        Sheets”, que es un lenguaje de hojas de estilo empleado para describir la
        semántica de presentación de un documento, en este caso un documento web.</li>
</ul>
<p></p>





<br></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4109"><h2 class="text-center pb-5">3. Desarrollo Web Full Stack</h2><p dir="ltr" style="text-align: left;"></p><p>El<em>
desarrollo web full stack</em> permite crear <strong>aplicaciones web dinámicas</strong>. Esto se logra en base a los <strong>estándares web </strong>y utilizando tecnologías
web que pueden variar dependiendo del stack de desarrollo.</p>

<p>Según
la definición previa el desarrollo web full stack tiene por objeto la creación
de aplicaciones web dinámicas pero...</p><p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77423/mod_book/chapter/4109/note-task-comment-message-edit-write_108613%20%281%29.png" alt="task" width="75" height="75" class="img-fluid atto_image_button_text-bottom"><strong>Desafío:&nbsp;</strong><em>¿Qué entendemos por web dinámica?
¿En qué se diferencia de las web estáticas?</em><span> <span style="">Investiga.</span></span></p>

<p></p><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4103"><h2 class="text-center pb-5">4. Arquitectura de Aplicaciones Web</h2><p dir="ltr" style="text-align: left;"></p>
<p>Las
    aplicaciones web se basan en una arquitectura cliente/servidor. Es decir que,
    por un lado está el cliente (navegador) y por otro lado el servidor. Existen
    diferentes variantes de la arquitectura básica según como se implemente.</p>

<p>A
    continuación enumeramos algunas las arquitecturas más comunes:</p>

<p></p>
<ul>
    <li><strong>Servidor web
            + base de datos en un mismo servidor (2 niveles)</strong>. En este caso el servidor
        gestiona tanto la lógica de negocio como la lógica de los datos y los datos.<img src="https://acceso.ispc.edu.ar/pluginfile.php/77423/mod_book/chapter/4103/image.png" alt="" role="presentation" class="img-fluid" style="font-size: 1rem;"></li>
    <li>
        <p><strong>Servidor web
                y de datos separados (3 niveles).</strong> En este caso se separa la lógica de negocio
            de la de datos en diferentes servidores.<img src="https://acceso.ispc.edu.ar/pluginfile.php/77423/mod_book/chapter/4103/image%20%281%29.png" alt="" role="presentation" class="img-fluid" style="font-size: 1rem;"></p>
    </li>
    <li>
        <p><span style="font-size: 1rem;"><strong>Servidor web
                    + servidor de aplicaciones + base de datos en un mismo servidor (2 niveles).</strong></span><br><img src="https://acceso.ispc.edu.ar/pluginfile.php/77423/mod_book/chapter/4103/image%20%282%29.png" alt="" role="presentation" class="img-fluid" style="font-size: 1rem;"></p>
    </li>
    <li>
        <p><span style="font-size: 1rem;"><strong>Servidor de
                    aplicaciones + base de datos en un mismo servidor (3 niveles)</strong>.</span></p>
    </li>
    <li><strong>Servidor de
            aplicaciones,&nbsp; base de datos y servicios
            de aplicaciones en diferentes separados en diferentes servidores (4 niveles)</strong>.</li>
</ul>
<p></p>

<p>El
    objetivo de separar las distintas funcionalidades en distintos servidores es
    aumentar la escalabilidad y el rendimiento. Por ejemplo el servidor web al
    ofrecer servicios de http deberá tener una buena conexión a internet mientras
    que el servidor de base de datos requerirá tener una buena capacidad de
    almacenamiento y procesamiento. (Sergio Lujan Mora, Arquitectura de aplicaciones
    web: historia, principios básicos y clientes web)</p><br>
<p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4104"><h3 class="text-center pb-5">4.1. Arquitectura Web de 3 niveles</h3><p dir="ltr" style="text-align: left;"></p><p>En
cuanto a los desarrolladores, es importante agregar que si bien, lo más
habitual es que&nbsp; se especialicen en
frontend o en backend, hoy existe un tercer perfil: desarrollador “Full-Stack”
(muy solicitado por las empresas de desarrollo de software). Este&nbsp; perfil se caracteriza por tener una visión
integral de toda la aplicación web (frontend + backend).</p><p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77423/mod_book/chapter/4104/image.png" alt="" role="presentation" class="img-fluid"><br></p><p></p><h4>Frontend </h4><p></p><p>El <b>Frontend</b>
son aquellas tecnologías de desarrollo <b><i>web del lado del cliente</i></b>, es decir,
las que corren en el navegador del usuario y que son básicamente tres: <i>HTML, CSS y
JavaScript</i>. </p>

<p>El frontend <i>se enfoca en el usuario</i>, en todo con lo que puede interactuar y lo
que ve mientras navega. Una buena experiencia de usuario, inmersión y
usabilidad son algunos de los objetivos que busca un buen desarrollador
frontend, y hoy en día hay una gran variedad de <b>Frameworks</b>, preprocesadores y librerías que ayudan en esta tarea.</p><h5>Lenguajes Web Frontend</h5><p></p><p>A
pesar de que hay varios lenguajes que se usan en el frontend, nosotros nos
basaremos en tres, HTML, CSS y JavaScript, aunque HTML y CSS no son lenguajes
de programación, no se debe confundir lenguajes de programación como ejemplo
JavaScript, ActionScript o Java, con lenguajes de marcado como HTML o lenguaje
de hojas de estilo cómo CSS. También existen otros lenguajes frontend, como por
ejemplo ActionScript, Java, Silverlight, VBScript u otros lenguajes XML, pero
se usan poco en comparación con HTML, CSS y JavaScript.</p>

<p>HTML
es un lenguaje de marcado de los contenidos de un sitio web, es decir, para
designar la función de cada elemento dentro de la página: titulares, párrafos,
listas, tablas, etc. Es el esqueleto de la web y la base de todo el frontend.</p>

<p>CSS
es un lenguaje de hojas de estilo creado para controlar la presentación de la
página definiendo colores, tamaños, tipos de letras, posiciones, espaciados,
etc.</p>

<p>JavaScript
es un lenguaje de programación interpretado que se encarga del comportamiento
de una página web y de la interactividad con el usuario.</p>

<p>Aparte,
junto al cliente también tenemos los frameworks, las librerías, los
preprocesadores, los plugins... pero todo gira alrededor de HTML, CSS y
JavaScript.</p><h4>Backend </h4><p>El<b> Backend</b> es aquello que <b><i>se
encuentra del lado del servidor</i></b> y se encarga de <i>interactuar con bases de datos, verificar maniobras de sesiones de
usuarios, montar la página en un servidor y servir todas las vistas creadas por
el desarrollador frontend</i>. </p>

<p>En
este caso el número de tecnologías es mucho menos limitado, puesto que la
programación backend puede alcanzar <i>lenguajes
como PHP, Python, .NET, Java, etc</i>., y las bases de datos sobre las que se
trabaja pueden ser SQL, MongoDB, MySQL, entre otras.</p>

<p>La
idea de esta abstracción es mantener separadas las diferentes partes de un sistema web o software para tener un mejor
control. En pocas palabras, el objetivo es que el frontend recoja los datos y
el backend los procese.</p>

<p>Estas
dos capas que forman una aplicación web son independientes entre sí (no
comparten código), pero intercambian información. Esta división permite que el
acceso a las bases de datos solo se haga desde el backend y el usuario no tenga
acceso al código de la aplicación, mientras que la programación del lado del
cliente permite que el navegador pueda, por ejemplo, controlar dónde el usuario
hace clic o acceder a sus ficheros.</p>

<p>Con
esta separación de entornos el usuario de una aplicación web lo que hace es, por
ejemplo, iniciar sesión escribiendo su usuario y contraseña en un formulario; a
continuación, los datos se envían y el backend toma esta información que viene
desde el HTML y busca las coincidencias de usuario en la base de datos con una
serie de procesos invisibles para el usuario. En este punto, el servidor
mandaría un mensaje al frontend dándole acceso (o no) a la aplicación.</p><h5>Lenguajes Web Backend</h5><p></p><p>Aquí
encontramos unos cuantos, por ejemplo, PHP, Python, Rails, Go, C#, Java, Node
JS (JavaScript) entre otros. Como vemos, mientras que para el frontend se
acostumbra a trabajar solo con tres lenguajes, en el backend hay unos cuantos
más. Por suerte, un desarrollador backend no necesita saberlos todos.</p>

<p>Quizás
habéis notado que tenemos JavaScript tanto por el lado del cliente como por el
lado del servidor. JavaScript se creó originalmente como lenguaje para el
frontend, pero los últimos años se ha creado su lugar dentro del backend con
NodeJS, un motor que interpreta JavaScript en el servidor sin necesidad de un
navegador. Esto no quiere decir que el JavaScript que tenemos en el cliente
tenga alguna conexión con el que se encuentra en el servidor: cada uno corre
por su parte de manera independiente. El JavaScript del cliente corre en el
navegador y no tiene ningún enlace ni ninguna conexión con el que hay en el
servidor y no le interesa saber cómo está montada la arquitectura del servidor
ni cómo se conecta a la base de datos.</p>

<p>Ahora
se puede utilizar el mismo lenguaje en todos los contextos del desarrollo:
JavaScript en el cliente de escritorio (DOM), en el cliente móvil (Cordova,
React Native), en el servidor (Node.js) o en la BBDD (MongoDB). La posibilidad
de trabajar frontend y backend con un mismo lenguaje desde el punto de vista
del desarrollador es muy cómoda, especialmente para aquellos que trabajan ambos
mundos.</p>

<p>En
cuanto a la tecnología, las herramientas que se utilizan en el backend son:
editores de código, compiladores, algunos depuradores para revisar errores y
seguridad, gestores de bases de datos y algunas otras cosas.</p><br><p></p><br><p></p><br><p></p><br><p></p><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4105"><h3 class="text-center pb-5">4.2. Elementos de la Arquitectura Web</h3><p dir="ltr" style="text-align: left;"></p><p>A
continuación se enumeran los elementos de la arquitectura web (pueden variar
según la arquitectura elegida):</p><p><b>La infraestructura de red</b></p>

<p>Si
bien es cierto que en fase de desarrollo, para probar nuestra aplicación web,
no necesitaríamos esta infraestructura, una vez nuestra aplicación se instale
en el hosting definitivo, será necesaria una red ethernet y todos los
componentes que hacen posible la conectividad de los equipos informáticos. Con
esto nos referimos a cables de red, sea utp o fibra óptica, placas de red, sea
wifi o cableada, switch, routers, modem, etc. Y estos componentes físicos son
necesarios tanto del lado del cliente como del servidor.</p>

<p>Con
esto se quiere decir que no es posible implementar una aplicación web sino
existe una infraestructura de red preexistente o se diseña e implementa una
nueva. </p>

<p>Esta
puede ser: internet, intranet o extranet.</p><p><b>Isp</b></p>

<p>Es
el proveedor del servicio de internet.</p><p><b>Cliente Web</b></p>

<p>Es el navegador web. Ej. Chrome, Safari,
Firefox, etc. El cliente se ejecuta en un hardware y hoy sabemos que puede ser
desde una pc de escritorio, una notebook, o un dispositivo móvil tal como un
teléfono celular o una tablet. </p>

<p>Pero ya no se restringe solo a estos
dispositivos sino que podría ser, por ejemplo, un sistema embebido ejecutándose
en una SBC (small board computer). Incluso podría no estar ejecutando un
navegador convencional, como por ejemplo un reloj inteligente, o un dispositivo
vinculado a una máquina de producción seriada como los surgidos de la mano del
concepto de Industria 4.0.</p><p><b>Nombre de
Dominio</b></p>

<p>Dicho de forma sencilla, el nombre de dominio
(o, simplemente, "dominio") es el nombre de un sitio web. Es decir,
es lo que aparece después de "@" en una dirección de correo
electrónico o después de "www." en una dirección web. Si alguien te
pregunta cómo encontrarte en Internet, normalmente tendrás que decirle tu
nombre de dominio (<u style="font-size: 1rem;"><a href="https://domains.google/intl/es_es/learn/web-terms-101/">https://domains.google/intl/es_es/learn/web-terms-101/</a>).</u></p><p><span style="font-size: 1rem;">Aquí tienes algunos ejemplos de nombres de
dominio:</span></p>

<p>google.com, wikipedia.org, youtube.com</p><p><b>URL</b></p>

<p>Una URL (o localizador uniforme de recursos)
es una dirección web completa que se utiliza para encontrar una página web
específica. Mientras que el dominio es el nombre del sitio web, la URL es una
dirección que remite a los usuarios a una de las páginas de ese sitio web. Cada
URL contiene un nombre de dominio y otros componentes necesarios para localizar
una página o un contenido concretos (<u><a href="https://domains.google/intl/es_es/learn/web-terms-101/">https://domains.google/intl/es_es/learn/web-terms-101/</a>)</u>. </p><p>Aquí tienes algunos ejemplos de URLs:</p>

<p><a href="http://www.google.com" class="_blanktarget">http://www.google.com</a></p>

<p><a href="https://es.wikipedia.org/wiki/umami" class="_blanktarget">https://es.wikipedia.org/wiki/umami</a></p>

<p><a href="https://www.youtube.com/feed/trending" class="_blanktarget">https://www.youtube.com/feed/trending</a></p><p><b>Sitio web </b></p>

<p>Aunque una cosa lleve a la otra, comprar un
nombre de dominio no implica tener un sitio web. El dominio es el nombre del
sitio web, la URL es la forma de encontrarlo y el sitio web es lo que los
usuarios ven en su pantalla y con lo que interactúan. Es decir, cuando compres
un dominio, habrás adquirido el nombre de tu sitio web, pero te faltará crear
el sitio web en cuestión (<u><a href="https://domains.google/intl/es_es/learn/web-terms-101/">https://domains.google/intl/es_es/learn/web-terms-101/</a>)</u>.</p><p><b>Servidor DNS</b> </p>

<p>Se ocupa de la administración del espacio de
nombres de dominio. Este servidor se encarga de hacer las conversiones de
nombres de dominio a direcciones IP. Cuando el cliente realiza una petición
web, por ejemplo google.com, una de las primeras acciones del sistema es
invocar a un servidor DNS para que le devuelva la dirección IP del/ o de alguno
de los servidores de google. Por ejemplo devolverá la ip 172.217.162.14.</p><p><b>Servidor Web</b> o servidor HTTP, es un programa informático que procesa una
aplicación del lado del servidor, realizando conexiones bidireccionales o
unidireccionales y síncronas o asíncronas con el cliente y generando o cediendo
una respuesta en cualquier lenguaje o aplicación del lado del cliente.</p><p><b>Contenedor de
aplicaciones Web (o servidor de aplicaciones web)</b>, módulo que permite la ejecución de aplicaciones web. Por ejemplo,
módulo PHP o Python del Servidor Web. Componente ASP o ASPX de IIS. Servidor o
Contenedor de Aplicaciones Web Java: Tomcat,&nbsp;
Weblogic, Websphere, JBoss, Geronimo, etc.</p><p><b>Servidor de
Bases de Datos. </b>Estos son contenedores de bases de datos que
permiten organizar y administrar los datos que deben permanecer en un medio de
almacenamiento permanente. Resuelven problemas de seguridad, mecanismos de
comunicación, concurrencia, inconsistencias de los datos, respaldo, entre
otros. Hay varios tipos de bases de datos, por ejemplo las relaciones que
organizan los datos en forma de tablas, en filas y columnas. Otro tipos son los
orientados a objetos u orientados a documentos donde el concepto de tablas se
cambia por el de colección con formatos similares a “json”. </p>

<p>JavaScript Object Notation (JSON) es un
formato basado en texto estándar para representar datos estructurados en la
sintaxis de objetos de JavaScript. Es comúnmente utilizado para transmitir
datos en aplicaciones web (por ejemplo: enviar algunos datos desde el servidor
al cliente, así estos datos pueden ser mostrados en páginas web, o vice versa) (<a href="https://developer.mozilla.org/es/docs/Learn/JavaScript/Objects/JSON" class="_blanktarget">https://developer.mozilla.org/es/docs/Learn/JavaScript/Objects/JSON</a>) .<a href="#_ftn1" name="_ftnref1" title=""><sup><!--[endif]--></sup></a></p>

<div><h4>Proceso de una Petición Web 2.0</h4><img src="https://acceso.ispc.edu.ar/pluginfile.php/77423/mod_book/chapter/4105/image.png" alt="" role="presentation" class="img-fluid"><br><div id="ftn1"><p><u></u></p>

</div>

</div><div><p style="text-align: left;">Figura: Proceso de petición web 2.0
Recuperado de: <u><a href="https://cursosdedesarrollo.com/2019/11/arquitectura-web-2-0-dinamica-en-el-servidor/">https://cursosdedesarrollo.com/2019/11/arquitectura-web-2-0-dinamica-en-el-servidor/</a></u></p><p style="text-align: left;"></p><ol><li><span style="font-size: 1rem;">“Cliente Web: Solicita la resolución de
     nombres al servidor DNS. Por ejemplo: google.com</span></li><li><span style="font-size: 1rem;">Servidor DNS: Recibe y trata la
     solicitud. Una vez recibida la petición realiza las consultas necesarias
     para resolver y obtener la dirección IP.</span></li><li><span style="font-size: 1rem;">Servidor DNS: Devuelve al navegador Web
     la dirección IP que corresponde al Servidor Web.</span></li><li><span style="font-size: 1rem;">Cliente Web: Conecta con el servidor web
     mediante la dirección IP y el puerto. Realiza la petición mediante una URL
     (Método GET) o un formulario (Método POST). Dicha solicitud incluye: la dirección
     IP del servidor web, el puerto del servidor web, URL y parámetros.</span></li><li><span style="font-size: 1rem;">Servidor Web: Control de Acceso, Análisis
     de la petición y localización del recurso. Como detecta que es el acceso a
     un fichero o ruta de aplicación tiene que traspasar el control al
     Contenedor de aplicaciones Web</span></li><li><span style="font-size: 1rem;">Paso de la petición del servidor web al
     contenedor de aplicaciones web</span></li><li><span style="font-size: 1rem;">El contenedor analiza la petición y en
     base a la ruta traspasa el control a la aplicación web.</span></li><li><span style="font-size: 1rem;">Paso del control de la petición desde el
     CAW a la aplicación.</span></li><li><span style="font-size: 1rem;">La aplicación recibe la petición y decide
     qué hacer en base a ella, es decir, elegir la funcionalidad que se
     encargará de gestionar esa petición, normalmente en base a la ruta, el
     método HTTP y los parámetros de entrada por URL. Una vez elegida ejecutará
     esa funcionalidad.</span></li><li><span style="font-size: 1rem;">La aplicación realiza una petición SQL a
     la base de datos.</span></li><li><span style="font-size: 1rem;">La Base de Datos recibe la petición SQL y
     la procesa realizando los cambios que tenga que hacer, si corresponde.</span></li><li><span style="font-size: 1rem;">Una vez procesada la petición devuelve
     los datos a la aplicación web, normalmente un conjunto de datos. Ej. los
     10 últimos clientes.</span></li><li><span style="font-size: 1rem;">La aplicación web recibe estos datos y
     tiene que generar una salida, normalmente HTML, donde estructura el
     contenido de los datos devueltos por la BBDD en etiquetas HTML.</span></li><li><span style="font-size: 1rem;">La aplicación web devuelve una respuesta
     al Contenedor de Aplicaciones Web</span></li><li><span style="font-size: 1rem;">El contenedor procesa la respuesta, para
     controlar la ejecución de la aplicación por si esta falla.</span></li><li><span style="font-size: 1rem;">El Contenedor de Aplicaciones Web
     devuelve el fichero al servidor web.</span></li><li><span style="font-size: 1rem;">El servidor Web devuelve los datos dentro
     de la respuesta HTTP al navegador web.</span></li><li><span style="font-size: 1rem;">Cliente Web: Presenta (renderiza) el
     contenido HTML resultante.</span></li><li>Repite los pasos 4-18 para obtener los ficheros
relacionados: CSS, JS, Imágenes, etc.”</li></ol><p></p><p></p>(<u><a href="https://cursosdedesarrollo.com/2019/11/arquitectura-web-2-0-dinamica-en-el-servidor/">https://cursosdedesarrollo.com/2019/11/arquitectura-web-2-0-dinamica-en-el-servidor/</a></u> )<br></div><br><p>En
resumen, si hay algo que nos queda claro entonces, es el potencial que ha
tenido y tiene la web, su capacidad de escalabilidad, por lo que&nbsp; todos los mercados, incluso la cultura y el
arte, se manifiestan con gran libertad.</p>

<p>Pero
a medida que ampliamos los horizontes aparecen nuevos problemas y estos generan
nuevas soluciones. Es que ya no son simples páginas web coloridas y
dinamizadas, sino sistemas completos, distribuidos, multiplataformas, para usos
generales y específicos, como por ejemplo una plataforma de ecommerce.</p><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4107"><h2 class="text-center pb-5">5. Stacks</h2><p dir="ltr" style="text-align: left;"></p><p>Lo
que denominamos <b><i>stack tecnológico</i></b>, o también denominado <b><i>stack de soluciones</i></b> o <b><i>ecosistema
de datos</i></b>, es un conjunto de todas las herramientas tecnológicas
utilizadas para construir y ejecutar una sola aplicación, en este caso web.
Sitios como la red social Facebook, han sido desarrolladas por una combinación
de frameworks de codificación y lenguajes, entre los que se incluyen
JavaScript, HTML, CSS, PHP y ReactJS. Así podemos decir que este es el “stack
tecnológico” de Facebook.</p>

<p>Me
surge de manera natural pensar cuales son los stacks usan Netflix, Whatsapp,
Instagram…</p>

<p>Uno
de los stacks o pila de tecnologías más utilizado por los desarrolladores es el
que se conoce por <b>LAMP</b>: Linux,
Apache, MySQL y PHP. Cualquier web hecha con Wordpress, Drupal o Prestashop,
por ejemplo, están hechas sobre estos cuatro pilares.</p><p>Pero
se pueden hacer las variaciones que se crean convenientes, puesto que muchas de
estas tecnologías son intercambiables por otras similares. Por ejemplo, NginX
en lugar de Apache, PostgreSQL en lugar de MySQL o Ruby on Rails en lugar de
PHP.</p>

<p>Otro
stack muy utilizado es el llamado <b>MEAN</b>,
que se compone de MongoDB, Express, Angular y NodeJS. A diferencia del conjunto
anterior, esta pila de trabajo busca entregar la mayor cantidad de carga de
procesamiento al cliente pero requiere una forma muy diferente de pensar las
cosas.</p>

<p>También
existe un equivalente en Microsoft que sería Windows + Microsoft IIS + .NET +
SQL Server.</p><p><b>Stack populares</b></p>

<p><ul><li><b>LAMP</b>: Linux - Apache - MySQL - PHP</li><li><b>LEMP</b>: Linux - Nginx - MySQL - PHP</li><li><b>MEAN</b>: MongoDB - Express - AngularJS - Node.js</li><li><b>Django</b>: Python - Django - MySQL</li><li><b>Ruby</b> <b>on Rails</b>: Ruby -
SQLite - Rails</li><li><b>.NET:</b> &nbsp;.NET + WebApi +
IIS - SQL Server </li></ul></p>









<br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4106"><h3 class="text-center pb-5">5.1. .NET  + Web Api+ IIS + Sql Server + Angular</h3><p dir="ltr" style="text-align: left;"></p><p>Microsoft tiene su propio
servidor web que se llama Internet Information Server, IIS, y su servidor de
base de datos, que se llama Microsoft SQL Server.</p>

<p>Afortunadamente nos
provee con sus versiones “community”, o sea de uso libre.</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77423/mod_book/chapter/4106/image.png" alt="" role="presentation" class="img-fluid"><br><p>Por
lo tanto esta arquitectura quedaría conformada por:</p>

<p></p><ul><li>IIS: servidor
web. </li><li>Lenguaje en
el backend: cualquiera de la familia .Net: C#, VB .Net, Asp.net, etc.</li><li>Servidor de
base de datos: SQL Server.</li><li>Frontend Framework: Angular Cli.</li></ul><p></p>





<p><span>Importante agregar que,&nbsp; </span><strong>Microsoft .Net Core e</strong><strong>s</strong> la plataforma de desarrollo de Microsoft
más moderna con las siguientes características generales:</p>

<p></p><ul><li>de código
fuente abierto </li><li>multiplataforma:
esto significa que el proyecto desarrollado se puede desplegar (deploy), o sea,
poner en producción, en un servidor linux, macOS u otros sistemas operativos.
No tiene la dependencia del sistema operativo Windows.</li><li>de alto
rendimiento. </li><li>para la
creación de todo tipo de aplicaciones.</li><li>es modular,
usando el sistema de paquetes <strong>NuGet.</strong></li></ul><p></p>







<p>Probablemente
la mejor variación de la arquitectura mostrada antes sea mudar de .Net
Framework a .Net Core.</p><p>Para más información sobre .Net
Core, consulta los siguientes enlaces:</p>

<p><ul><li><u><a href="https://openwebinars.net/blog/que-es-net-core/">https://openwebinars.net/blog/que-es-net-core/</a></u></li><li><u><a href="https://docs.microsoft.com/en-us/aspnet/core/?view=aspnetcore-5.0">https://docs.microsoft.com/en-us/aspnet/core/?view=aspnetcore-5.0</a></u></li></ul></p>

<br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4108"><h3 class="text-center pb-5">5.2. LAMP</h3><p dir="ltr" style="text-align: left;"></p><p>LAMP es el
acrónimo de Linux, Apache, MySQL y PHP, es decir las tecnologías que conforman
esta plataforma de código abierto para el desarrollo del backend.</p>

<p></p><ul><li>Linux, el sistema operativo;</li><li>Apache, el servidor web;</li><li>MySQL/MariaDB, el motor de bases de datos;</li><li>PHP, el lenguaje de programación.</li></ul><p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77423/mod_book/chapter/4108/image.png" alt="" role="presentation" class="img-fluid"><br></p><p></p><p style="text-align: left;">Figura:
Arquitectura LAMP,&nbsp;<u style="font-size: 1rem; text-align: left;"><a href="https://es.wikipedia.org/wiki/LAMP">https://es.wikipedia.org/wiki/LAMP</a></u></p><p style="text-align: left;"></p><p>De este stack se pueden
desprender varias variaciones como mencionamos anteriormente, incluso cambiando
la marca del servidor de Apache a Nginx, los motores de bases de datos, por
ejemplo de Mysql a Postgresql.</p>

<p>Esta arquitectura tiene
una particularidad, en principio es la más antigua y el formato de aplicaciones
predominante se denomina <b><i>“Multi Page Application o MPA” </i></b>o
aplicación de múltiples páginas.</p>

<p>Esto hace referencia a Arquitecturas
Web Clásicas en donde uno dispone de múltiples páginas HTML y cada una carga
diferentes contenidos. Es decir cada página muestra su contenido y se conecta
mediante links con las demás y todas son enviadas desde el servidor.</p><br><p></p><br><p></p><p></p>





<br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4097"><h3 class="text-center pb-5">5.3. MEAN</h3><p dir="ltr" style="text-align: left;"></p><p>MEAN es una plataforma de desarrollo
full-stack en JavaScript, es decir, es el conjunto de tecnologías necesarias
para el desarrollo de todas las capas de una aplicación web con JavaScript.
Está compuesto fundamentalmente por cuatro tecnologías, MongoDB, Express,
Angular y Node.js.</p>

<p>Cada
subsistema del MEAN stack es de código abierto y de uso gratuito. A
continuación se describen estas tecnologías. </p><p></p><ul><li><b>MongoDB:</b> es un sistema de base de datos NoSQL, que
almacena los datos en estructuras o “documentos”, los cuales están definidos
con la notación JSON (Notación simple de objeto tipo JavaScript), lo que
permite una rápida manipulación y transferencia de los datos. La mayor
característica de esta plataforma es su escalabilidad, lo que significa que
puede aumentar en forma considerable la cantidad de datos que almacena sin que
esto afecte su funcionamiento en general.</li><li><b>ExpressJS:</b> este framework está escrito
en JavaScript para Node.js, es decir es un módulo de NodeJS y como tal funciona
sobre esta plataforma; este módulo ofrece los métodos suficientes en
JavaScript, para poder manejar las solicitudes o peticiones que se hacen por
medio de los métodos del protocolo HTTP (GET, POST, etc.). También ofrece un
sistema simple de enrutamiento, que dentro del mean stack es aprovechado en el
back-end o en el lado del servidor.</li><li><b>AngularJS:</b> es un framework que facilita
la manipulación del DOM ('Modelo de Objetos del Documento' o 'Modelo en Objetos
para la Representación de Documentos), y por lo tanto en el mean stack es la
plataforma que se usa para trabajar en el front end. Este framework permite
crear una gran variedad de efectos, de una forma sencilla, reduciendo
contundentemente la cantidad de código, lo que permite que sea mucho más
sencillo de mantener.</li><li><b>NodeJS:</b> Es un entorno de ejecución o
runtime para JavaScript construido con el motor de JavaScript V8 de Chrome y es
la plataforma encargada del funcionamiento del servidor. Funciona totalmente
con JavaScript, un lenguaje de programación que en un principio era dedicado a
correr en el lado del cliente, pero su uso se ha ampliado considerablemente en
todos los aspectos de un sitio web.</li></ul><p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77423/mod_book/chapter/4097/image.png" alt="" role="presentation" class="img-fluid"><br></p><p></p><p style="text-align: left;">Figura: Arquitectura MEAN, <u style="font-size: 1rem; text-align: left;"><a href="https://funnyfrontend.com/instalar-mongodb-y-uso-de-comandos-basicos/stack-mean-esquema/">https://funnyfrontend.com/instalar-mongodb-y-uso-de-comandos-basicos/stack-mean-esquema/</a></u></p><p>Esta
arquitectura tiene una particularidad, en principio es la más moderna y el
formato de aplicaciones predominante se denomina <b><i>“Single Page Application o SPA” </i></b>o
aplicación de una sola página.</p>

<p>Single
Page Applications es una arquitectura en la que el servidor únicamente dispone
de una página y carga todos los estilos y todos los formatos en el cliente. A
partir de ese momento, el cliente pide únicamente datos al servidor y va
renderizando diferentes componentes en el navegador que existen en la mega
página.</p><br><p></p><p></p>





<br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4099"><h3 class="text-center pb-5">5.4. MEER</h3><p dir="ltr" style="text-align: left;"></p><p>"MERN" es el acrónimo
de cuatro componentes: </p>

<p></p><ul><li><strong>&nbsp;MongoDB: </strong>definido en MEAN</li><li><strong>&nbsp;</strong><strong style="font-size: 1rem;">Express: </strong><span style="font-size: 1rem;">definido en MEAN</span></li><li><strong>&nbsp;</strong><strong style="font-size: 1rem;">React: </strong><span style="font-size: 1rem;">React (también llamada
React.js o ReactJS) es una librería Javascript de código abierto diseñada para
crear interfaces de usuario (frontend) y facilita el desarrollo de todo tipo de
aplicaciones.</span></li><li><span style="font-size: 1rem;"><p><strong>Node.js: </strong>definido en MEAN</p></span></li></ul><p></p>

<p><strong></strong></p>



<p>Es
importante agregar que Reac es una librería de software libre desarrollada
inicialmente por Facebook pero hoy mantenida por una creciente comunidad de
desarrolladores.</p>

<p></p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77423/mod_book/chapter/4099/image.png" alt="" role="presentation" class="img-fluid"><br><p style="text-align: left;">Figura:
Arquitectura MEER,<span style="font-size: 1rem;"><strong>&nbsp;</strong><u style=""><a href="https://medium.com/@blockchain_simplified/what-is-mern-stack-9c867dbad302" style="">https://medium.com/@blockchain_simplified/what-is-mern-stack-9c867dbad302</a></u></span></p><p>Es importante observar que, esta arquitectura es similar a MEAN, solo que cambia Angular por React.</p><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4101"><h3 class="text-center pb-5">5.5. BFF</h3><p dir="ltr" style="text-align: left;"></p><p>Se
puede usar una arquitectura Backend for Frontend (BFF) para crear backends para
aplicaciones web o móviles orientadas al cliente. Los BFF pueden ayudar a
respaldar una aplicación con múltiples clientes al mismo tiempo que mueven el
sistema a un estado menos acoplado que un sistema monolítico. </p>

<p>El
acoplamiento es “es el grado en que los módulos de un programa <strong>dependen </strong>unos de otros.”<a href="#_ftn1" name="_ftnref1" title=""><sup><!--[if !supportFootnotes]--><sup>[1]</sup><!--[endif]--></sup></a> </p>

<p>Una
aplicación monolítica es una unidad cohesiva de código.<a href="#_ftn2" name="_ftnref2" title=""><sup><!--[if !supportFootnotes]--><sup>[2]</sup><!--[endif]--></sup></a></p>

<p>Este
code pattern ayuda a los equipos a iterar las funciones más rápido y tener
control sobre los backends para aplicaciones móviles sin afectar la experiencia
de la aplicación móvil o web correspondiente.</p>

<div><!--[if !supportFootnotes]--><h4><span>Descripción</span></h4>

<p>Una
arquitectura de microservicio permite a los equipos iterar rápidamente y
desarrollar tecnología para escalar rápidamente. La arquitectura Backend for
Frontend (BFF) es un tipo de patrón creado con microservicios. El componente
principal de este patrón es una aplicación que conecta el frontend de su
aplicación con el backend. Este “Code Pattern BFF” lo ayudará a crear ese
componente de acuerdo con las mejores prácticas de IBM.</p>

<p>Este
patrón de código lo ayudará a:</p>

<p></p><ul><li>Crear
el patrón de arquitectura Backend for Frontend (BFF)</li><li>Generar
una aplicación en Node.js, Swift o Java</li><li>Generar
una aplicación con archivos para implementar en Kubernetes, Cloud Foundry o
DevOps Pipeline</li><li>Generar
una aplicación con archivos para monitoreo y seguimiento distribuido</li><li>Conectar
a servicios provisionados</li></ul><p></p>









<p>También
facilita el seguimiento de un modelo de programación Cloud Native que utiliza
las mejores prácticas de IBM para el desarrollo de aplicaciones BFF. Verá cosas
como casos de prueba, chequeo de funcionamiento y métricas en cada lenguaje de
programación.</p>

<p>Si
hace clic en <strong>Desarrollar en IBM Cloud</strong>
en la parte superior del Code Pattern, podrá aprovisionar dinámicamente los
servicios de Cloud. Esos servicios se inicializará automáticamente en su
aplicación generada. Adicione un servicio administrado de MongoDB, un servicio
de Watson o pruebas automáticas en un pipeline de DevOps personalizado.</p>

<p>&nbsp;<img src="https://acceso.ispc.edu.ar/pluginfile.php/77423/mod_book/chapter/4101/image.png" alt="" role="presentation" class="img-fluid"></p>

<p style="text-align: center;"><br><!--[endif]--></p>

<p style="text-align: left;">Figura: Arquitectura BFF,&nbsp;<u style="font-size: 1rem;"><a href="https://developer.ibm.com/es/patterns/create-backend-for-frontend-application-architecture">https://developer.ibm.com/es/patterns/create-backend-for-frontend-application-architecture</a></u></p><br clear="all">

<hr size="1" width="33%" style="text-align: left;">

<!--[endif]-->

<div id="ftn1">

<p><a href="#_ftnref1" name="_ftn1" title=""><sup><!--[if !supportFootnotes]--><sup>[1]</sup><!--[endif]--></sup></a>Modularidad, Acoplamiento y Cohesión, <u><a href="https://www.disrupciontecnologica.com/acoplamiento-y-cohesion/">https://www.disrupciontecnologica.com/acoplamiento-y-cohesion/</a></u></p>

</div>

<div id="ftn2">

<p><a href="#_ftnref2" name="_ftn2" title=""><sup><!--[if !supportFootnotes]--><sup>[2]</sup><!--[endif]--></sup></a>Sistemas monolíticos, <u><a href="https://reactiveprogramming.io/blog/es/estilos-arquitectonicos/monolitico">https://reactiveprogramming.io/blog/es/estilos-arquitectonicos/monolitico</a></u></p>

</div>

</div><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4098"><h3 class="text-center pb-5">5.6. Otros Stacks</h3><p dir="ltr" style="text-align: left;"></p><p>Hay otros stacks, y probablemente surjan nuevos en el futuro
cercano.</p>

<p>Una solución completa involucra no solo el stack, que en
ocasiones conlleva la inversión en las correspondientes licencias, sino también
las consideraciones referidas al costo de hardware, entre ellos el del servidor
físico.</p>

<p></p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77423/mod_book/chapter/4098/note-task-comment-message-edit-write_108613%20%281%29.png" alt="task" width="75" height="75" class="img-fluid atto_image_button_text-bottom"><strong>Desafíos:&nbsp;</strong>De acuerdo a los stack definidos previamente, unos proveen la construcción de aplicaciones SPA (Single Page Application) y otros MPA (Multiple Page Application). <span><span>Investiga:</span><em> ¿Cuál es la diferencia entre ellos? ¿ Cuáles son las ventajas y desventajas de cada uno? ¿Cuándo convendrá utilizar aplicaciones SPA y cuándo aplicaciones MPA?</em></span><br><p></p></div>
            </div>
    </div>
</div></div>
    </section>
</div>
<script>
//<![CDATA[
var require = {
    baseUrl : 'https://acceso.ispc.edu.ar/lib/requirejs.php/1659972264/',
    // We only support AMD modules with an explicit define() statement.
    enforceDefine: true,
    skipDataMain: true,
    waitSeconds : 0,

    paths: {
        jquery: 'https://acceso.ispc.edu.ar/lib/javascript.php/1659972264/lib/jquery/jquery-3.5.1.min',
        jqueryui: 'https://acceso.ispc.edu.ar/lib/javascript.php/1659972264/lib/jquery/ui-1.12.1/jquery-ui.min',
        jqueryprivate: 'https://acceso.ispc.edu.ar/lib/javascript.php/1659972264/lib/requirejs/jquery-private'
    },

    // Custom jquery config map.
    map: {
      // '*' means all modules will get 'jqueryprivate'
      // for their 'jquery' dependency.
      '*': { jquery: 'jqueryprivate' },
      // Stub module for 'process'. This is a workaround for a bug in MathJax (see MDL-60458).
      '*': { process: 'core/first' },

      // 'jquery-private' wants the real jQuery module
      // though. If this line was not here, there would
      // be an unresolvable cyclic dependency.
      jqueryprivate: { jquery: 'jquery' }
    }
};

//]]>
</script>
<script src="https://acceso.ispc.edu.ar/lib/javascript.php/1659972264/lib/requirejs/require.min.js"></script>
<script>
//<![CDATA[
M.util.js_pending("core/first");
require(['core/first'], function() {
require(['core/prefetch'])
;
require(["media_videojs/loader"], function(loader) {
    loader.setUp('es');
});;

M.util.js_pending('theme_boost/loader');
require(['theme_boost/loader'], function() {
  M.util.js_complete('theme_boost/loader');
});
;
M.util.js_pending('core/notification'); require(['core/notification'], function(amd) {amd.init(77423, []); M.util.js_complete('core/notification');});;
M.util.js_pending('core/log'); require(['core/log'], function(amd) {amd.setConfig({"level":"warn"}); M.util.js_complete('core/log');});;
M.util.js_pending('core/page_global'); require(['core/page_global'], function(amd) {amd.init(); M.util.js_complete('core/page_global');});
    M.util.js_complete("core/first");
});
//]]>
</script>
<script>
//<![CDATA[
M.str = {"moodle":{"lastmodified":"\u00daltima modificaci\u00f3n","name":"Nombre","error":"Error","info":"Informaci\u00f3n","yes":"S\u00ed","no":"No","cancel":"Cancelar","confirm":"Confirmar","areyousure":"\u00bfEst\u00e1 seguro?","closebuttontitle":"Cerrar","unknownerror":"Error desconocido","file":"Archivo","url":"URL","collapseall":"Colapsar todo","expandall":"Expandir todo"},"repository":{"type":"Tipo","size":"Tama\u00f1o","invalidjson":"Cadena JSON no v\u00e1lida","nofilesattached":"No se han adjuntado archivos","filepicker":"Selector de archivos","logout":"Salir","nofilesavailable":"No hay archivos disponibles","norepositoriesavailable":"Lo sentimos, ninguno de sus repositorios actuales puede devolver archivos en el formato solicitado.","fileexistsdialogheader":"El archivo existe","fileexistsdialog_editor":"Un archivo con ese nombre ha sido anexado al texto que Usted est\u00e1 editando","fileexistsdialog_filemanager":"Ya ha sido anexado un archivo con ese nombre","renameto":"Cambiar el nombre a \"{$a}\"","referencesexist":"Existen {$a} enlaces a este archivo","select":"Seleccionar"},"admin":{"confirmdeletecomments":"Est\u00e1 a punto de eliminar comentarios, \u00bfest\u00e1 seguro?","confirmation":"Confirmaci\u00f3n"},"debug":{"debuginfo":"Informaci\u00f3n de depuraci\u00f3n","line":"L\u00ednea","stacktrace":"Trazado de la pila (stack)"},"langconfig":{"labelsep":":"}};
//]]>
</script>
<script>
//<![CDATA[
(function() {Y.use("moodle-filter_mathjaxloader-loader",function() {M.filter_mathjaxloader.configure({"mathjaxconfig":"\nMathJax.Hub.Config({\n    config: [\"Accessible.js\", \"Safe.js\"],\n    errorSettings: { message: [\"!\"] },\n    skipStartupTypeset: true,\n    messageStyle: \"none\"\n});\n","lang":"es"});
});
M.util.help_popups.setup(Y);
 M.util.js_pending('random6319610f5b0ae2'); Y.on('domready', function() { M.util.js_complete("init");  M.util.js_complete('random6319610f5b0ae2'); });
})();
//]]>
</script>

</body>
</html>