<?php /* Template Name:  Page Comments Template */ get_header(); ?>
    <div class="content clearfix">

<section class="reviews-section page-section">
    <div class="container">
        <div class="reviews panel clearfix">
            <div class="panel-top"></div>
            <div>
                <div class="panel-content">
                    <h1 class="page-title"><?php the_title(); ?></h1>
                    <div class="reviews-button-container">
                        <a href="№" class="reviews-button button">Добавить отзыв</a>
                    </div>
                    <ul class="reviews-list list-unstyle">
                    <?php if( have_rows('comments_table') ): while ( have_rows('comments_table') ) : the_row(); ?>
                                                <li class="review">
                            <div class="review-header clearfix">
                                <div class="left">
                                    <div class="review-name"><span><?php the_sub_field('name'); ?></span></div>
                                    <div class="review-date"><span>Дата: </span><?php the_sub_field('date'); ?></div>
                                </div>
                                <div class="right">
                                    <ul class="review-rating review-rating-5 list-inline">
                                        <li class="review-rating-item"></li>
                                        <li class="review-rating-item"></li>
                                        <li class="review-rating-item"></li>
                                        <li class="review-rating-item"></li>
                                        <li class="review-rating-item"></li>
                                    </ul>
                                </div>
                            </div>
                            <div class="review-main">
                                <p><?php the_sub_field('comment'); ?></p>
                            </div>
                        </li>
                        <?php endwhile; endif; ?>
                    </ul>
                </div>
            </div>
            <div class="panel-bottom"></div>
        </div>
    </div>
</section>    </div>
</div>

<?php get_footer(); ?>
