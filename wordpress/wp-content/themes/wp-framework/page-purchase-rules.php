<?php /* Template Name:  Page Purchase rules */ get_header(); ?>

<div class="content clearfix">
<section class="vacancy-section page-section">
    <div class="container">
        <div class="vacancy panel clearfix">
            <div class="panel-top"></div>
            <div>
                <div class="panel-content">
                    <h1 class="page-title"><?php the_title(); ?></h1>
                    <p>Правила магазина <a href="http://shamarc.biz/">Shamarc.biz</a></p><p>Совершая покупку в нашем магазине вы автоматически соглашаетесь с нашими правилами и обязуетесь выполнять их.</p><p><strong><u>Общие положения:</u></strong></p>
                    <?php the_field('rules_text'); ?>
                    </div>
            </div>
            <div class="panel-bottom"></div>
        </div>
    </div>
</section>
 </div>
<?php get_footer(); ?>
