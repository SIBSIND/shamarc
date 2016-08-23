<?php /* Template Name:  Page Bitcoin Payment */ get_header(); ?>
    <div class="content clearfix">


<section class="vacancy-section page-section">
    <div class="container">
        <div class="vacancy panel clearfix">
            <div class="panel-top"></div>
            <div>
                <div class="panel-content">
                    <h1 class="page-title"><?php the_title(); ?></h1>
                    <h4 style="text-align: center;">Гайд по оплате биткоином через обменник
                    <a href="http://minibank.cc/">http://minibank.cc/</a>
                    <span style="font-size: 15px; color: rgb(51, 51, 51);"></span></h4>
                    <h4 style="text-align: center;">
                    <span style="font-weight: normal;">Вам нужно:</span></h4>
                    <h4 style="text-align: center;">
                    <span style="font-weight: normal;">1. Зарегистрированный кошелек на сайте <a href="https://qiwi.com/"> https://qiwi.com </a></span></h4>
                    <h4 style="text-align: center;">
                    <span style="font-weight: normal;">2. Зайти на сайт <a href="http://minibank.cc/">http://minibank.cc/ </a></span></h4>
                    <h4 style="text-align: center;">
                    <span style="font-weight: normal;">3. Зайти на сайт <a href="https://blockchain.info/">https://blockchain.info/ </a> для проверки подтверждений вашей оплаты.</span>
                    </h4>
                    <?php $images = get_field('images'); if( $images ): ?>
                    <?php foreach( $images as $image ): ?>
                    <p><img src="<?php echo $image['sizes']['large']; ?>" alt="<?php echo $image['alt']; ?>" /></p>
                    <?php endforeach; ?>
                    <?php endif; ?>

                    <h4 style="text-align: center;">Так же если у вас будут вопросы по оплате биткоином  - пишите нашим оператором они вам подскажут как купить за биткоин! </h4>
                    <h2 style="text-align: center;">Всем приятных покупок!</h2>

                    </div>
            </div>
            <div class="panel-bottom"></div>
        </div>
    </div>
</section>    </div>
</div>
<?php get_footer(); ?>
