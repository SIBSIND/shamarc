<?php /* Template Name:  Page Work */ get_header(); ?>

<div class="content clearfix">
<section class="vacancy-section page-section">
    <div class="container">
        <div class="vacancy panel clearfix">
            <div class="panel-top"></div>
            <div>
                <div class="panel-content page-work" style="font-family: &quot;Helvetica Neue&quot;, Helvetica, sans-serif;">
                    <h1 class="page-title"><?php the_title(); ?></h1>
                    <h3 style="text-align: center;"><strong><span >Приветствую всех</span></strong></h3>
                    <?php the_field('work_text'); ?>
                    </div>
            </div>
            <div class="panel-bottom"></div>
        </div>
    </div>
</section>
</div>
<?php get_footer(); ?>
