
<!DOCTYPE html>

<html  dir="ltr" lang="es-wp" xml:lang="es-wp">
<head>
    <title>Guía POO</title>
    <link rel="shortcut icon" href="https://acceso.ispc.edu.ar/pluginfile.php/1/tool_tenant/favicon/1/favicon-96x96.png" />
    <meta name="apple-itunes-app" content="app-id=1470929705, app-argument=https://acceso.ispc.edu.ar/mod/book/print.php?id=32059&amp;chapterid=0"/><link rel="manifest" href="https://acceso.ispc.edu.ar/admin/tool/mobile/mobile.webmanifest.php" /><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="moodle, Guía POO" />
<link rel="stylesheet" type="text/css" href="https://acceso.ispc.edu.ar/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.css" /><script id="firstthemesheet" type="text/css">/** Required in order to fix style inclusion problems in IE with YUI **/</script><link rel="stylesheet" type="text/css" href="https://acceso.ispc.edu.ar/theme/workplace/wpcss.php/workplace/1659990713_1/all-1-1654194304" />
<link rel="stylesheet" type="text/css" href="https://acceso.ispc.edu.ar/mod/book/tool/print/print.css" />
<script>
//<![CDATA[
var M = {}; M.yui = {};
M.pageloadstarttime = new Date();
M.cfg = {"wwwroot":"https:\/\/acceso.ispc.edu.ar","sesskey":"Uzh6OTIEiZ","sessiontimeout":"10800","sessiontimeoutwarning":"1200","themerev":"1659990713","slasharguments":1,"theme":"workplace","iconsystemmodule":"core\/icon_system_fontawesome","jsrev":"1659972264","admin":"admin","svgicons":true,"usertimezone":"Am\u00e9rica\/Argentina\/Buenos_Aires","contextid":77597,"langrev":1661670867,"templaterev":"1658767754"};var yui1ConfigFn = function(me) {if(/-skin|reset|fonts|grids|base/.test(me.name)){me.type='css';me.path=me.path.replace(/\.js/,'.css');me.path=me.path.replace(/\/yui2-skin/,'/assets/skins/sam/yui2-skin')}};
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

