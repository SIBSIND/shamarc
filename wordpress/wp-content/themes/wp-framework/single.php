<?php get_header(); ?>
<div class="content clearfix">
<section class="vacancy-section page-section">
<div class="container choose-method">
        <div class="vacancy panel clearfix">
            <div class="panel-top"></div>
            <div>
                <div class="panel-content">
                    <h1 class="page-title">Выберите метод оплаты</h1>

            <div class="paymentMethod">

      <div class="item item-qiwi">
        <a href="#">
            <img src="<?php echo get_template_directory_uri(); ?>/img/paymentMethod_qiwi.png">
            <span class="caption">Qiwi</span>
        </a>
    </div>
    <div class="item item-bitcoin">
        <a href="#">
            <img src="<?php echo get_template_directory_uri(); ?>/img/paymentMethod_btc.png">
            <span class="caption">Bitcoin</span>
        </a>
    </div>

</div>                </div>
            </div>
            <div class="panel-bottom"></div>
        </div>
    </div>




<div class="container method-qiwi">
        <div class="panel clearfix">
            <div class="panel-top"></div>
            <div>
                <div class="panel-content">
                    <div class="dark-text" style="font-size: 1.25em; text-align: center;">
                    <?php if (have_posts()): while (have_posts()) : the_post(); ?>
                        <p>Вы приобретаете</p>
                    </div>
                    <h3 class="first-title"><?php the_title(); ?></h3>
                    <div class="dark-text" style="font-size: 1.25em; text-align: center;">
                      <p>Для приобретения выбранного товара, оплатите<br><span class="warning-text">
                      <?php if ( get_post_meta($post->ID, 'price', true) ) : ?>
                      <?php echo get_post_meta($post->ID, 'price', true) ?>
                      <?php endif; ?>
                      рублей</span> на номер QIWI:</p>
                    </div>
                    <p class="first-title qiwi-pocket"><a href="#">Получить QIWI кошелек</a>
                    <span class="qiwi-payment" style="display: none"><?php echo strip_tags ( get_the_term_list( get_the_ID(), 'qiwi')); ?></span>
                    </p>
                    <div class="dark-text" style="font-size: 1.25em; text-align: center;">
                        <p>комментарий к платежу</p>
                    </div>
                    <p class="first-title">
                    <?php if ( get_post_meta($post->ID, 'comment', true) ) : ?>
                    <?php echo get_post_meta($post->ID, 'comment', true) ?>
                    <?php endif; ?>
                  </p>
                    <div class="warning-text" style="text-align: center;">
                        <p>Внимание! Обязательно укажите этот комментарий при оплате,<br>иначе оплата не будет засчитана в автоматическом режиме. </p>
                    </div>
                    <p class="first-title">Заказ
                      <?php if ( get_post_meta($post->ID, 'number', true) ) : ?>
                      <?php echo get_post_meta($post->ID, 'number', true) ?>
                      <?php endif; ?>
                    </p>
                    <div class="dark-text" style="text-align: center;">
                        <p>Это номер вашего заказа, запомните его. По номеру заказа и комментарию вы сможете узнать статус заказа (получить адрес) в любой момент и с любого устройства на странице "Проверка заказа</p>
                    </div>


                    <center><img id="ajaxLoader" style="display: none;" src="<?php echo get_template_directory_uri(); ?>/img/ajax-loader.gif"></center>
                    <div id="info">
                        После оплаты нажмите кнопку, чтобы получить адрес
                    </div>
                    <div class="buy-button-container">
                        <input class="buy-button button" name="yt0" type="button" value="Проверить оплату" id="yt0">
                    </div>
                        <?php endwhile; endif; ?>
                </div>
            </div>
            <div class="panel-bottom"></div>
        </div>
    </div>


<div class="form-style-6 captha-ispection get-code">
    <h1>Получение кошелька</h1>
    <form method="post">
                    <p style="text-align:center"><img id="yw0" src="<?php echo get_template_directory_uri(); ?>/img/captcha.png" alt=""></p>
            <input type="text" name="captcha" placeholder="Введите код">
            <a href="#"><p class="purple-bgc">Получить</p></a>
            </form>
