
<!DOCTYPE html>

<html  dir="ltr" lang="es-wp" xml:lang="es-wp">
<head>
    <title>Guía CSS</title>
    <link rel="shortcut icon" href="https://acceso.ispc.edu.ar/pluginfile.php/1/tool_tenant/favicon/1/favicon-96x96.png" />
    <meta name="apple-itunes-app" content="app-id=1470929705, app-argument=https://acceso.ispc.edu.ar/mod/book/print.php?id=31894&amp;chapterid=0"/><link rel="manifest" href="https://acceso.ispc.edu.ar/admin/tool/mobile/mobile.webmanifest.php" /><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="moodle, Guía CSS" />
<link rel="stylesheet" type="text/css" href="https://acceso.ispc.edu.ar/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.css" /><script id="firstthemesheet" type="text/css">/** Required in order to fix style inclusion problems in IE with YUI **/</script><link rel="stylesheet" type="text/css" href="https://acceso.ispc.edu.ar/theme/workplace/wpcss.php/workplace/1659990713_1/all-1-1654194304" />
<link rel="stylesheet" type="text/css" href="https://acceso.ispc.edu.ar/mod/book/tool/print/print.css" />
<script>
//<![CDATA[
var M = {}; M.yui = {};
M.pageloadstarttime = new Date();
M.cfg = {"wwwroot":"https:\/\/acceso.ispc.edu.ar","sesskey":"Uzh6OTIEiZ","sessiontimeout":"10800","sessiontimeoutwarning":"1200","themerev":"1659990713","slasharguments":1,"theme":"workplace","iconsystemmodule":"core\/icon_system_fontawesome","jsrev":"1659972264","admin":"admin","svgicons":true,"usertimezone":"Am\u00e9rica\/Argentina\/Buenos_Aires","contextid":77425,"langrev":1661670867,"templaterev":"1658767754"};var yui1ConfigFn = function(me) {if(/-skin|reset|fonts|grids|base/.test(me.name)){me.type='css';me.path=me.path.replace(/\.js/,'.css');me.path=me.path.replace(/\/yui2-skin/,'/assets/skins/sam/yui2-skin')}};
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