<body  id="page-mod-book-print" class="format-wplist  path-mod path-mod-book chrome dir-ltr lang-es_wp yui-skin-sam yui3-skin-sam acceso-ispc-edu-ar pagelayout-embedded course-1863 context-77597 cmid-32059 category-242 ">
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
    <div class="text-center pb-3 book_title"><h1>Guía POO</h1></div>
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
                        Guía POO
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
                        jueves, 8 septiembre 2022, 12:39 
                    </td>
                </tr>
            </table>
        </div>
    </div>
    <div class="w-100 book_description">
        <div class="py-5">
            <h2 class="text-center pb-5">Descripción</h2>
             <p class="book_summary"><p dir="ltr" style="text-align: left;"><img src="https://acceso.ispc.edu.ar/pluginfile.php/77597/mod_book/intro/OIP%20%289%29.jpg" alt="Python" width="349" height="148" class="img-fluid atto_image_button_text-top"><br></p></p>
        </div>
    </div>
    <div class="w-100">
        <div class="py-5"><div class="book_toc_numbered"><a name="toc"></a><h2 class="text-center pb-5">Tabla de contenidos</h2><ul><li><a title="1. Introducción" class="font-weight-bold text-decoration-none" href="#ch4247">1. Introducción</a><ul><li><a title="1.1. Motivación de la POO" class="text-decoration-none" href="#ch4248">1.1. Motivación de la POO</a></li></ul></li><li><a title="2. Clases y Objetos" class="font-weight-bold text-decoration-none" href="#ch4249">2. Clases y Objetos</a><ul><li><a title="2.1. Ejercicio práctico de clases" class="text-decoration-none" href="#ch4270">2.1. Ejercicio práctico de clases</a></li></ul></li><li><a title="3. Métodos y Atributos" class="font-weight-bold text-decoration-none" href="#ch4250">3. Métodos y Atributos</a><ul><li><a title="3.1. Ejercicio práctico atributos" class="text-decoration-none" href="#ch4271">3.1. Ejercicio práctico atributos</a></li></ul></li><li><a title="4. Abstracción" class="font-weight-bold text-decoration-none" href="#ch4251">4. Abstracción</a></li><li><a title="5. Herencia" class="font-weight-bold text-decoration-none" href="#ch4252">5. Herencia</a><ul><li><a title="5.1. Ejercicio práctico de Herncia" class="text-decoration-none" href="#ch4272">5.1. Ejercicio práctico de Herncia</a></li></ul></li><li><a title="6. Encapsulamiento y Ocultamiento de la información" class="font-weight-bold text-decoration-none" href="#ch4253">6. Encapsulamiento y Ocultamiento de la información</a></li><li><a title="7. Polimorfismo" class="font-weight-bold text-decoration-none" href="#ch4255">7. Polimorfismo</a></li></ul></div></div>
    </div>
    <div class="w-100">
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4247"><h2 class="text-center pb-5">1. Introducción</h2><p dir="ltr"></p><p>Empecemos con una introducción básica a la&nbsp;<strong>P</strong>rogramación&nbsp;<strong>O</strong>rientada a&nbsp;<strong>O</strong>bjetos&nbsp;<strong>POO</strong>&nbsp;o&nbsp;<strong>OOP</strong>&nbsp;en inglés. Se trata de un paradigma de programación introducido en los años '70, pero que no se hizo popular hasta los '90.</p><p>Este modo o paradigma de programación nos permite organizar el código de una manera que se asemeja bastante a como pensamos en la vida real, utilizando las famosas&nbsp;<strong>clases</strong>. Estas nos permiten agrupar un conjunto de variables y funciones que veremos a continuación.</p><p>Cosas de lo más cotidianas como un perro o un coche pueden ser representadas con clases. Estas clases tienen diferentes características, que en el caso del perro podrían ser la edad, el nombre o la raza. Llamaremos a estas características,&nbsp;<strong>atributos</strong>.</p><p>Por otro lado, las clases tienen un conjunto de funcionalidades o cosas que pueden hacer. En el caso del perro podría ser andar o ladrar. Llamaremos a estas funcionalidades&nbsp;<strong>métodos</strong>.</p><p>Por último, pueden existir diferentes tipos de perro. Podemos tener uno que se llama Toby o el del vecino que se llama Laika. Llamaremos a estos diferentes tipos de perro&nbsp;<strong>objetos</strong>. Es decir, el concepto abstracto de perro es la&nbsp;<strong>clase</strong>, pero Toby o cualquier otro perro particular será el&nbsp;<strong>objeto</strong>.</p><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4248"><h3 class="text-center pb-5">1.1. Motivación de la POO</h3><p dir="ltr" style="text-align: left;"></p><p>Una vez explicada la programación orientada a objetos puede parecer bastante lógica, pero no es algo que haya existido siempre, y de hecho hay muchos lenguajes de programación que no la soportan.</p><p>En parte surgió debido a la creciente complejidad a la que los programadores se iban enfrentando conforme pasaban los años. En el mundo de la programación hay gran cantidad de aplicaciones que realizan tareas muy similares y es importante identificar los patrones que nos permiten no reinventar la rueda. La programación orientada a objetos intentaba resolver esto.</p><p>Uno de los primeros mecanismos que se crearon fueron las&nbsp;<strong>funciones</strong>, que permiten agrupar bloques de código que hacen una tarea específica bajo un nombre. Algo muy útil ya que permite también reusar esos módulos o funciones sin tener que copiar todo el código, tan solo la llamada.</p><p>Las funciones resultaron muy útiles, pero no eran capaces de satisfacer todas las necesidades de los programadores. Uno de los problemas de las funciones es que sólo realizan unas operaciones con unos datos de entrada para entregar una salida, pero no les importa demasiado conservar esos datos o mantener algún tipo de estado. Salvo que se devuelva un valor en la llamada a la función o se usen variables globales, todo lo que pasa dentro de la función queda olvidado, y esto en muchos casos es un problema.</p><p>Imaginemos que tenemos un juego con naves espaciales moviéndose por la pantalla. Cada nave tendrá una posición (x,y) y otros parámetros como el tipo de nave, su color o tamaño. Sin hacer uso de clases y POO, tendremos que tener una variable para cada dato que queremos almacenar: coordenadas, color, tamaño, tipo. El problema viene si tenemos 10 naves, ya que nos podríamos juntar con un número muy elevado de variables. Todo un desastre.</p><p>En el mundo de la programación existen tareas muy similares al ejemplo con las naves, y en respuesta a ello surgió la programación orientada a objetos. Una herramienta perfecta que permite resolver cierto tipo de problemas de una forma mucho más sencilla, con menos código y más organizado. Agrupa bajo una clase un conjunto de variables y funciones, que pueden ser reutilizadas con características particulares creando objetos.</p><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4249"><h2 class="text-center pb-5">2. Clases y Objetos</h2><p dir="ltr" style="text-align: left;"></p><div>Una clase es
la definición de las propiedades y comportamiento de un tipo de objeto
concreto.&nbsp;</div><div>Es un modelo que se utiliza para describir uno o más objetos del
mismo tipo.</div><br>En Python se crean de la siguiente manera:<br><img src="https://acceso.ispc.edu.ar/pluginfile.php/77597/mod_book/chapter/4249/image.png" alt="" role="presentation" class="img-fluid"><br><br><p>Se trata de una clase vacía y sin mucha utilidad práctica, pero es la mínima clase que podemos crear. Nótese el uso del&nbsp;<code>pass</code>&nbsp;que no hace realmente nada, pero daría un error si después de los&nbsp;<code>:</code>&nbsp;no tenemos contenido.</p><p>Ahora que tenemos la&nbsp;<strong>clase</strong>, podemos crear un&nbsp;<strong>objeto</strong>&nbsp;de la misma. Podemos hacerlo como si de una variable normal se tratase. Nombre de la variable igual a la clase con&nbsp;<code>()</code>. Dentro de los paréntesis irían los parámetros de entrada si los hubiera.</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77597/mod_book/chapter/4249/image%20%281%29.png" alt="" role="presentation" class="img-fluid"><br><br><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4270"><h3 class="text-center pb-5">2.1. Ejercicio práctico de clases</h3><p dir="ltr" style="text-align: left;">Crear un programa que permita crear la clase Motovechiculo, capaz de procesar la información básica de las motos en un concesionario llamado "Córdoba Motos", para ello vamos a suponer que los atributos de una moto son:</p><p dir="ltr" style="text-align: left;">•Marca</p><p dir="ltr" style="text-align: left;">•Modelo</p><p dir="ltr" style="text-align: left;">•Patente</p><p dir="ltr" style="text-align: left;">•kilometraje</p><p dir="ltr" style="text-align: left;">Se deberá poder ingresar dichos datos y ser mostrados por consola.</p><p dir="ltr" style="text-align: left;"><br></p><p dir="ltr" style="text-align: left;">Le dejamos la solución del ejercicio dado, pero se les recomienda intentar varias veces hasta que salga la solución antes de ver la misma.</p><p dir="ltr" style="text-align: left;"><span style="font-size: 1rem;">Link a la resolución del ejercicio propuesto:&nbsp;</span><br></p><p dir="ltr" style="text-align: left;"><a href="https://drive.google.com/file/d/1TJar-Q3f_wJpAxINDBPqcNHipoN_H-Lr/view?usp=sharing" class="_blanktarget">https://drive.google.com/file/d/1TJar-Q3f_wJpAxINDBPqcNHipoN_H-Lr/view?usp=sharing</a><br></p><p dir="ltr" style="text-align: left;"><br></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4250"><h2 class="text-center pb-5">3. Métodos y Atributos</h2><p dir="ltr" style="text-align: left;"><span style="font-size: 1rem;">Los atributos
son características individuales que diferencian un objeto de otro y que
determinan su apariencia, estado u otras cualidades.</span><br></p><div>Los atributos
se guardan en variables denominadas de instancia y cada objeto particular puede
tener valores distintos para estas variables.</div><br><p>A continuación vamos a añadir algunos atributos a nuestra clase. Antes de nada es importante distinguir que existen dos tipos de atributos:</p><ul><li>Atributos de&nbsp;<strong>instancia</strong>: Pertenecen a la instancia de la clase o al objeto. Son atributos particulares de cada instancia, en nuestro caso de cada perro.</li><li>Atributos de&nbsp;<strong>clase</strong>: Se trata de atributos que pertenecen a la clase, por lo tanto serán comunes para todos los objetos.</li></ul><p>Empecemos creando un par de&nbsp;<strong>atributos de instancia</strong>&nbsp;para nuestro perro, el&nbsp;<code>nombre</code>&nbsp;y la&nbsp;<code>raza</code>. Para ello creamos un método&nbsp;<code>__init__</code>&nbsp;que será llamado automáticamente cuando creemos un objeto. Se trata del&nbsp;<strong>constructor</strong>.</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77597/mod_book/chapter/4250/image.png" alt="" role="presentation" class="img-fluid"><br><br>Ahora que hemos definido el método&nbsp;<em>init</em>&nbsp;con dos parámetros de entrada, podemos crear el objeto pasando el valor de los atributos. Usando&nbsp;<code>type()</code>&nbsp;podemos ver como efectivamente el objeto es de la clase&nbsp;<code>Perro</code>.<br><br><img src="https://acceso.ispc.edu.ar/pluginfile.php/77597/mod_book/chapter/4250/image%20%281%29.png" alt="" role="presentation" class="img-fluid"><br><br><p>Seguramente te hayas fijado en el&nbsp;<code>self</code>&nbsp;que se pasa como parámetro de entrada del método. Es una variable que representa la instancia de la clase, y deberá estar siempre ahí.</p><p>El uso de&nbsp;<code>__init__</code>&nbsp;y el doble&nbsp;<code>__</code>&nbsp;no es una coincidencia. Cuando veas un método con esa forma, significa que está reservado para un uso especial del lenguaje. En este caso sería lo que se conoce como&nbsp;<strong>constructor</strong>. Hay gente que llama a estos métodos mágicos.</p><p>Por último, podemos acceder a los atributos usando el objeto y&nbsp;<code>.</code>. Por lo tanto.</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77597/mod_book/chapter/4250/image%20%282%29.png" alt="" role="presentation" class="img-fluid"><br><br><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4271"><h3 class="text-center pb-5">3.1. Ejercicio práctico atributos</h3>Luego del análisis de la clase de Motovehículo, nos hemos dado cuenta que además de las info que se guarda en dicha clase, necesitamos agregar:<br>•Año de patentamiento - SOLO AÑO.<br>•Color.<br>•Capacidad del tanque.<br><br>Además se necesita modificar el programa, de manera que se puedan ingresar n cantidad de motos, ya que se necesita que podamos brindar la siguiente información:<br>•Cantidad de motos con menos de 1000km<br>•Cantidad de motos patentadas en 2021.<br><br><p dir="ltr">Le dejamos la solución del ejercicio dado, pero se les recomienda intentar varias veces hasta que salga la solución antes de ver la misma.</p><p dir="ltr">Link a la resolución del ejercicio propuesto:&nbsp;</p><br><br></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4251"><h2 class="text-center pb-5">4. Abstracción</h2><p dir="ltr" style="text-align: left;"></p><div>Es la
capacidad para extraer las propiedades esenciales de un concepto e identificar
comportamientos comunes para definir nuevos tipos de entidades en el mundo
real.</div>

