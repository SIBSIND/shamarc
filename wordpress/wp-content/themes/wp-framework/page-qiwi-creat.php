<?php /* Template Name:  Qiwi */ get_header(); ?>
<div class="content clearfix">


<section class="vacancy-section page-section">
    <div class="container">
        <div class="vacancy panel clearfix">
            <div class="panel-top"></div>
            <div>
                <div class="panel-content">
                    <h1 class="page-title"><?php the_title(); ?></h1>
                    <?php the_field('qiwi_text'); ?>
                </div>
            </div>
            <div class="panel-bottom"></div>
        </div>
    </div>
</section>
</div>
<?php get_footer(); ?>
