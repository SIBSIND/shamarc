<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

    <link rel="stylesheet" type="text/css" href="<?php echo get_template_directory_uri(); ?>/css/normalize.css">
<link rel="stylesheet" type="text/css" href="<?php echo get_template_directory_uri(); ?>/css/style.css">
<title><?php wp_title( '' ); ?><?php if ( wp_title( '', false ) ) { echo ' :'; } ?> <?php bloginfo( 'name' ); ?></title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
<!--[if lt IE 9]>
    <script type="text/javascript" src="<?php echo get_template_directory_uri(); ?>/js/html5shiv.js"></script>
    <script type="text/javascript" src="<?php echo get_template_directory_uri(); ?>/js/selectivizr.js"></script>
    <script type="text/javascript" src="<?php echo get_template_directory_uri(); ?>/js/respond.js"></script>
  <![endif]-->
  <!-- css + javascript -->

    <script src="<?php echo get_template_directory_uri(); ?>/js/jquery.min.js"></script>
    <!--<![endif]-->
    <script src="<?php echo get_template_directory_uri(); ?>/js/tinynav.min.js"></script>
    <script src="<?php echo get_template_directory_uri(); ?>/js/jquery.customSelect.min.js"></script>
        <?php wp_head(); ?>
    </head>
<body class="home-page">

<div class="main">
    <header class="header">
        <div class="container">
            <div class="header-item logo">
                <a href="<?php echo home_url(); ?>" class="logo-link">Shama Shop<!--<img src="/img/logo_new.png" border="0">--></a>
            </div>
            <a href="https://shamarc.biz/?ddosprotected=1#" class="header-menu-toggle"><span></span>меню</a>
            <nav class="header-item header-menu">
                    <?php wpeHeadNav(); ?>
            </nav>
        </div>
    </header>
