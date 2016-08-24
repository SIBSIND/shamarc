<?php get_header(); ?>
<div class="content clearfix">
<h1 class="hide">Главная</h1>
    <section class="home-one-section page-section">
        <div class="container">
            <div class="error-panel">Если вы взяли для оплаты реквизиты киви то имейте ввиду что они актуальны только в течении 10 минут!!! По этому советуем всем покупать именно через биткоин!!! Так же на оплату биткоина действует скидка
            </div>
        </div>
    </section>
<section class="home-two-section page-section">
<div class="filter clearfix">
    <div class="container">
        <div class="filter-title">Выберите город</div>
        <ul class="filter-list filter-city-list list-inline l_tinynav1">
            <li class="filter-city-list-item item_city_hidden selected"><a class="filter-city-list-link" href="javascript:void(0)">Выберите город</a>
            </li>
                <?php wp_list_categories("title_li&parent=0&orderby=term_group");?></a>
        </ul>
        <select id="tinynav1" class="tinynav tinynav1">
          <option value="javascript:void(0)" selected="selected">Выберите город</option>
          <option value="/?city_id=17">Екатеринбург</option>
          <option value="/?city_id=16">Тюмень</option>
          <option value="/?city_id=32">Краснодар</option>
          <option value="/?city_id=22">Ростов-на-Дону</option>
          <option value="/?city_id=50">Сочи</option>
          <option value="/?city_id=46">Славянск-на-Кубани</option>
          <option value="/?city_id=28">Челябинск </option>
          <option value="/?city_id=34">Копейск</option>
          <option value="/?city_id=35">Златоуст</option>
          <option value="/?city_id=27">Уфа </option><
          <option value="/?city_id=54">Стерлитамак</option>
          <option value="/?city_id=33">Казань</option>
          <option value="/?city_id=36">Саратов</option>
          <option value="/?city_id=47">Тольятти</option>
          <option value="/?city_id=37">Самара</option>
          <option value="/?city_id=38">Новокуйбышевск</option>
          <option value="/?city_id=45">Нижний Новгород</option>
          <option value="/?city_id=51">Дзержинск</option>
          <option value="/?city_id=26">Тула</option>
          <option value="/?city_id=56">Киреевск</option>
          <option value="/?city_id=57">Новомосковск</option>
          <option value="/?city_id=20">Верхняя Пышма</option>
          <option value="/?city_id=40">Первоуральск</option>
          <option value="/?city_id=39">Ревда</option>
          <option value="/?city_id=19">Тобольск</option>
          <option value="/?city_id=52">Ишим</option>
          <option value="/?city_id=49">Каменск-Уральский</option>
          <option value="/?city_id=30">Курган</option>
          <option value="/?city_id=41">Нижний Тагил</option>
          <option value="/?city_id=42">Новосибирск </option>
          <option value="/?city_id=43">Красноярск</option>
          <option value="/?city_id=58">Туапсе</option>
          <option value="/?city_id=59">Иркутск</option>
        </select>

        <div class="filter-region filter-container">
          <div class="filter-title">Выберите район</div>
          <ul class="filter-list filter-region-list list-inline clearfix l_tinynav2">
            <li class="filter-region-list-item selected">
            <?php $category = get_the_category(); $category_id = $category[0]->cat_ID;
              $category_link = get_category_link( $category_id ); ?>
                <a class="filter-region-list-link" href="<?php echo $category_link; ?>">Все</a>
            </li>
                <?php if (is_category()) { $this_category = get_category($cat);
                    if (get_category_children($this_category->cat_ID) != "") {
                    wp_list_categories('hide_empty=0&title_li=&child_of=' . $this_category->cat_ID);
                    }  else { $parent = $this_category->category_parent;
                    wp_list_categories('hide_empty=0&title_li=&child_of=' . $parent); } } ?>
            </ul>

            <select id="tinynav2" class="tinynav tinynav2">
              <option value="/?city_id=17" selected="selected">Все</option>
              <option value="/?district_id=60">Сортировка</option>
              <option value="/?district_id=70">Центр</option>
              <option value="/?district_id=71">УРАЛМАШ</option>
              <option value="/?district_id=91">Кировский</option>
              <option value="/?district_id=97">ХИММАШ</option>
              <option value="/?district_id=104">Шарташ</option>
              <option value="/?district_id=114">ЖБИ</option>
              <option value="/?district_id=125">Уктус</option>
              <option value="/?district_id=137">ЭЛЬМАШ</option>
              <option value="/?district_id=148">Октябрьский</option>
              <option value="/?district_id=230">Широкая речка</option>
              <option value="/?district_id=493">Рудный</option>
              <option value="/?district_id=495">г. Березовский</option>
              <option value="/?district_id=498">Разные районы</option>
              <option value="/?district_id=580">Мега</option>
            </select>
        </div>
    </div>
</div>
<div class="goods">
    <div class="container">
        <h2 class="extra-title"><span>Товары</span></h2>
        <ul class="goods-list list-unstyle clearfix">
<?php if (have_posts()): while (have_posts()) : the_post(); ?>
                <li class="goods-list-item">
                    <div class="goods-list-item-inner clearfix">
                        <h3 class="goods-title">
                            <span><?php the_title(); ?></span>
                        </h3>
                        <div class="goods-availability">В наличии: <?php the_field('exist'); ?>шт</div>
                        <div class="goods-price"><?php the_field('price'); ?> руб</div>
                        <div class="goods-buy">
                            <a href="<?php the_permalink(); ?>">Купить</a>
                        </div>
                    </div>
                </li>
                <?php endwhile; endif; ?>
        </ul>
    </div>
</div>
      </section>
    </div>
</div>
<?php get_footer(); ?>