<body  id="page-mod-book-print" class="format-wplist  path-mod path-mod-book chrome dir-ltr lang-es_wp yui-skin-sam yui3-skin-sam acceso-ispc-edu-ar pagelayout-embedded course-1863 context-77425 cmid-31894 category-242 ">
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
    <div class="text-center pb-3 book_title"><h1>Guía CSS</h1></div>
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
                        Guía CSS
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
                        jueves, 8 septiembre 2022, 12:30 
                    </td>
                </tr>
            </table>
        </div>
    </div>
    <div class="w-100">
        <div class="py-5"><div class="book_toc_numbered"><a name="toc"></a><h2 class="text-center pb-5">Tabla de contenidos</h2><ul><li><a title="1. Introducción" class="font-weight-bold text-decoration-none" href="#ch4137">1. Introducción</a></li><li><a title="2. ¿Qué es CSS?" class="font-weight-bold text-decoration-none" href="#ch4135">2. ¿Qué es CSS?</a></li><li><a title="3. ¿Para qué utilizar CSS?" class="font-weight-bold text-decoration-none" href="#ch4136">3. ¿Para qué utilizar CSS?</a></li><li><a title="4. Reglas CSS" class="font-weight-bold text-decoration-none" href="#ch4152">4. Reglas CSS</a></li><li><a title="5. Selectores" class="font-weight-bold text-decoration-none" href="#ch4148">5. Selectores</a><ul><li><a title="5.1. Selectores básicos" class="text-decoration-none" href="#ch4153">5.1. Selectores básicos</a></li><li><a title="5.2. Selector descendente" class="text-decoration-none" href="#ch4132">5.2. Selector descendente</a></li><li><a title="5.3. Selector de clase" class="text-decoration-none" href="#ch4147">5.3. Selector de clase</a></li><li><a title="5.4. Selector de ID" class="text-decoration-none" href="#ch4149">5.4. Selector de ID</a></li><li><a title="5.5. Selectores avanzados" class="text-decoration-none" href="#ch4139">5.5. Selectores avanzados</a></li></ul></li><li><a title="6. Herencia" class="font-weight-bold text-decoration-none" href="#ch4154">6. Herencia</a></li><li><a title="7. Agrupar reglas" class="font-weight-bold text-decoration-none" href="#ch4150">7. Agrupar reglas</a></li><li><a title="8. Formas de insertar CSS" class="font-weight-bold text-decoration-none" href="#ch4133">8. Formas de insertar CSS</a><ul><li><a title="8.1. Hojas de estilo en línea" class="text-decoration-none" href="#ch4138">8.1. Hojas de estilo en línea</a></li><li><a title="8.2. Hojas de estilo interna" class="text-decoration-none" href="#ch4130">8.2. Hojas de estilo interna</a></li><li><a title="8.3. Hojas de estilo externas" class="text-decoration-none" href="#ch4131">8.3. Hojas de estilo externas</a></li></ul></li><li><a title="9. Modelo de Cajas" class="font-weight-bold text-decoration-none" href="#ch4134">9. Modelo de Cajas</a><ul><li><a title="9.1. Dimensiones de las cajas" class="text-decoration-none" href="#ch4140">9.1. Dimensiones de las cajas</a></li><li><a title="9.2. Margen" class="text-decoration-none" href="#ch4141">9.2. Margen</a></li><li><a title="9.3. Relleno o padding" class="text-decoration-none" href="#ch4142">9.3. Relleno o padding</a></li></ul></li><li><a title="10. Web Responsive" class="font-weight-bold text-decoration-none" href="#ch4143">10. Web Responsive</a><ul><li><a title="10.1. Vista de cuadrícula" class="text-decoration-none" href="#ch4144">10.1. Vista de cuadrícula</a></li><li><a title="10.2. Media Query" class="text-decoration-none" href="#ch4145">10.2. Media Query</a></li><li><a title="10.3. Flexbox" class="text-decoration-none" href="#ch4146">10.3. Flexbox</a></li><li><a title="10.4. Desafío Final" class="text-decoration-none" href="#ch4151">10.4. Desafío Final</a></li></ul></li></ul></div></div>
    </div>
    <div class="w-100">
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4137"><h2 class="text-center pb-5">1. Introducción</h2><p dir="ltr" style="text-align: left;"><strong></strong></p><p dir="ltr"><span id="docs-internal-guid-1bd620cb-7fff-e216-eac5-3539403aa61a"><span>El gran impulso de los lenguajes de hojas de estilos se produjo con el boom de Internet y el crecimiento exponencial del lenguaje HTML. Entre la fuerte competencia de navegadores web y la falta de un estándar para la definición de los estilos, se dificultaba la creación de documentos con la misma apariencia en diferentes navegadores</span></span></p><span id="docs-internal-guid-1bd620cb-7fff-e216-eac5-3539403aa61a"><span><span style="font-size: 1rem;">A mediados de la década de 1990 el <a href="https://www.w3.org/" target="_blank">W3C</a>, encargado de crear todos los estándares relacionados con la web, propuso la creación de un lenguaje de hojas de estilos específico para el lenguaje HTML y se presentaron nueve propuestas. Las dos propuestas que se tuvieron en cuenta fueron la CHSS, Cascading HTML Style Sheets y la SSP, Stream-based Style Sheet Proposal. La propuesta CHSS fue realizada por Håkon Wium Lie y SSP fue propuesto por Bert Bos. Entre finales de 1994 y 1995 Lie y Bos se unieron para definir un nuevo lenguaje que tomaba lo mejor de cada propuesta y lo llamaron CSS, Cascading Style Sheets.&nbsp;<br></span><br></span><p dir="ltr" style="">En 1995, el W3C decidió gestionar el desarrollo y estandarización de CSS y añadió el proyecto a su grupo de trabajo de HTML. A finales de 1996, el W3C publicó la primera recomendación oficial, conocida como "CSS nivel 1". (<a href="https://www.ecured.cu/CSS" style="">https://www.ecured.cu/CSS</a>)</p><p dir="ltr" style=""></p><p><span style=""><strong>Objetivos</strong></span></p><ol><li dir="ltr" aria-level="1"><p dir="ltr" role="presentation">Crear páginas web básicas con estilos CSS.</p></li><li dir="ltr" aria-level="1"><p dir="ltr" role="presentation"><span>Incorporar conocimientos básicos del lenguaje CSS para tener una visión amplia y poder complementarlo con otros lenguajes de front-end tales como HTML.</span></p></li><li dir="ltr" aria-level="1"><p dir="ltr" role="presentation">Incorporar los conceptos básicos sobre diseño web responsive en CSS.</p></li></ol><strong></strong><br><p></p></span><br><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4135"><h2 class="text-center pb-5">2. ¿Qué es CSS?</h2><p dir="ltr" style="text-align: left;"><strong></strong></p><p dir="ltr"><span id="docs-internal-guid-1120030a-7fff-1b38-2bae-cf8f7a5be345">Hojas de estilo en cascada o CSS por sus siglas en inglés, Cascading Style Sheets, es un lenguaje que trabaja junto con HTML para proveer estilos visuales a los elementos de un documento web.</span></p><span id="docs-internal-guid-1120030a-7fff-1b38-2bae-cf8f7a5be345"><span style="font-size: 1rem;">Características:</span><br><p dir="ltr"></p><ul><li><span style="font-size: 1rem;">Ahorra trabajo. Se puede controlar el diseño de varias páginas HTML a la vez.</span></li><li><span style="font-size: 1rem;">Se pueden almacenar en archivos *.css</span></li></ul><p></p><p dir="ltr"><strong>CSS3 es la última versión estándar.</strong></p></span><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4135/note-task-comment-message-edit-write_108613.png" alt="task
" width="75" height="75" class="img-fluid atto_image_button_text-bottom"><strong>Desafío:</strong> Investiga ¿Por qué las hojas de estilo reciben el nombre "en cascada"?<br><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4136"><h2 class="text-center pb-5">3. ¿Para qué utilizar CSS?</h2><p dir="ltr" style="text-align: left;"><strong></strong></p>
<p dir="ltr">Para definir estilos en los documentos web, incluyendo el diseño, la disposición de los elementos y para responder a las variaciones en los tamaños de pantalla en cuanto a diferentes dispositivos.</p>
<h5>Ventajas</h5>
<p dir="ltr"></p><ul><li>Control centralizado de la presentación de un sitio web completo con lo que se agiliza considerablemente la actualización y mantenimiento.</li><li>Los Navegadores permiten a los usuarios especificar su propia hoja de estilo local que será aplicada a un sitio web, con lo que aumenta considerablemente la accesibilidad. Por ejemplo, personas con deficiencias visuales pueden configurar su propia hoja de estilo para aumentar el tamaño del texto o remarcar más los enlaces.</li><li>Una página puede disponer de diferentes hojas de estilo según el dispositivo que la muestre o incluso a elección del usuario. Por ejemplo, para ser impresa, mostrada en un dispositivo móvil, o ser "leída" por un sintetizador de voz.</li><li>El documento HTML en sí mismo es más claro de entender y se consigue reducir considerablemente su tamaño (siempre y cuando no se utilice estilo en línea)&nbsp;<span style="font-size: 1rem;">(<a href="https://www.ecured.cu/CSS" class="_blanktarget">https://www.ecured.cu/CSS</a>)</span></li></ul><p></p>



<p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4136/note-task-comment-message-edit-write_108613.png" alt="task" width="75" height="75"><strong>Desafío:</strong>&nbsp;De acuerdo a lo expresado arriba, CSS nos permite responder a las variaciones en los tamaños de pantalla<em>&nbsp;¿A qué se refiere? ¿Consideras este punto importante al momento de crear un sitio o aplicación web?&nbsp;</em>Busca en la web un ejemplo de sitio o aplicación web que sea capaz de responder a las variaciones en los tamaños de pantalla.&nbsp;<br></p><br><br>
<p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4152"><h2 class="text-center pb-5">4. Reglas CSS</h2><p dir="ltr" style="text-align: left;"><strong></strong></p>
<p dir="ltr"><span id="docs-internal-guid-2884ad46-7fff-0d9b-cceb-2a3680b0da49">CSS define conjunto de reglas que permiten describir cada una de las partes que componen los estilos CSS.&nbsp;</span></p>
<p dir="ltr"><span><strong><img src="https://lh3.googleusercontent.com/Nr5AzFcPX4jWNPGnid7oSFVWOAQyFHisM3arkF9mOWP_SWlKCtrq4GX5mnyvPan8EuGkoUSImGAYQYqvap2aLosLokBSbKHiE2RlYeiVWF575qe09Ckv6BOS_jZkPN5BkomnUKF0iEigkfwjqvkV" width="602" height="191"></strong><br></span></p>
<pre><span><span><span id="docs-internal-guid-aa6df30d-7fff-898c-6a96-91feb728d017" style="">Figura: Sintaxis CSS</span></span></span></pre><span><span><span style=""><ul><li><span><span><span style=""><strong>Selector:</strong> indica el elemento o elementos HTML a los que se aplica la regla CSS.
</span></span></span></li><li><span><span><span style=""><strong>Declaración:</strong> especifica los estilos que se aplican a los elementos. </span></span></span></li><li><span><span><span style=""><strong>Propiedad: </strong>permite modificar el aspecto de una característica del elemento.
</span></span></span></li><li><span><span><span style=""><strong>Valor: </strong>indica el nuevo valor de la característica modificada en el elemento.
</span></span></span></li></ul><p><br></p></span></span></span><br><br>
<p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4148"><h2 class="text-center pb-5">5. Selectores</h2><p dir="ltr" style="text-align: left;"><strong></strong></p>

<p>Nos indican a qué elemento HTML hay que aplicar el estilo.&nbsp;<br>
</p>
<p><span>Una misma regla puede aplicarse a varios selectores y, a un mismo selector se le pueden aplicar varias reglas.<br></span><span>Para mayor información referirse a&nbsp;<a href="https://www.w3.org/wiki/CSS_/_Selectores_CSS#Lista_de_selectores_css&nbsp" class="_blanktarget">https://www.w3.org/wiki/CSS_/_Selectores_CSS#Lista_de_selectores_css&nbsp</a>;<br></span></p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4148/1455554318_line-20_icon-icons.com_53327.png" alt="video
" width="75" height="75" class="img-fluid atto_image_button_text-bottom">A continuación, los invitamos a mirar un video explicativo:&nbsp;<br><br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/YCtSesqUDl8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe><br><br>Visita en el siguiente enlace para acceder a la información sobre selectores que nos provee la <strong>W3C</strong>:&nbsp;<a href="https://www.w3.org/wiki/CSS_/_Selectores_CSS#Lista_de_selectores_css" class="_blanktarget">https://www.w3.org/wiki/CSS_/_Selectores_CSS#Lista_de_selectores_css</a><br>
<p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4153"><h3 class="text-center pb-5">5.1. Selectores básicos</h3><p dir="ltr" style="text-align: left;"></p><p><strong>Selector universal</strong>: Se utiliza para seleccionar todos los elementos de la página.</p><p></p><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image.png" alt="" role="presentation"><br><br><strong>Selector de tipo o etiqueta</strong>:&nbsp;Selecciona todos los elementos de la página cuya etiqueta HTML coincide con el valor del selector.<br><br><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%281%29.png" alt="" role="presentation"><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4132"><h3 class="text-center pb-5">5.2. Selector descendente</h3><p dir="ltr" style="text-align: left;">Selecciona los elementos que se encuentran dentro de otros elementos. Se encuentra entre las etiquetas de apertura y de cierre del otro elemento.</p><p dir="ltr" style="text-align: left;"><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%282%29.png" alt="" role="presentation"><br><span style="font-size: 1rem;"><br></span></p><p dir="ltr" style="text-align: left;"><span style="font-size: 1rem;">La <strong>sintaxis formal</strong> del selector descendente se muestra a continuación:</span><br></p><p dir="ltr" style="text-align: left;"><strong><span class="" style="color: rgb(125, 159, 211);">elemento1 elemento2 elemento3 ... elementoN</span></strong></p><p dir="ltr" style="text-align: left;"><span>Ejemplo:</span></p><p dir="ltr" style="text-align: left;">Si el código HTML de la página es el siguiente:</p><p dir="ltr" style="text-align: left;"><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%284%29.png" alt="" role="presentation"><br><span style="font-size: 1rem;"><br></span></p><p dir="ltr" style="text-align: left;"><span style="font-size: 1rem;">El selector p span selecciona tanto texto1 como texto2. ¿Por qué sucede esto?&nbsp;Simplemente porque es un selector descendente. Es decir,&nbsp;el elemento no tiene que ser descendiente directo. La única condición es que un elemento debe estar dentro de otro elemento, sin importar el nivel de profundidad en el que se encuentre.</span></p><p dir="ltr" style="text-align: left;">Los selectores descendentes nos permiten aumentar la precisión del selector de tipo o etiqueta. Así, utilizando el selector descendente podemos aplicar diferentes estilos a los elementos del mismo tipo (<u><a href="https://uniwebsidad.com/libros/css/capitulo-2/selectores-basicos">https://uniwebsidad.com/libros/css/capitulo-2/selectores-basicos</a>)</u><br></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4147"><h3 class="text-center pb-5">5.3. Selector de clase</h3><p dir="ltr" style="text-align: left;"></p><h4><span>Selector de clase o selector Class</span></h4>Si consideramos el siguiente código HTML de ejemplo:<br><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%285%29.png" alt="" role="presentation"><p></p><p dir="ltr" style="text-align: left;"><em><strong>¿Cómo podemos aplicar estilos CSS sólo al primer párrafo?</strong></em></p><p dir="ltr" style="text-align: left;">El selector universal (*) no se puede utilizar porque seleccionaría todos los elementos de la página. El selector de tipo o etiqueta (p) tampoco se puede utilizar porque seleccionaría todos los párrafos. Por último, el selector descendente (body p) tampoco se puede utilizar porque todos los párrafos se encuentran en el mismo sitio.</p><p dir="ltr" style="text-align: left;">Una de las soluciones más sencillas para aplicar estilos a un solo elemento de la página consiste en utilizar el atributo class de HTML sobre ese elemento para indicar directamente la regla CSS que se le debe aplicar:</p><p dir="ltr" style="text-align: left;"><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%286%29.png" alt="" role="presentation"><br></p><p>A continuación, creamos en el archivo CSS una nueva regla llamada&nbsp;<strong>destacado</strong>&nbsp;con todos los estilos que vamos a aplicar al elemento. Para que el navegador no confunda este selector con los otros tipos de selectores, pre fijamos el valor del atributo class con un punto (.) tal como vemos en la siguiente línea:</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%287%29.png" alt="" role="presentation"><p dir="ltr"></p><p></p><span style="font-size: 1rem;">El selector&nbsp;</span><strong style="font-size: 1rem;">.destacado</strong><span style="font-size: 1rem;">&nbsp;se interpreta como "cualquier elemento de la página cuyo atributo class sea igual a&nbsp;</span><strong style="font-size: 1rem;">destacado</strong><span style="font-size: 1rem;">", por lo que solamente el primer párrafo del anterior ejemplo cumple esa condición.<br><span style="font-size: 1rem;"><br>Este tipo de selectores son los más utilizados junto con los selectores de ID que veremos a continuación. La principal característica de este selector es que en una misma página HTML varios elementos diferentes pueden utilizar el mismo valor en el atributo class:<br></span><br></span><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%288%29.png" alt="" role="presentation"><br><br><p>Los&nbsp;<strong>selectores de clase</strong>&nbsp;resultan imprescindibles para diseñar páginas web complejas, ya que nos permiten disponer de una precisión total al seleccionar los elementos. Además, estos selectores nos permiten reutilizar los mismos estilos para varios elementos diferentes.</p><p><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%289%29.png" alt="" role="presentation"><br></p><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%2810%29.png" alt="" role="presentation"><br><br><p>El elemento &lt;span&gt; tiene un atributo&nbsp;<strong>class="error"</strong>, por lo que se le aplican las reglas CSS indicadas por el selector&nbsp;<strong>.error</strong>. Por su parte, el elemento &lt;div&gt; tiene un atributo&nbsp;<strong>class="aviso"</strong>, por lo que su estilo es el que define las reglas CSS del selector&nbsp;<strong>.aviso</strong>.</p><p><span style="font-size: 1rem;">En ciertos casos, es necesario restringir el alcance del selector de clase. Si utilizamos el ejemplo anterior:</span></p><p><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%2811%29.png" alt="" role="presentation"><br></p><p><strong><em>¿Cómo podemos aplicar estilos solamente al párrafo cuyo atributo class sea igual a destacado?</em></strong></p><p>Combinando el selector de tipo y el selector de clase, se obtiene un selector mucho más específico:</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%2812%29.png" alt="" role="presentation"><br><br><p>Interpretamos al selector p.destacado como "aquellos elementos de tipo &lt;p&gt; que dispongan de un atributo class con valor destacado". De la misma forma, el selector a.destacado solamente seleccionaría los enlaces cuyo atributo class sea igual a destacado.</p><p>De lo anterior deducimos que el atributo .destacado es equivalente a *.destacado, por lo que todos los diseñadores obvian el símbolo * al escribir un selector de clase normal.</p><p>No debemos confundir el selector de clase con los selectores anteriores:</p><p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4147/code.png?time=1661179626431" alt="code" width="937" height="414" class="img-fluid atto_image_button_text-bottom"><br></p><p>Para completar, es posible aplicar los estilos de varias clases CSS sobre un mismo elemento. La sintaxis es similar, pero los diferentes valores del atributo class se separan con espacios en blanco.</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%2813%29.png" alt="" role="presentation"><br><br><p>Al párrafo anterior le aplicamos los estilos definidos en las reglas&nbsp;<b>.especial</b>,<b>&nbsp;.destacado</b>&nbsp;y&nbsp;<b>.error</b>, por lo que en el siguiente ejemplo, el texto del párrafo se vería de color rojo, en negrita y con un tamaño de letra de 15 píxel:</p><p><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%2814%29.png" alt="" role="presentation"><br></p><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%2815%29.png" alt="" role="presentation"><br><br><p>Si un elemento dispone de un atributo class con más de un valor, es posible utilizar un selector más avanzado:</p><p><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%2816%29.png" alt="" role="presentation"><br></p><p><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%2817%29.png" alt="" role="presentation"><br></p><p>En el ejemplo anterior, el color de la letra del texto es azul y no rojo. Esto se debe a que hemos utilizado un selector de clase múltiple .error.destacado, que se interpreta como "aquellos elementos de la página que dispongan de un atributo class con al menos los valores error y destacado"&nbsp;(<u><a href="https://uniwebsidad.com/libros/css/capitulo-2/selectores-basicos">https://uniwebsidad.com/libros/css/capitulo-2/selectores-basicos</a></u>)</p><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4149"><h3 class="text-center pb-5">5.4. Selector de ID</h3><p dir="ltr" style="text-align: left;"></p><h5>Selectores de ID</h5><p>En ocasiones, es necesario aplicar estilos CSS a un único elemento de la página. Aunque puede utilizarse un selector de clase para aplicar estilos a un único elemento, existe otro selector más eficiente en este caso.</p><p>El selector de ID permite seleccionar un elemento de la página a través del valor de su atributo id. Este tipo de selectores sólo seleccionan un elemento de la página porque el valor del atributo id no se puede repetir en dos elementos diferentes de una misma página.</p><p>La sintaxis de los selectores de ID es muy parecida a la de los selectores de clase, salvo que se utiliza el símbolo de la almohadilla (#) en vez del punto (.) como prefijo del nombre de la regla CSS:</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%2818%29.png" alt="" role="presentation"><br><br><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%2819%29.png" alt="" role="presentation"><br><br><p>En el ejemplo anterior, el selector #destacado solamente selecciona el segundo párrafo (cuyo atributo id es igual a destacado).</p><p>La principal diferencia entre este tipo de selector y el selector de clase tiene que ver con HTML y no con CSS. En una misma página, el valor del atributo id debe ser único, de forma que dos elementos diferentes no pueden tener el mismo valor de id. Sin embargo, el atributo class no es obligatorio que sea único, de forma que muchos elementos HTML diferentes pueden compartir el mismo valor para su atributo class.</p><p>De esta forma, la recomendación general es la de utilizar el selector de ID cuando se quiere aplicar un estilo a un solo elemento específico de la página y utilizar el selector de clase cuando queremos aplicar un estilo determinado a varios elementos diferentes de la página HTML.</p><p>Al igual que los selectores de clase, en este caso también podemos restringir el alcance del selector mediante la combinación con otros selectores. El siguiente ejemplo aplica la regla CSS solamente al elemento de tipo &lt;p&gt; que tenga un atributo id igual al indicado:</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/image%20%2820%29.png" alt="" role="presentation"><br><br><p>A primera vista, restringir el alcance de un selector de ID puede parecer absurdo. En realidad, un selector de tipo p#aviso sólo tiene sentido cuando el archivo CSS se aplica sobre muchas páginas HTML diferentes.</p><p>En este caso, algunas páginas pueden disponer de elementos con un atributo id igual a aviso y que no sean párrafos, por lo que la regla anterior no se aplica sobre esos elementos.</p><p>No debe confundirse el selector de ID con los selectores anteriores:</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3941/code2.png" alt="code2" width="936" height="380"><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4139"><h3 class="text-center pb-5">5.5. Selectores avanzados</h3><p dir="ltr" style="text-align: left;"></p><p>Se trata de un selector similar
al selector descendente, pero muy diferente en su funcionamiento. Se utiliza
para seleccionar un elemento que es hijo directo de otro elemento y se indica
mediante el "signo de mayor que" (&gt;):</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4139/image.png" alt="" role="presentation" class="img-fluid"><br><br><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4139/image%20%281%29.png" alt="" role="presentation" class="img-fluid"><br><br><p>En el ejemplo anterior, el
selector p &gt; span se interpreta como "cualquier elemento &lt;span&gt;
que sea hijo directo de un elemento &lt;p&gt;", por lo que el primer
elemento &lt;span&gt; cumple la condición del selector. Sin embargo, el segundo
elemento &lt;span&gt; no la cumple porque es descendiente pero no es hijo
directo de un elemento &lt;p&gt;.</p>

<p><span style="font-size: 1rem;">El siguiente ejemplo muestra las
diferencias entre el selector descendente y el selector de hijos:</span></p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4139/image%20%282%29.png" alt="" role="presentation" class="img-fluid"><br><br><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4139/image%20%283%29.png" alt="" role="presentation" class="img-fluid"><br><br><p>El primer selector es de tipo
descendente y por tanto se aplica a todos los elementos &lt;a&gt; que se
encuentran dentro de elementos &lt;p&gt;. En este caso, los estilos de este
selector se aplican a los dos enlaces.</p><p>Por otra parte, el selector de
hijos obliga a que el elemento &lt;a&gt; sea hijo directo de un elemento
&lt;p&gt;. Por lo tanto, los estilos del selector p &gt; a no se aplican al
segundo enlace del ejemplo anterior.&nbsp;<span style="font-size: 1rem;">(</span><u style="font-size: 1rem;"><a href="https://uniwebsidad.com/libros/css/capitulo-2/selectores-avanzados">https://uniwebsidad.com/libros/css/capitulo-2/selectores-avanzados</a></u><span style="font-size: 1rem;">)</span></p><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3938/note-task-comment-message-edit-write_108613.png" alt="task
" width="75" height="75"><strong>Desafío: </strong>A fin de ejercitarnos en el dominio de selectores, te invitamos a jugar&nbsp;<strong><a href="https://flukeout.github.io/" target="_blank" rel="noopener" style=""><span class="" style="color: rgb(239, 69, 64);">CSS Diner</span></a><span class="" style="color: rgb(239, 69, 64);">!</span></strong>&nbsp;<br><strong>Nota:</strong> Lee bien las instrucciones a la derecha de la pantalla. Revisa el código HTML ya que, utiliza etiquetas que son propias del juego.&nbsp;<br><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4139/image%20%285%29.png" alt="" role="presentation" class="img-fluid"><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4154"><h2 class="text-center pb-5">6. Herencia</h2><p dir="ltr" style="text-align: left;">Cuando se establece el valor de alguna propiedad en un elemento, todos sus descendientes heredan inicialmente ese mismo valor.<br></p><p dir="ltr" style="text-align: left;"><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4154/image.png" alt="" role="presentation" class="img-fluid"><br></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4150"><h2 class="text-center pb-5">7. Agrupar reglas</h2><p dir="ltr">CSS permite agrupar todas las reglas individuales en una sola regla con un selector múltiple.</p><p dir="ltr">En CSS es habitual agrupar las propiedades comunes de varios elementos en una única regla CSS y posteriormente definir las propiedades específicas</p><p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4150/image.png" alt="" role="presentation" class="img-fluid"><br></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4133"><h2 class="text-center pb-5">8. Formas de insertar CSS</h2><p dir="ltr">En CSS existen tres formas para insertar los estilos en el documento HTML:</p><p dir="ltr"><ul><li>En línea.</li><li>Interna.</li><li>Externa.</li></ul></p><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4138"><h3 class="text-center pb-5">8.1. Hojas de estilo en línea</h3><p dir="ltr" style="text-align: left;"></p><div><div><p dir="ltr"><span style="font-size: 1rem;">Utilizamos hojas de estilo en línea cuando incluimos CSS en los mismos elementos HTML.</span><br></p><p dir="ltr">Esta forma para incluir estilos CSS en documentos HTML es el menos recomendado, ya que es una manera muy dura de establecer estilos. Esta forma es la más específica para introducir estilos y se debe hacer elemento por elemento.</p><p dir="ltr">Debido a que los estilos en línea son los estilos más específicos, pueden anular a otros estilos definidos. También niegan uno de los aspectos más importantes de CSS que es la capacidad de crear estilos para muchas páginas web desde un único archivo CSS central para de esta manera hacer que las futuras actualizaciones y cambios de estilo sean mucho más fáciles de gestionar.<br></p><p></p><p>Si sólo tuviéramos que utilizar estilos en línea, nuestros documentos se complejizarán rápidamente y se tornarán muy difíciles de mantener. Ya que cualquier cambio en la estética del sitio web significará cambiar los estilos en cada uno de los elementos HTML de cada página.</p><p>&nbsp;Esta forma de incluir CSS directamente en los elementos HTML no se debería utilizar, con la excepción de situaciones muy exclusivas.</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3949/image.png" alt="" role="presentation"><br><p></p></div></div><div><a title="Anterior: 7. Agrupar reglas" href="https://acceso.ispc.edu.ar/mod/book/view.php?id=31894&amp;chapterid=4150"><i title="Anterior: 7. Agrupar reglas" aria-label="Anterior: 7. Agrupar reglas"></i></a></div><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4130"><h3 class="text-center pb-5">8.2. Hojas de estilo interna</h3><p dir="ltr" style="text-align: left;"></p><p>Utilizamos hojas de estilo
interna cuando insertamos CSS en el mismo documento HTML.</p>

<p>Estos estilos se definen en la
cabecera del documento HTML, exclusivamente dentro del elemento &lt;head&gt; y
para definirlos empleamos el elemento &lt;style&gt;.</p>

<p>Fundamentalmente empleamos este
método cuando definimos un número pequeño de estilos o cuando queremos incluir
estilos específicos en una determinada página HTML para que completen los
estilos que incluimos por defecto en todas las páginas del sitio web.</p>

<p>El principal inconveniente de
usar estilos internos para todo el sitio web, es que si queremos hacer una
modificación en los estilos definidos, es necesario modificar todas las páginas
que incluyen el estilo que vayamos a modificar.</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4130/image.png" alt="" role="presentation" class="img-fluid"><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4131"><h3 class="text-center pb-5">8.3. Hojas de estilo externas</h3><p dir="ltr" style="text-align: left;"></p><p>Utilizamos hojas de estilo
externas cuando definimos un archivo CSS externo al html.</p>

<p>En este caso, todos los estilos
CSS se incluyen en un archivo de tipo CSS donde las páginas HTML lo enlazan
mediante la etiqueta &lt;link&gt;. Un archivo de tipo CSS no es más que un
simple archivo de texto cuya extensión es .css.</p>

<p>Se pueden crear todos los
archivos CSS que sean necesarios y cada página HTML puede enlazar tantos
archivos CSS como se necesite.</p>

<p>&nbsp;<span style="font-size: 1rem;">A continuación veremos el paso a
paso para definir CSS externos.</span></p><p><strong>Paso 1 - </strong>Creamos un archivo de
texto y le añadimos solamente la siguiente línea.</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4131/image.png" alt="" role="presentation" class="img-fluid"><br><br><p><strong>Paso 2</strong> - Guardamos el archivo de
texto con el nombre estilos.css, luego ponemos especial atención a que el
archivo tenga extensión .css y no .txt. </p>

<p>Para esto podemos crear una
carpeta que se llame CSS al mismo nivel que la carpeta HTML y guardar el
archivo dentro de la carpeta CSS.</p>

<p><strong>Paso 3</strong> - En la página HTML
enlazamos el archivo CSS externo mediante la etiqueta &lt;link&gt;</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4131/image%20%281%29.png" alt="" role="presentation" class="img-fluid"><br><br><p>A la hora de ejecutar el sitio
web en un navegador, cuando el navegador carga la página HTML del ejemplo
anterior, antes de mostrar sus contenidos, también descarga los archivos CSS
externos enlazados mediante la etiqueta &lt;link&gt; y aplica los estilos a los
contenidos de la página.</p>

<p><span style="font-size: 1rem;">Normalmente, la etiqueta
&lt;link&gt; incluye cuatro atributos cuando enlaza un archivo CSS:</span><br></p>

<p></p><ul><li><strong style="font-size: 1rem;"><i>rel:</i></strong><span style="font-size: 1rem;"> indica el tipo de
relación que existe entre el recurso enlazado (en este caso, el archivo CSS) y
la página HTML. Para los archivos CSS, siempre se utiliza el valor stylesheet</span></li><li><strong><i>type: </i></strong>indica el tipo de
recurso enlazado. Sus valores están estandarizados y para los archivos CSS su
valor siempre es text/css</li><li><strong><i>href:</i></strong> indica la URL del
archivo CSS que contiene los estilos. La URL indicada puede ser relativa o
absoluta y puede apuntar a un recurso interno o externo al sitio web.</li><li><strong><i>media:</i></strong> indica el medio en
el que se van a aplicar los estilos del archivo CSS.</li></ul><p></p>





<p>De todas las formas de incluir
CSS en las páginas HTML, las hojas de estilo externas son las más utilizadas.
La principal ventaja es que se puede incluir un mismo archivo CSS en multitud
de páginas HTML, por lo que se garantiza la aplicación homogénea de los mismos
estilos a todas las páginas que forman un sitio web.</p>

<p><span style="font-size: 1rem;">Con esta forma, el mantenimiento
del sitio web se simplifica al máximo, ya que un solo cambio en un solo archivo
CSS permite variar de forma instantánea los estilos de todas las páginas HTML
que enlazan ese archivo.</span></p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4131/note-task-comment-message-edit-write_108613.png" alt="task" width="75" height="75" class="img-fluid atto_image_button_text-bottom"><strong>Desafío: </strong>&nbsp;¿Cuál es la diferencia entre estas formas de insertar CSS? ¿Cuál conviene utilizar?&nbsp;<br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4134"><h2 class="text-center pb-5">9. Modelo de Cajas</h2><p dir="ltr" style="text-align: left;"></p><p></p><p></p><p>Tal como dijimos en la unidad de
HTML, si hacemos una analogía con una estructura de cajas de cartón, podemos
decir que hay ciertas cajas que van dentro de otras y ciertas cajas que van una
al lado de otra.</p>

<p>El modelo de cajas o "box
model" es seguramente la característica más importante del lenguaje de
hojas de estilos CSS, ya que condiciona el diseño de todas las páginas web. El
modelo de cajas es el comportamiento de CSS que hace que todos los elementos de
las páginas sean representados mediante cajas rectangulares.</p>

<p>&nbsp;<span style="font-size: 1rem;">Cada vez que se inserta un
elemento HTML, se crea una nueva caja rectangular que encierra los contenidos
de ese elemento. La siguiente imagen muestra tres cajas rectangulares que crean
los tres elementos HTML de una porción de página de ejemplo.</span></p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4134/image%20%281%29.png" alt="" role="presentation" class="img-fluid"><br><p></p><ul><li><span style="font-size: 1rem;"><strong>Content (contenido)</strong>: se trata del contenido HTML del
elemento (las palabras de un párrafo, una imagen, el texto de una lista de
elementos, etc.)</span></li><li><strong>Padding
(relleno)</strong>: espacio libre opcional existente entre el contenido y el borde.</li><li><strong>Border
(borde):</strong> línea que encierra completamente el contenido y su relleno.</li><li><span><strong>Background
image (Imagen de fondo):</strong></span> imagen que se muestra por detrás del contenido y el
espacio de relleno.</li><li><strong>Color
de fondo (background color):</strong> color que se muestra por detrás del contenido y el
espacio de relleno.</li><li><strong>Margin
(margen): </strong>separación opcional existente entre la caja y el resto de cajas adyacentes.</li></ul><p></p>









<br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4140"><h3 class="text-center pb-5">9.1. Dimensiones de las cajas</h3><p dir="ltr" style="text-align: left;"></p><h4>Anchura</h4>

<p>Para los elementos de bloque y
las imágenes, la propiedad width (anchura) permite establecer la anchura
directamente mediante una medida.</p>

<p><strong>&nbsp;<span style="font-size: 1rem;">Anchura = width</span></strong></p>

<p>En CSS:</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4140/image.png" alt="" role="presentation" class="img-fluid"><br><br><p>En HTML:</p><p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4140/image%20%281%29.png" alt="" role="presentation" class="img-fluid"><br></p><p></p><p>Si se utilizan unidades de
medida, los valores indicados no pueden ser negativos. Si en vez de una unidad
de medida se indica un porcentaje, la referencia de ese valor es la anchura del
elemento que lo contiene. El valor <strong><i>inherit </i></strong>indica que la anchura del
elemento se hereda de su elemento padre.</p>

<p>Si se establece la anchura de un
elemento con la unidad de medida <strong><i>em</i></strong>, el valor indicado toma como
referencia el tamaño de letra del propio elemento.</p>

<p>El valor <strong><i>auto</i></strong> es el valor por
defecto de la anchura de todos los elementos. En este caso, el navegador determina
la anchura de cada elemento teniendo en cuenta, entre otros, el tipo de
elemento que se trata (de bloque o en línea), el sitio disponible en la
pantalla del navegador y los contenidos de los elementos.</p><h4>Altura</h4><p>Al igual que sucede con width, la
propiedad height (altura) no admite valores negativos. Si se indica un
porcentaje, se toma como referencia la altura del elemento padre. Si el
elemento padre no tiene una altura definida explícitamente, se asigna el valor <strong><i>auto </i></strong>a
la altura.</p>

<p>&nbsp;<span style="font-size: 1rem;">El valor </span><strong style="font-size: 1rem;"><i>inherit </i></strong><span style="font-size: 1rem;">indica que la
altura del elemento se hereda de su elemento padre. El valor </span><strong style="font-size: 1rem;"><i>auto</i></strong><span style="font-size: 1rem;">,
que es el que se utiliza si no se establece de forma explícita un valor a esta
propiedad, indica que el navegador debe calcular automáticamente la altura del
elemento, teniendo en cuenta sus contenidos y el sitio disponible en la página.</span></p>

<p>&nbsp;<span style="font-size: 1rem;"><strong>Altura = height</strong></span></p><p>En CSS:</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4140/image%20%282%29.png" alt="" role="presentation" class="img-fluid"><br><br><p>En HTML:</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4140/image%20%283%29.png" alt="" role="presentation" class="img-fluid"><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4141"><h3 class="text-center pb-5">9.2. Margen</h3><p dir="ltr" style="text-align: left;"></p><p>CSS define cuatro propiedades
para controlar cada uno de los márgenes horizontales y verticales de un
elemento.</p>

<p></p><ul><li><span style="font-size: 1rem;"><strong>margin-top: </strong>Margen
superior</span></li><li><strong>margin-right: </strong>Margen derecho</li><li><strong>margin-bottom:</strong> Margen inferior </li><li><strong>margin-left: </strong>Margen izquierdo</li></ul><p></p>







<p>&nbsp;<span style="font-size: 1rem;">Cada una de las propiedades
establece la separación entre el borde lateral de la caja y el resto de cajas
adyacentes:</span></p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4141/image.png" alt="" role="presentation" class="img-fluid"><br><p>Los márgenes verticales
(margin-top y margin-bottom) sólo se pueden aplicar a los elementos de bloque y
las imágenes, mientras que los márgenes laterales (margin-left y margin-right)
se pueden aplicar a cualquier elemento.</p>En CSS:<br><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4141/image%20%281%29.png" alt="" role="presentation" class="img-fluid"><br><br>Alternativa:&nbsp;<br><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4141/image%20%282%29.png" alt="" role="presentation" class="img-fluid"><br><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4142"><h3 class="text-center pb-5">9.3. Relleno o padding</h3><p dir="ltr" style="text-align: left;"></p><p>Relleno o padding. CSS define
cuatro propiedades para controlar cada uno de los espacios de relleno
horizontales y verticales de un elemento.</p>

<p></p><ul><li><span style="font-size: 1rem;">padding-top: Relleno superior</span></li><li>padding-right: Relleno derecho</li><li>padding-bottom: Relleno inferior</li><li>padding-left: Relleno izquierdo</li></ul><p></p>





<img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4142/image.png" alt="" role="presentation" class="img-fluid"><br><br>Ejemplo:&nbsp;<br><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4142/image%20%281%29.png" alt="" role="presentation" class="img-fluid"><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4143"><h2 class="text-center pb-5">10. Web Responsive</h2><p dir="ltr" style="text-align: left;"></p><p>El diseño web responsive hace que
nuestra página web se vea bien en todos los dispositivos utilizando sólo los
lenguajes HTML y CSS. El diseño web responsive no es un programa ni un
JavaScript.</p>

<p>Con el diseño web responsive las
páginas web se pueden ver utilizando muchos dispositivos diferentes:
computadoras de escritorio, tabletas y teléfonos. La página web debe verse bien
y ser fácil de usar, independientemente del dispositivo.</p>

<p>El concepto fundamental es que
las páginas web no deben omitir información para adaptarse a dispositivos más
pequeños, sino adaptar su contenido para así poder adaptarse a cualquier
dispositivo. En la siguiente imagen observamos este concepto.</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4143/image.png" alt="" role="presentation" class="img-fluid"><br>Fuente:&nbsp;<p><u><a href="https://www.w3schools.com/css/css_rwd_intro.asp">https://www.w3schools.com/css/css_rwd_intro.asp</a></u></p><p></p><h4>¿Qué es el Viewport?</h4><p>La ventana gráfica o viewport en
inglés, es el área visible para el usuario de una página web y varía según el
dispositivo. El viewport será más pequeño en un teléfono móvil que en una
pantalla de computadora.</p>

<p>Antes de las tabletas y los
teléfonos móviles, las páginas web se diseñaron sólo para pantallas de
computadora, y era común que las páginas web tuvieran un diseño estático y un
tamaño fijo. Luego, cuando comenzamos a navegar por Internet usando tabletas y
teléfonos móviles, las páginas web de tamaño fijo eran demasiado grandes para
caber en el viewport. Para solucionar esto, los navegadores, en esos
dispositivos, redujeron la página web completa para adaptarse a la pantalla.</p><h4><span style="font-weight: normal;">Configuración</span></h4><p>HTML5 introdujo un método para
permitir que los diseñadores web tomen el control del viewport, a través de la
etiqueta &lt;meta&gt;. Para ello debemos incluir el siguiente elemento
&lt;meta&gt; de ventana gráfica en todas nuestras páginas web:</p>

<p>&nbsp;<img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4143/image%20%281%29.png" alt="" role="presentation" class="img-fluid"></p><p>Esto le da al navegador
instrucciones sobre cómo controlar las dimensiones y la escala de la página.</p>

<p></p><ul><li><span style="font-size: 1rem;">La propiedad width=device-width
establece el ancho de la página para seguir el ancho de la pantalla del
dispositivo (que variará según el dispositivo).</span></li><li>La propiedad&nbsp; initial-scale=1.0 establece el nivel de zoom
inicial cuando el navegador carga la página por primera vez.</li></ul><p></p>



<p></p><h4>Tamaño&nbsp;</h4><p>Debemos tener en cuenta que los
usuarios están acostumbrados a desplazarse por los sitios web verticalmente en
dispositivos móviles y de escritorio, <b><i>¡pero no están acostumbrados a desplazarse
horizontalmente!</i></b></p>

<p>Por lo tanto, si el usuario se ve
obligado a desplazarse horizontalmente o alejarse, para ver toda la página web,
la experiencia del usuario se torna deficiente.</p><h5>Algunas reglas adicionales a seguir:</h5>

<p><ol><li>NO utilizar elementos grandes
de ancho fijo: por ejemplo, si una imagen se muestra con un ancho más ancho que
la ventana, puede hacer que la ventana se desplace horizontalmente. Recuerde
ajustar este contenido para que se ajuste al ancho del viewport.</li><li>NO permitir que el contenido
dependa de un ancho de ventana en particular para renderizarse adecuadamente.
Las dimensiones y el ancho de la pantalla en píxeles varían ampliamente entre
dispositivos, el contenido no debe depender de un ancho de ventana en
particular para renderizarse bien.</li><li>Usar media queries para
aplicar diferentes estilos para pantallas pequeñas y grandes. Establecer anchos
CSS absolutos grandes para elementos de página hará que el elemento sea
demasiado ancho para el viewport en un dispositivo más pequeño. En su lugar,
considerar usar valores de ancho relativo, como ancho: 100%. Además, tener
cuidado con el uso de valores de posicionamiento absolutos grandes. Puede hacer
que el elemento se salga del viewport en dispositivos pequeños.</li></ol></p>



<br><p></p><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4144"><h3 class="text-center pb-5">10.1. Vista de cuadrícula</h3><p dir="ltr" style="text-align: left;"></p><h4>¿Qué es una vista de cuadrícula?</h4>

<p>Muchas páginas web se basan en
una vista de cuadrícula, lo que significa que la página está dividida en
columnas. Usar una vista de cuadrícula es muy útil al diseñar páginas web.
Facilita la colocación de elementos en la página.&nbsp;</p><br><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4144/image%20%281%29.png" alt="" role="presentation" class="img-fluid"><br>Fuente:&nbsp;&nbsp;<u style="font-size: 1rem;"><a href="https://www.w3schools.com/css/css_rwd_grid.asp">https://www.w3schools.com/css/css_rwd_grid.asp</a><br></u><br><!--[if !supportAnnotations]-->

<script language="JavaScript"><!--
function msoCommentShow(anchor_id, com_id)
{
	if(msoBrowserCheck()) 
		{
		c = document.all(com_id);
		a = document.all(anchor_id);
		if (null != c && null == c.length && null != a && null == a.length)
			{
			var cw = c.offsetWidth;
			var ch = c.offsetHeight;
			var aw = a.offsetWidth;
			var ah = a.offsetHeight;
			var x  = a.offsetLeft;
			var y  = a.offsetTop;
			var el = a;
			while (el.tagName != "BODY") 
				{
				el = el.offsetParent;
				x = x + el.offsetLeft;
				y = y + el.offsetTop;
				}
			var bw = document.body.clientWidth;
			var bh = document.body.clientHeight;
			var bsl = document.body.scrollLeft;
			var bst = document.body.scrollTop;
			if (x + cw + ah / 2 > bw + bsl && x + aw - ah / 2 - cw >= bsl ) 
				{ c.style.left = x + aw - ah / 2 - cw; }
			else 
				{ c.style.left = x + ah / 2; }
			if (y + ch + ah / 2 > bh + bst && y + ah / 2 - ch >= bst ) 
				{ c.style.top = y + ah / 2 - ch; }
			else 
				{ c.style.top = y + ah / 2; }
			c.style.visibility = "visible";
}	}	}
function msoCommentHide(com_id) 
{
	if(msoBrowserCheck())
		{
		c = document.all(com_id);
		if (null != c && null == c.length)
		{
		c.style.visibility = "hidden";
		c.style.left = -1000;
		c.style.top = -1000;
		} } 
}
function msoBrowserCheck()
{
	ms = navigator.appVersion.indexOf("MSIE");
	vers = navigator.appVersion.substring(ms + 5, ms + 6);
	ie4 = (ms > 0) && (parseInt(vers) >= 4);
	return ie4;
}
if (msoBrowserCheck())
{
	document.styleSheets.dynCom.addRule(".msocomanchor","background: infobackground");
	document.styleSheets.dynCom.addRule(".msocomoff","display: none");
	document.styleSheets.dynCom.addRule(".msocomtxt","visibility: hidden");
	document.styleSheets.dynCom.addRule(".msocomtxt","position: absolute");
	document.styleSheets.dynCom.addRule(".msocomtxt","top: -1000");
	document.styleSheets.dynCom.addRule(".msocomtxt","left: -1000");
	document.styleSheets.dynCom.addRule(".msocomtxt","width: 33%");
	document.styleSheets.dynCom.addRule(".msocomtxt","background: infobackground");
	document.styleSheets.dynCom.addRule(".msocomtxt","color: infotext");
	document.styleSheets.dynCom.addRule(".msocomtxt","border-top: 1pt solid threedlightshadow");
	document.styleSheets.dynCom.addRule(".msocomtxt","border-right: 2pt solid threedshadow");
	document.styleSheets.dynCom.addRule(".msocomtxt","border-bottom: 2pt solid threedshadow");
	document.styleSheets.dynCom.addRule(".msocomtxt","border-left: 1pt solid threedlightshadow");
	document.styleSheets.dynCom.addRule(".msocomtxt","padding: 3pt 3pt 3pt 3pt");
	document.styleSheets.dynCom.addRule(".msocomtxt","z-index: 100");
}
// --></script>
<!--[endif]-->







<p>Una vista de cuadrícula
responsive tiene 12 columnas y tiene un ancho total del 100%, y se encogerá y
expandirá a medida que cambie el tamaño de la ventana del navegador.<span style="font-size: 1rem;">&nbsp;</span><span style="font-size: 1rem;">Para mayor información acerca de la vista de
cuadrículas, sugerimos ver el ejemplo de la W3Schools </span><a href="https://www.w3schools.com/css/css_rwd_grid.asp#:~:text=Responsive%20Grid%20View-,Building%20a%20Responsive%20Grid-View,-Lets%20start%20building" style="font-size: 1rem; background-color: rgb(255, 255, 255);">Responsive Web
Design Grid-View</a><a id="_anchor_1" href="#_msocom_1" language="JavaScript" name="_msoanchor_1" style="font-size: 1rem; background-color: rgb(255, 255, 255);">[1]</a><span style="font-size: 1rem;">&nbsp;</span></p>

<div><!--[if !supportAnnotations]-->

<h3><br></h3><br><div><div id="_com_1" language="JavaScript" onmouseover="msoCommentShow('_anchor_1','_com_1')" onmouseout="msoCommentHide('_com_1')">

<!--[if !supportAnnotations]--></div>

<!--[endif]--></div>

</div><br><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4145"><h3 class="text-center pb-5">10.2. Media Query</h3><p dir="ltr" style="text-align: left;"></p><p>Media query es una técnica CSS
introducida en CSS3. Utiliza la regla <b>@media</b>
para incluir un bloque de propiedades CSS solo si una determinada condición es
verdadera.</p>

<p>Una media query es la base
principal del responsive web design. De forma sencilla podemos decir que los
media queries son un módulo de CSS que nos permiten identificar el medio en el
cual se está mostrando nuestro sitio y bajo qué condiciones aplicar estilos específicos.</p>

<p>&nbsp;<span style="font-size: 1rem;">Usando media queries, podremos
saber, por ejemplo, cuándo el sitio se está presentado en una ventana que mide
600px de ancho o menos, o cuando se está enviando a imprimir. Por ejemplo, si
la ventana del navegador tiene 600px o menos, el color de fondo será celeste.</span></p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4145/image.png" alt="" role="presentation" class="img-fluid"><br><br><p>Veamos otro ejemplo. Supongamos
que tenemos un div con la clase «caja» y queremos que se muestre con un ancho
de 500 pixeles en ventanas grandes, pero que se muestre con un ancho del 100%
al ser visto en ventanas de 700 pixeles de ancho o menos. Para ello deberemos
hacer lo siguiente.</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4145/image%20%281%29.png" alt="" role="presentation" class="img-fluid"><br><br><p>En el siguiente ejemplo, notar
que los estilos del div y el párrafo no están dentro de la media query. Eso es
porque todo lo que no está dentro de los media queries se aplica de manera
predeterminada. En este caso dejamos que el color del fondo del párrafo sea el
mismo, independientemente del tamaño de la ventana, para ello dejamos fuera de
la media query a esas propiedades.</p><p>En HTML:&nbsp;</p><p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4145/image%20%282%29.png" alt="" role="presentation" class="img-fluid"><br></p><p>En CSS:</p><p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4145/image%20%283%29.png" alt="" role="presentation" class="img-fluid"><br></p><p><br></p><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4146"><h3 class="text-center pb-5">10.3. Flexbox</h3><p dir="ltr" style="text-align: left;">El Módulo de Caja
Flexible, comúnmente llamado flexbox, fue diseñado como un modelo
unidimensional de layout, y como un método que pueda ayudar a distribuir el
espacio entre los ítems de una interfaz y mejorar las capacidades de
alineación.</p><p dir="ltr" style="text-align: left;"><img src="https://acceso.ispc.edu.ar/pluginfile.php/75666/mod_book/chapter/3938/note-task-comment-message-edit-write_108613.png" alt="task
" width="75" height="75"><strong>Desafío: </strong>A fin de aprender flexbox de manera dinámica y divertida, te invitamos a jugar<strong><span class="" style="color: rgb(239, 69, 64);">&nbsp;</span><a href="https://flexboxfroggy.com/#es" target="_blank" rel="noopener"><span class="" style="color: rgb(239, 69, 64);">Flexbox Froggy</span></a>!!</strong><br></p><p dir="ltr" style="text-align: left;"><strong><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4146/image%20%281%29.png" alt="" role="presentation" class="img-fluid"><br></strong></p><p dir="ltr" style="text-align: left;">Consulta la siguiente guía de Flexbos para más información:&nbsp;<a href="https://css-tricks.com/snippets/css/a-guide-to-flexbox/" class="_blanktarget">https://css-tricks.com/snippets/css/a-guide-to-flexbox/</a><br></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4151"><h3 class="text-center pb-5">10.4. Desafío Final</h3><h4 style="text-align: left;"><span class="" style="color: rgb(125, 159, 211);"><strong><span class="" style="color: rgb(51, 51, 51);">Si llegaste hasta aquí! Te invitamos a desafiar tus conocimientos!!&nbsp;</span></strong></span></h4><p dir="ltr"><strong>Guess CSS:</strong> <a href="https://www.guess-css.app/" class="_blanktarget">https://www.guess-css.app/</a></p><p dir="ltr">Juego que pone a prueba tus conocimientos en relación a grid layout, selectores y flexbox</p><p dir="ltr"><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4151/image%20%283%29.png" alt="" role="presentation" class="img-fluid"><br></p><p dir="ltr"><strong>FLEXBOX&nbsp; ADVENTURE:</strong> <a href="https://codingfantasy.com/games/flexboxadventure/play" class="_blanktarget">https://codingfantasy.com/games/flexboxadventure/play</a></p><p dir="ltr">Juego para practicar las propiedades de Flexbox. Tiene 3 niveles de dificultades y cada uno tiene a sus vez 24 niveles.</p><p dir="ltr" style="text-align: left;"><img src="https://acceso.ispc.edu.ar/pluginfile.php/77425/mod_book/chapter/4151/image%20%282%29.png" alt="" role="presentation" class="img-fluid"><br></p></div>
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
M.util.js_pending('core/notification'); require(['core/notification'], function(amd) {amd.init(77425, []); M.util.js_complete('core/notification');});;
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
 M.util.js_pending('random631961da6be5d2'); Y.on('domready', function() { M.util.js_complete("init");  M.util.js_complete('random631961da6be5d2'); });
})();
//]]>
</script>

</body>
</html>