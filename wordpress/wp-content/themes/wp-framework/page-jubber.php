<?php /* Template Name:  Page Jubber */ get_header(); ?>
<div class="content clearfix">


<section class="vacancy-section page-section">
    <div class="container">
        <div class="vacancy panel clearfix">
            <div class="panel-top"></div>
            <div>
                <div class="panel-content" style="font-family: &quot;Helvetica Neue&quot;, Helvetica, sans-serif;">
                    <h1 class="page-title"><?php the_title(); ?></h1>
                    <?php the_field('jubb_text'); ?>
                </div>
            </div>
            <div class="panel-bottom"></div>
        </div>
    </div>
</section>
</div>
<?php get_footer(); ?>