<div><br><!--[endif]--></div>

<h5>Abstracción
funcional:&nbsp;</h5><div>Es lo que sabemos que un objeto puede hacer, por ejemplo en el caso
de un auto , acelerar, frenar, doblar. </div>

<div><br><!--[endif]--></div>

<h5>Abstracción de
datos:&nbsp;</h5><div>Son los atributos que tiene&nbsp; un
determinado tipo de objetos, por ejemplo en el caso de un auto, marca, modelo,
patente, color.</div><br><br><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4252"><h2 class="text-center pb-5">5. Herencia</h2><p dir="ltr" style="text-align: left;"></p><div>Es la
propiedad que permite definir una clase a partir de otra clase relacionado que
suponga alguna de las siguientes relaciones: </div><div><br></div>

<h5>Especialización:&nbsp;</h5><div>La clase Auto
como especialización de Vehículo.</div><div><br></div>

<h5>Generalización:</h5><div>La clase
Vehículo como generalización de la clase Auto.</div><div><br></div>

Es un
mecanismo para la reutilización de código.<br><div><u>Ejemplo:</u></div>

<div>Si una clase B
(celular) hereda de una clase A (productos) implica que:</div>

<div>B incorpora la
estructura (atributos) y comportamientos (métodos)de la clase A.</div>

