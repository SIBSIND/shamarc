<?php /* Template Name: Home Page Template */ get_header(); ?>

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
        <select id="tinynav1" class="tinynav tinynav1"><option value="javascript:void(0)" selected="selected">Выберите город</option><option value="/?city_id=17">Екатеринбург</option><option value="/?city_id=16">Тюмень</option><option value="/?city_id=32">Краснодар</option><option value="/?city_id=22">Ростов-на-Дону</option><option value="/?city_id=50">Сочи</option><option value="/?city_id=46">Славянск-на-Кубани</option><option value="/?city_id=28">Челябинск </option><option value="/?city_id=34">Копейск</option><option value="/?city_id=35">Златоуст</option><option value="/?city_id=27">Уфа </option><option value="/?city_id=54">Стерлитамак</option><option value="/?city_id=33">Казань</option><option value="/?city_id=36">Саратов</option><option value="/?city_id=47">Тольятти</option><option value="/?city_id=37">Самара</option><option value="/?city_id=38">Новокуйбышевск</option><option value="/?city_id=45">Нижний Новгород</option><option value="/?city_id=51">Дзержинск</option><option value="/?city_id=26">Тула</option><option value="/?city_id=56">Киреевск</option><option value="/?city_id=57">Новомосковск</option><option value="/?city_id=20">Верхняя Пышма</option><option value="/?city_id=40">Первоуральск</option><option value="/?city_id=39">Ревда</option><option value="/?city_id=19">Тобольск</option><option value="/?city_id=52">Ишим</option><option value="/?city_id=49">Каменск-Уральский</option><option value="/?city_id=30">Курган</option><option value="/?city_id=41">Нижний Тагил</option><option value="/?city_id=42">Новосибирск </option><option value="/?city_id=43">Красноярск</option><option value="/?city_id=58">Туапсе</option><option value="/?city_id=59">Иркутск</option></select>

        <div class="filter-region filter-container">
            <div class="filter-title">Выберите район</div>
            <ul class="filter-list filter-region-list list-inline clearfix l_tinynav2">
                <li class="filter-region-list-item selected"><a class="filter-region-list-link" href="https://shamarc.biz/?city_id=17">Все</a></li>
                <?php $kat = 9; $na_akran = '<ul class="l_tinynav1">' . "\n";
            $dochernii_kategorii = get_categories('child_of=' . $kat . '&hide_empty=0');
            foreach ($dochernii_kategorii as $dochernaya_kategoria) :
                if ($kat == $dochernaya_kategoria->category_parent) :
                    $na_akran .= "\t" . '<li class="filter-region-list-item "><a class="filter-region-list-link" href="' .
                        get_category_link($dochernaya_kategoria->cat_ID) . '" title="' .
                        $dochernaya_kategoria->category_description . '">';
                    $na_akran .= $dochernaya_kategoria->cat_name . '</a>';
                    $na_akran .= '</li>' . "\n";
                endif;
            endforeach;
            $na_akran .= '</ul>' . "\n";
            print $na_akran; ?>

            </ul>

            <select id="tinynav2" class="tinynav tinynav2"><option value="/?city_id=17" selected="selected">Все</option><option value="/?district_id=60">Сортировка</option><option value="/?district_id=70">Центр</option><option value="/?district_id=71">УРАЛМАШ</option><option value="/?district_id=91">Кировский</option><option value="/?district_id=97">ХИММАШ</option><option value="/?district_id=104">Шарташ</option><option value="/?district_id=114">ЖБИ</option><option value="/?district_id=125">Уктус</option><option value="/?district_id=137">ЭЛЬМАШ</option><option value="/?district_id=148">Октябрьский</option><option value="/?district_id=230">Широкая речка</option><option value="/?district_id=493">Рудный</option><option value="/?district_id=495">г. Березовский</option><option value="/?district_id=498">Разные районы</option><option value="/?district_id=580">Мега</option></select>
        </div>
    </div>
</div>
    </section>
    </div>
</div>
<?php get_footer(); ?>