</div>







    <div class="container second-qiwi">
        <div class="panel clearfix">
            <div class="panel-top"></div>
            <div>
                <div class="panel-content">
                    <div class="dark-text" style="font-size: 1.25em; text-align: center;">
                    <?php if (have_posts()): while (have_posts()) : the_post(); ?>
                        <p>Вы приобретаете</p>
                    </div>
                    <h3 class="first-title"><?php the_title(); ?></h3>
                    <div class="dark-text" style="font-size: 1.25em; text-align: center;">
                        <p>Для приобретения выбранного товара, оплатите<br><span class="warning-text">
                        <?php if ( get_post_meta($post->ID, 'price', true) ) : ?>
                        <?php echo get_post_meta($post->ID, 'price', true) ?>
                          <?php endif; ?> рублей</span> на номер QIWI:
                        </p>
                    </div>
                    <p class="first-title">
                    <span class="qiwi-payment" style="font-size: 20px;">
                  <?php echo strip_tags ( get_the_term_list( get_the_ID(), 'qiwi')); ?></span>
                    </p>
                    <div class="dark-text" style="font-size: 1.25em; text-align: center;">
                        <p>комментарий к платежу</p>
                    </div>
                    <p class="first-title">
                    <?php if ( get_post_meta($post->ID, 'comment', true) ) : ?>
                  <?php echo get_post_meta($post->ID, 'comment', true) ?>
                  <?php endif; ?>
                  </p>
                    <div class="warning-text" style="text-align: center;">
                        <p>Внимание! Обязательно укажите этот комментарий при оплате,<br>иначе оплата не будет засчитана в автоматическом режиме. </p>
                    </div>
                    <p class="first-title">Заказ
                    <?php if ( get_post_meta($post->ID, 'number', true) ) : ?>
                    <?php echo get_post_meta($post->ID, 'number', true) ?>
                     <?php endif; ?>

                     </p>
                    <div class="dark-text" style="text-align: center;">
                        <p>Это номер вашего заказа, запомните его. По номеру заказа и комментарию вы сможете узнать статус заказа (получить адрес) в любой момент и с любого устройства на странице "Проверка заказа"</p>
                    </div>


                    <center><img id="ajaxLoader" style="display: none;" src="<?php echo get_template_directory_uri(); ?>/img/ajax-loader.gif"></center>
                    <div id="info">
                        После оплаты нажмите кнопку, чтобы получить адрес
                    </div>
                    <div class="buy-button-container">
                        <input class="buy-button button" name="yt0" type="button" value="Проверить оплату" id="yt0">
                    </div>
                        <?php endwhile; endif; ?>
                </div>
            </div>
            <div class="panel-bottom"></div>
        </div>
    </div>






<div class="container method-bitcoin">
        <div class="panel clearfix">
            <div class="panel-top"></div>
            <div>
                <div class="panel-content">
                    <div class="dark-text" style="font-size: 1.25em; text-align: center;">
                    <?php if (have_posts()): while (have_posts()) : the_post(); ?>
                        <p>Вы приобретаете</p>
                    </div>
                    <h3 class="first-title"><?php the_title(); ?></h3>
                    <div class="dark-text" style="font-size: 1.25em; text-align: center;">
                        <p>Для приобретения выбранного товара, оплатите<br><span class="warning-text">
                        <?php if ( get_post_meta($post->ID, 'btc_price', true) ) : ?>
                      <?php echo get_post_meta($post->ID, 'btc_price', true) ?>
                        <?php endif; ?>
                      BTC</span> на Bitcoin кошелек:</p>
                    </div>
                    <p class="first-title" style="word-break: break-word;">
                    <?php echo strip_tags ( get_the_term_list( get_the_ID(), 'bitcoin')); ?>

                    </p>


                    <p class="first-title">Заказ
                    <?php if ( get_post_meta($post->ID, 'btc_number', true) ) : ?>
                    <?php echo get_post_meta($post->ID, 'btc_number', true) ?>
                     <?php endif; ?>
                    </p>

                    <div class="dark-text" style="font-size: 1.25em; text-align: center;">
                        <p>комментарий</p>
                    </div>
                    <p class="first-title">
                    <?php if ( get_post_meta($post->ID, 'btc_comment', true) ) : ?>
                    <?php echo get_post_meta($post->ID, 'btc_comment', true) ?>
                    <?php endif; ?>
                    </p>
                    <div class="dark-text" style="text-align: center;">
                        <p>Это номер вашего заказа, запомните его. По номеру заказа и комментарию вы сможете узнать статус заказа (получить адрес) в любой момент и с любого устройства на странице <a href="/check">проверка заказа</a></p>
                    </div>

                    <p class="text-warning">
                        Комментарий служит исключительно для идентификации Вашего заказа.
                        Отправлять BTC с комментарием не нужно, достаточно просто на указанный кошелек перевести <span style="color:red">точную сумму, дождаться 3 подтверждений</span> в системе Bitcoin, после чего Вы получите свой адрес.
                        <span style="color:red">Оплачивать необходимо одним переводом. Сумма перевода и кошелек должны быть точными, как указано в реквизитах выше, иначе Ваша оплата не засчитается. Будьте внимательны, так как при ошибочном платеже получить адрес или возврат средств будет невозможно!</span>
                        Выдача адреса производиться на этой странице автоматически, либо на странице <a href="/check">проверка заказа</a> по выданному номеру заказа и присвоенному комментарию.
                        Если Вы случайно закрыли данную страницу, воспользуйтесь страницей <a href="/check">проверка заказа</a>.
                        Создать свой кошелек <a href="https://bitcoin.org/ru/faq" target="_blank">Bitcoin</a> можно <a href="https://blockchain.info/ru/wallet/new" target="_blank">здесь</a> или <a href="https://bitcoin.org/ru/choose-your-wallet" target="_blank">здесь</a>.
                        Купить <a href="https://bitcoin.org/ru/faq" target="_blank">Bitcoin</a> можно через обменники, например: <a href="http://www.bestchange.ru/qiwi-to-bitcoin.html" target="_blank">здесь</a>.
                    </p>


                    <center><img id="ajaxLoader" style="display: none;" src="<?php echo get_template_directory_uri(); ?>/img/ajax-loader.gif"></center>
                    <div id="info">
                        После оплаты нажмите кнопку, чтобы получить адрес
                    </div>
                    <div class="buy-button-container">
                        <input class="buy-button button" name="yt0" type="button" value="Проверить оплату" id="yt0">
                    </div>
                        <?php endwhile; endif; ?>
                </div>
            </div>
            <div class="panel-bottom"></div>
        </div>
    </div>
  </section>
</div>
<?php get_footer(); ?>