<div>B puede añadir
nuevos atributos.</div>

<div>B puede añadir
nuevos métodos.</div>

<div>B puede
redefinir métodos (sobre escritura u overwriting).</div><br><div>La herencia
organiza las clases en una estructura jerárquica formando jerarquía de clases.</div>

<div>Ejemplo: </div><img src="https://acceso.ispc.edu.ar/pluginfile.php/77597/mod_book/chapter/4252/image.png" alt="" role="presentation" class="img-fluid"><br><br><p>Python permite
la&nbsp;herencia múltiple, es
decir, se puede heredar de múltiples clases. La herencia múltiple es la
capacidad de una subclase de heredar de múltiples súper clases.</p>Lo vemos más gráfico en un ejemplo:<br><img src="https://acceso.ispc.edu.ar/pluginfile.php/77597/mod_book/chapter/4252/image%20%281%29.png" alt="" role="presentation" class="img-fluid"><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4272"><h3 class="text-center pb-5">5.1. Ejercicio práctico de Herncia</h3><p dir="ltr" style="text-align: left;">Crear la clase Triciclomotor que herede de la clase Motovehículo y le añada el atributo de capacidad de carga y características especiales.</p><p dir="ltr" style="text-align: left;"></p><p dir="ltr">Le dejamos la solución del ejercicio dado, pero se les recomienda intentar varias veces hasta que salga la solución antes de ver la misma.</p><p dir="ltr">Link a la resolución del ejercicio propuesto:&nbsp;</p><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4253"><h2 class="text-center pb-5">6. Encapsulamiento y Ocultamiento de la información</h2><p dir="ltr" style="text-align: left;"></p><div></div><h4>Encapsulamiento:</h4><p>La encapsulación es una forma de darle uso exclusivo a los comportamientos o atributos que posee una clase, es decir, protege esos atributos y comportamientos para que no sean usados de manera externa.</p><p>En python para hacer que un atributo o comportamiento sea privado tenemos que colocar un par de guiones bajos antes del nombre del atributo o comportamiento “__nombre”.</p><p>Para empezar nuestro ejemplo de encapsulación vamos a crear una clase que llamaremos “Ejemplo” y dentro de ella declaramos un método al que llamaremos “publico” que contendrá un&nbsp;<strong>return</strong>&nbsp;que solo mostrara una cadena de texto que dirá “Soy un método público a la vista de todo”:</p><img src="https://acceso.ispc.edu.ar/pluginfile.php/77597/mod_book/chapter/4253/image.png" alt="" role="presentation" class="img-fluid"><br><br>Ahora declaramos un método que se llame “privado” pero antes de su nombre pondremos un par de guiones bajos “__” y dentro del método una cadena de texto como en el método anterior:<br><br><img src="https://acceso.ispc.edu.ar/pluginfile.php/77597/mod_book/chapter/4253/image%20%281%29.png" alt="" role="presentation" class="img-fluid"><br><br><p>Ya con todo esto creamos un objeto perteneciente a la clase ejemplo y procedemos a imprimir los dos métodos hemos creado:</p><div><div><div><br>

