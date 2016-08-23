<?php /* Template Name: Order Page Template */ get_header(); ?>
    <div class="content clearfix">


<h1 class="hide"><?php the_title(); ?></h1>
<section class="check-order-section page-section">
    <div class="container">
        <div class="check-order-form panel clearfix">
            <div class="panel-top"></div>
            <div class="panel-center">
                <div class="panel-content">
                    <form>
                        <div class="form-group">
                            <label for="id" class="check-order-form-label label">Номер заказа</label>
                            <div>
                                <input type="text" id="id" class="check-order-form-textbox textbox">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="comment" class="check-order-form-label label">Комментарий к платежу</label>
                            <div>
                                <input type="text" id="comment" class="check-order-form-textbox textbox">
                            </div>
                        </div>
                        <center><img id="ajaxLoader" style="display: none;" src="<?php echo get_template_directory_uri(); ?>/img/ajax-loader.gif"></center>
                        <div id="info">

                        </div>
                        <div>
                            <input class="check-order-form-button" name="yt0" type="button" value="Проверить оплату" id="yt0">                            <div>Проверить платеж по чеку можно <a target="_blank" href="https://qiwi.ru/support/check.action">&gt;&gt;&gt;ТУТ&lt;&lt;&lt;</a></div>
                        </div>
                    </form>
                </div>
            </div>
            <div class="panel-bottom"></div>
        </div>
    </div>
</section>    </div>
</div>
<?php get_footer(); ?>