</div></div></div><img src="https://acceso.ispc.edu.ar/pluginfile.php/77597/mod_book/chapter/4253/image%20%282%29.png" alt="" role="presentation" class="img-fluid"><br><br><p>Si ejecutamos el ejemplo nos mostrara algo parecido:</p><pre>Soy un método público, a la vista de todo
Traceback (most recent can last):
 File “encapsulación.py”, line 12, in (module)
print(objeto.__private())
AttributeError: ‘Ejemplo’ object has no attribute ‘__privado’
</pre><p>Como puedes ver al ejecutarlo si nos muestra el contenido del método publico pero a la hora de mostrar el método privado nos dice que tal método no existe pero en realidad si solo que por ser privado no puede ser mostrado externamente.</p><br><h4>Ocultamiento:</h4><div>El
ocultamiento protege a las propiedades de un objeto contra su modificación por
quien no tenga derecho a acceder a ellas. Esto asegura que otros objetos no
pueden cambiar el estado interno de un objeto de maneras inesperadas.</div><div><br></div>

<div>Cada tipo de
objeto expone una interfaz&nbsp; a otros
objetos que especifica cómo pueden interactuar con los objetos de una clase.</div><div><br></div>

<div>Es un concepto
relacionado con la seguridad de los datos.</div><br><br><p></p></div>
            </div>
            <div class="pb-5">
            <div class="book_chapter pt-3" id="ch4255"><h2 class="text-center pb-5">7. Polimorfismo</h2><p dir="ltr" style="text-align: left;"></p><div>El
polimorfismo nos permite programar de manera general en lugar de programar de
manera específica.<br>
</div><div><br></div>

<div>Hay cuatro
técnicas, cada una de las cuales permite una forma distinta de reutilización de
código, que facilita a su vez el desarrollo rápido, la confianza, facilidad de
uso y mantenimiento del software:</div>

<div>•Sobrecarga</div>

<div>•Sobreescritura</div>

<div>•Variables
polimórficas</div>

<div>•Genericidad</div><div><br></div><div><h5>Sobrecarga (overloading,
polimorfismo ad-hoc)</h5>

<div>•Un solo nombre
de método y muchas implementaciones distintas.</div>

<div>•Las funciones
sobrecargadas normalmente se distinguen en tiempo de compilación por tener
distintos parámetros de entrada y/o salida.<br>
</div><div><br></div>

<h5>Sobreescritura (overriding,
polimorfismo de inclusión):</h5>

<div>•Tipo especial
de sobrecarga que ocurre dentro de relaciones de herencia en métodos con enlace
dinámico.</div>

<div>•Dichos
métodos, definidos en clases base, son refinados o reemplazados en las clases
derivadas.</div><br></div><h5>Variables
polimórficas (polimorfismo
de asignación):</h5>

<div>Variable que
se declara como de un tipo pero que referencia en realidad un valor de un tipo
distinto (normalmente relacionado mediante herencia).</div>

<p></p>

<h5>Genericidad (plantillas o
templates):</h5>

<div>•Clases o
métodos parametrizados (algunos tipos se dejan sin definir).</div>

<div>•Forma de crear
herramientas de propósito general (clases, métodos) y especializarlas para
situaciones específicas.</div><br><h4>Ejemplos:</h4><h5>Variables
polimórficas:</h5>

<div>•Cuenta pc=new
CuentaJoven();</div>

<div><br><!--[endif]--></div>

<h5>Genericidad:</h5>

<div>•Lista&lt;Cliente&gt;</div>

<div>•Lista&lt;Articulo&gt;</div>

<div>•Lista&lt;Alumno&gt;</div>

<div>•Lista&lt;Habitacion&gt;</div><br><h5>Sobrecarga:</h5>

<div>•Factura:
imprimir()</div>

<div>•Factura:
imprimir(int numCopias)</div>

<div>•ListaCompra:
imprimir()</div>

<div><span style="font-size: 1rem;"><br></span></div><h5><span style="font-size: 1rem;">Sobreescritura:</span></h5>

<div>•Cuenta:
abonarIntereses()</div>

<div>•CuentaJoven:
abonarIntereses()</div><br><p></p></div>
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
M.util.js_pending('core/notification'); require(['core/notification'], function(amd) {amd.init(77597, []); M.util.js_complete('core/notification');});;
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
 M.util.js_pending('random631963df52c4c2'); Y.on('domready', function() { M.util.js_complete("init");  M.util.js_complete('random631963df52c4c2'); });
})();
//]]>
</script>

</body>
</html>