# v9 TTS 音频预制方案

## 概述
将 KidStart 所有语音从实时在线 TTS 改为预制 CDN 静态音频，提升加载速度、离线可用、节约 API 调用。

## 技术方案
- TTS 服务：火山引擎 灿灿2.0（BV700_V2_streaming）
- 格式：mp3
- 语速：0.9（适合6岁小朋友）
- CDN：`https://cdn.onemilelab.com/audio/`

## 一、词汇音频（160词 × 3 = 480条）

| # | 场景 | 文件 | 英文文本 | 中文文本 | 例句文本 |
|---|------|------|----------|----------|----------|
| 1 | fruit-kitchen | words/apple.mp3 | apple | 苹果 | I like apples |
| 2 | fruit-kitchen | words/banana.mp3 | banana | 香蕉 | The monkey eats a banana |
| 3 | fruit-kitchen | words/orange.mp3 | orange | 橙子 | I drink orange juice |
| 4 | fruit-kitchen | words/grape.mp3 | grape | 葡萄 | These grapes are sweet |
| 5 | fruit-kitchen | words/watermelon.mp3 | watermelon | 西瓜 | Watermelon is big and sweet |
| 6 | fruit-kitchen | words/strawberry.mp3 | strawberry | 草莓 | I love strawberry cake |
| 7 | fruit-kitchen | words/pear.mp3 | pear | 梨 | The pear is green |
| 8 | fruit-kitchen | words/peach.mp3 | peach | 桃子 | This peach smells good |
| 9 | fruit-kitchen | words/cherry.mp3 | cherry | 樱桃 | Cherries are small and red |
| 10 | fruit-kitchen | words/pineapple.mp3 | pineapple | 菠萝 | Pineapple is sweet and sour |
| 11 | animal-farm | words/cow.mp3 | cow | 奶牛 | The cow eats grass |
| 12 | animal-farm | words/pig.mp3 | pig | 小猪 | The pig is pink |
| 13 | animal-farm | words/chicken.mp3 | chicken | 小鸡 | The chicken lays an egg |
| 14 | animal-farm | words/horse.mp3 | horse | 马 | I can ride a horse |
| 15 | animal-farm | words/sheep.mp3 | sheep | 绵羊 | The sheep has white wool |
| 16 | animal-farm | words/duck.mp3 | duck | 鸭子 | The duck swims in the pond |
| 17 | animal-farm | words/dog.mp3 | dog | 狗 | My dog is very cute |
| 18 | animal-farm | words/cat.mp3 | cat | 猫 | The cat is sleeping |
| 19 | animal-farm | words/rabbit.mp3 | rabbit | 兔子 | The rabbit likes carrots |
| 20 | animal-farm | words/rooster.mp3 | rooster | 公鸡 | The rooster crows at dawn |
| 21 | color-park | words/red.mp3 | red | 红色 | The apple is red |
| 22 | color-park | words/blue.mp3 | blue | 蓝色 | The sky is blue |
| 23 | color-park | words/green.mp3 | green | 绿色 | The leaf is green |
| 24 | color-park | words/yellow.mp3 | yellow | 黄色 | The sun is yellow |
| 25 | color-park | words/purple.mp3 | purple | 紫色 | I like purple grapes |
| 26 | color-park | words/orange.mp3 | orange | 橙色 | The pumpkin is orange |
| 27 | color-park | words/pink.mp3 | pink | 粉色 | Her dress is pink |
| 28 | color-park | words/black.mp3 | black | 黑色 | The cat is black |
| 29 | color-park | words/white.mp3 | white | 白色 | Snow is white |
| 30 | color-park | words/rainbow.mp3 | rainbow | 彩虹 | The rainbow is so pretty |
| 31 | food-street | words/bread.mp3 | bread | 面包 | I eat bread for breakfast |
| 32 | food-street | words/rice.mp3 | rice | 米饭 | I love eating rice |
| 33 | food-street | words/egg.mp3 | egg | 鸡蛋 | I have an egg every day |
| 34 | food-street | words/milk.mp3 | milk | 牛奶 | Milk is good for you |
| 35 | food-street | words/cake.mp3 | cake | 蛋糕 | We eat cake on birthdays |
| 36 | food-street | words/pizza.mp3 | pizza | 披萨 | Pizza is my favorite food |
| 37 | food-street | words/noodle.mp3 | noodle | 面条 | I want to eat noodles |
| 38 | food-street | words/cookie.mp3 | cookie | 饼干 | Can I have a cookie |
| 39 | food-street | words/juice.mp3 | juice | 果汁 | I want some apple juice |
| 40 | food-street | words/chocolate.mp3 | chocolate | 巧克力 | I love chocolate so much |
| 41 | body-land | words/eye.mp3 | eye | 眼睛 | I have two eyes |
| 42 | body-land | words/nose.mp3 | nose | 鼻子 | My nose can smell flowers |
| 43 | body-land | words/mouth.mp3 | mouth | 嘴巴 | Open your mouth please |
| 44 | body-land | words/ear.mp3 | ear | 耳朵 | I hear with my ears |
| 45 | body-land | words/hand.mp3 | hand | 手 | Wash your hands please |
| 46 | body-land | words/foot.mp3 | foot | 脚 | I have two feet |
| 47 | body-land | words/head.mp3 | head | 头 | Touch your head |
| 48 | body-land | words/hair.mp3 | hair | 头发 | Her hair is long |
| 49 | body-land | words/tooth.mp3 | tooth | 牙齿 | Brush your teeth every day |
| 50 | body-land | words/shoulder.mp3 | shoulder | 肩膀 | Head shoulders knees and toes |
| 51 | number-park | words/one.mp3 | one | 一 | I have one nose |
| 52 | number-park | words/two.mp3 | two | 二 | I have two hands |
| 53 | number-park | words/three.mp3 | three | 三 | Three little cats |
| 54 | number-park | words/four.mp3 | four | 四 | A table has four legs |
| 55 | number-park | words/five.mp3 | five | 五 | Give me a high five |
| 56 | number-park | words/six.mp3 | six | 六 | I am six years old |
| 57 | number-park | words/seven.mp3 | seven | 七 | Seven days in a week |
| 58 | number-park | words/eight.mp3 | eight | 八 | The octopus has eight arms |
| 59 | number-park | words/nine.mp3 | nine | 九 | Nine plus one is ten |
| 60 | number-park | words/ten.mp3 | ten | 十 | I have ten fingers |
| 61 | family-home | words/mom.mp3 | mom | 妈妈 | I love my mom |
| 62 | family-home | words/dad.mp3 | dad | 爸爸 | Dad is very tall |
| 63 | family-home | words/baby.mp3 | baby | 宝宝 | The baby is smiling |
| 64 | family-home | words/sister.mp3 | sister | 姐姐/妹妹 | My sister plays with me |
| 65 | family-home | words/brother.mp3 | brother | 哥哥/弟弟 | My brother is funny |
| 66 | family-home | words/grandma.mp3 | grandma | 奶奶/姥姥 | Grandma tells me stories |
| 67 | family-home | words/grandpa.mp3 | grandpa | 爷爷/姥爷 | Grandpa is very kind |
| 68 | family-home | words/family.mp3 | family | 家庭 | I love my family |
| 69 | family-home | words/home.mp3 | home | 家 | Let us go home |
| 70 | family-home | words/love.mp3 | love | 爱 | I love you so much |
| 71 | transport-city | words/car.mp3 | car | 汽车 | Dad drives a car |
| 72 | transport-city | words/bus.mp3 | bus | 公交车 | I go to school by bus |
| 73 | transport-city | words/bike.mp3 | bike | 自行车 | I can ride a bike |
| 74 | transport-city | words/train.mp3 | train | 火车 | The train is very fast |
| 75 | transport-city | words/boat.mp3 | boat | 船 | The boat is on the water |
| 76 | transport-city | words/plane.mp3 | plane | 飞机 | The plane flies in the sky |
| 77 | transport-city | words/truck.mp3 | truck | 卡车 | The truck is very big |
| 78 | transport-city | words/taxi.mp3 | taxi | 出租车 | Take a taxi to the park |
| 79 | transport-city | words/subway.mp3 | subway | 地铁 | We take the subway |
| 80 | transport-city | words/helicopter.mp3 | helicopter | 直升机 | The helicopter is so cool |
| 81 | weather-sky | words/sun.mp3 | sun | 太阳 | The sun is bright |
| 82 | weather-sky | words/rain.mp3 | rain | 雨 | It is raining today |
| 83 | weather-sky | words/cloud.mp3 | cloud | 云 | The clouds are white |
| 84 | weather-sky | words/snow.mp3 | snow | 雪 | I love playing in the snow |
| 85 | weather-sky | words/wind.mp3 | wind | 风 | The wind is blowing |
| 86 | weather-sky | words/hot.mp3 | hot | 热 | It is very hot today |
| 87 | weather-sky | words/cold.mp3 | cold | 冷 | Winter is very cold |
| 88 | weather-sky | words/star.mp3 | star | 星星 | I can see many stars |
| 89 | weather-sky | words/moon.mp3 | moon | 月亮 | The moon is round tonight |
| 90 | weather-sky | words/thunder.mp3 | thunder | 雷 | Thunder is very loud |
| 91 | clothes-closet | words/shirt.mp3 | shirt | 衬衫 | I wear a blue shirt |
| 92 | clothes-closet | words/pants.mp3 | pants | 裤子 | These pants are new |
| 93 | clothes-closet | words/shoes.mp3 | shoes | 鞋子 | Put on your shoes |
| 94 | clothes-closet | words/hat.mp3 | hat | 帽子 | I like my red hat |
| 95 | clothes-closet | words/socks.mp3 | socks | 袜子 | My socks are colorful |
| 96 | clothes-closet | words/dress.mp3 | dress | 裙子 | She wears a pretty dress |
| 97 | clothes-closet | words/coat.mp3 | coat | 外套 | Wear your coat it is cold |
| 98 | clothes-closet | words/scarf.mp3 | scarf | 围巾 | The scarf is warm |
| 99 | clothes-closet | words/gloves.mp3 | gloves | 手套 | I need my gloves |
| 100 | clothes-closet | words/sunglasses.mp3 | sunglasses | 太阳镜 | Cool sunglasses for summer |
| 101 | school-class | words/book.mp3 | book | 书 | I read a book every day |
| 102 | school-class | words/pen.mp3 | pen | 笔 | Give me a pen please |
| 103 | school-class | words/bag.mp3 | bag | 书包 | My bag is very heavy |
| 104 | school-class | words/desk.mp3 | desk | 桌子 | Sit at your desk |
| 105 | school-class | words/teacher.mp3 | teacher | 老师 | My teacher is very nice |
| 106 | school-class | words/friend.mp3 | friend | 朋友 | She is my best friend |
| 107 | school-class | words/crayon.mp3 | crayon | 蜡笔 | I draw with crayons |
| 108 | school-class | words/paper.mp3 | paper | 纸 | Give me a piece of paper |
| 109 | school-class | words/clock.mp3 | clock | 钟 | Look at the clock |
| 110 | school-class | words/homework.mp3 | homework | 作业 | I finished my homework |
| 111 | playground | words/ball.mp3 | ball | 球 | Let us play ball |
| 112 | playground | words/tree.mp3 | tree | 树 | The tree is very tall |
| 113 | playground | words/flower.mp3 | flower | 花 | The flower is beautiful |
| 114 | playground | words/swing.mp3 | swing | 秋千 | I love the swing |
| 115 | playground | words/slide.mp3 | slide | 滑梯 | The slide is so fun |
| 116 | playground | words/kite.mp3 | kite | 风筝 | Let us fly a kite |
| 117 | playground | words/bird.mp3 | bird | 鸟 | The bird is singing |
| 118 | playground | words/butterfly.mp3 | butterfly | 蝴蝶 | The butterfly is colorful |
| 119 | playground | words/balloon.mp3 | balloon | 气球 | I have a red balloon |
| 120 | playground | words/ladybug.mp3 | ladybug | 瓢虫 | The ladybug has black dots |
| 121 | ocean-world | words/fish.mp3 | fish | 鱼 | The fish swims fast |
| 122 | ocean-world | words/shell.mp3 | shell | 贝壳 | I found a pretty shell |
| 123 | ocean-world | words/water.mp3 | water | 水 | I drink water every day |
| 124 | ocean-world | words/whale.mp3 | whale | 鲸鱼 | The whale is very big |
| 125 | ocean-world | words/crab.mp3 | crab | 螃蟹 | The crab walks sideways |
| 126 | ocean-world | words/shark.mp3 | shark | 鲨鱼 | Baby shark doo doo |
| 127 | ocean-world | words/turtle.mp3 | turtle | 海龟 | The turtle is slow |
| 128 | ocean-world | words/dolphin.mp3 | dolphin | 海豚 | The dolphin jumps high |
| 129 | ocean-world | words/starfish.mp3 | starfish | 海星 | The starfish has five arms |
| 130 | ocean-world | words/octopus.mp3 | octopus | 章鱼 | The octopus has eight legs |
| 131 | space-voyage | words/rocket.mp3 | rocket | 火箭 | The rocket goes to space |
| 132 | space-voyage | words/earth.mp3 | earth | 地球 | We live on Earth |
| 133 | space-voyage | words/sky.mp3 | sky | 天空 | The sky is very high |
| 134 | space-voyage | words/planet.mp3 | planet | 星球 | Mars is a red planet |
| 135 | space-voyage | words/robot.mp3 | robot | 机器人 | The robot can dance |
| 136 | space-voyage | words/alien.mp3 | alien | 外星人 | Hello little alien |
| 137 | space-voyage | words/satellite.mp3 | satellite | 卫星 | The satellite is in space |
| 138 | space-voyage | words/comet.mp3 | comet | 彗星 | The comet has a long tail |
| 139 | space-voyage | words/telescope.mp3 | telescope | 望远镜 | I look through the telescope |
| 140 | space-voyage | words/astronaut.mp3 | astronaut | 宇航员 | I want to be an astronaut |
| 141 | sports-field | words/run.mp3 | run | 跑 | I can run very fast |
| 142 | sports-field | words/jump.mp3 | jump | 跳 | Jump as high as you can |
| 143 | sports-field | words/swim.mp3 | swim | 游泳 | I like to swim |
| 144 | sports-field | words/kick.mp3 | kick | 踢 | Kick the ball hard |
| 145 | sports-field | words/catch.mp3 | catch | 接住 | Catch the ball |
| 146 | sports-field | words/throw.mp3 | throw | 扔 | Throw the ball to me |
| 147 | sports-field | words/dance.mp3 | dance | 跳舞 | I love to dance |
| 148 | sports-field | words/climb.mp3 | climb | 爬 | Climb up the tree |
| 149 | sports-field | words/race.mp3 | race | 比赛 | Let us have a race |
| 150 | sports-field | words/champion.mp3 | champion | 冠军 | I am the champion today |
| 151 | party-time | words/happy.mp3 | happy | 开心 | I am so happy today |
| 152 | party-time | words/sing.mp3 | sing | 唱歌 | Let us sing a song |
| 153 | party-time | words/gift.mp3 | gift | 礼物 | Thank you for the gift |
| 154 | party-time | words/candle.mp3 | candle | 蜡烛 | Blow out the candles |
| 155 | party-time | words/candy.mp3 | candy | 糖果 | I love candy |
| 156 | party-time | words/ice cream.mp3 | ice cream | 冰淇淋 | I want ice cream please |
| 157 | party-time | words/music.mp3 | music | 音乐 | I like this music |
| 158 | party-time | words/clown.mp3 | clown | 小丑 | The clown is very funny |
| 159 | party-time | words/fireworks.mp3 | fireworks | 烟花 | The fireworks are beautiful |
| 160 | party-time | words/birthday.mp3 | birthday | 生日 | Happy birthday to you |

### CDN 路径
- 英文单词：`audio/words/{word}.mp3`
- 中文释义：`audio/chinese/{word}.mp3`
- 英文例句：`audio/sentences/{word}.mp3`

## 二、引导语/鼓励语音频

### 2.1 audio.js GUIDE_TEXTS（10条）

| key | 文本 | 文件 |
|-----|------|------|
| new-word | 来认识一个新词吧 | guide/new-word.mp3 |
| remember | 记住了就点绿色按钮 | guide/remember.mp3 |
| quiz | 哪个是正确的？点一点 | guide/quiz.mp3 |
| correct | 太棒了 | guide/correct.mp3 |
| wrong | 没关系，看看正确答案 | guide/wrong.mp3 |
| tpr | 跟着做动作吧 | guide/tpr.mp3 |
| tpr-done | 做完了就点按钮 | guide/tpr-done.mp3 |
| summary | 今天学了这些词，真棒 | guide/summary.mp3 |
| lesson-done | 课程完成啦 | guide/lesson-done.mp3 |
| eye-rest | 让眼睛休息一下吧，看看远处 | guide/eye-rest.mp3 |

### 2.2 word-card.js 交互语音（去重后11条）

| 文本 | 文件 |
|------|------|
| 猜猜看，这是什么呢？ | guide/guess-what.mp3 |
| 来跟我读一读 | guide/read-along.mp3 |
| 读得真棒！ | guide/read-great.mp3 |
| 太棒了！ | guide/awesome.mp3 |
| 拼出这个词 | guide/spell-it.mp3 |
| 不对哦，再试一次 | guide/try-again.mp3 |
| 太厉害了，全对！ | guide/all-correct.mp3 |
| 差一点点，再试试 | guide/almost.mp3 |
| 再试一次！ | guide/retry.mp3 |
| 答对啦！ | guide/got-it.mp3 |
| 你是语言天才！ | guide/genius.mp3 |
| 继续加油！ | guide/keep-going.mp3 |
| Perfect! | guide/perfect.mp3 |

### 2.3 "这是{中文}" 变体（160条）

| 文本 | 文件 |
|------|------|
| 这是苹果 | guide/this-is-apple.mp3 |
| 这是香蕉 | guide/this-is-banana.mp3 |
| 这是橙子 | guide/this-is-orange.mp3 |
| 这是葡萄 | guide/this-is-grape.mp3 |
| 这是西瓜 | guide/this-is-watermelon.mp3 |
| 这是草莓 | guide/this-is-strawberry.mp3 |
| 这是梨 | guide/this-is-pear.mp3 |
| 这是桃子 | guide/this-is-peach.mp3 |
| 这是樱桃 | guide/this-is-cherry.mp3 |
| 这是菠萝 | guide/this-is-pineapple.mp3 |
| 这是奶牛 | guide/this-is-cow.mp3 |
| 这是小猪 | guide/this-is-pig.mp3 |
| 这是小鸡 | guide/this-is-chicken.mp3 |
| 这是马 | guide/this-is-horse.mp3 |
| 这是绵羊 | guide/this-is-sheep.mp3 |
| 这是鸭子 | guide/this-is-duck.mp3 |
| 这是狗 | guide/this-is-dog.mp3 |
| 这是猫 | guide/this-is-cat.mp3 |
| 这是兔子 | guide/this-is-rabbit.mp3 |
| 这是公鸡 | guide/this-is-rooster.mp3 |
| 这是红色 | guide/this-is-red.mp3 |
| 这是蓝色 | guide/this-is-blue.mp3 |
| 这是绿色 | guide/this-is-green.mp3 |
| 这是黄色 | guide/this-is-yellow.mp3 |
| 这是紫色 | guide/this-is-purple.mp3 |
| 这是橙色 | guide/this-is-orange.mp3 |
| 这是粉色 | guide/this-is-pink.mp3 |
| 这是黑色 | guide/this-is-black.mp3 |
| 这是白色 | guide/this-is-white.mp3 |
| 这是彩虹 | guide/this-is-rainbow.mp3 |
| 这是面包 | guide/this-is-bread.mp3 |
| 这是米饭 | guide/this-is-rice.mp3 |
| 这是鸡蛋 | guide/this-is-egg.mp3 |
| 这是牛奶 | guide/this-is-milk.mp3 |
| 这是蛋糕 | guide/this-is-cake.mp3 |
| 这是披萨 | guide/this-is-pizza.mp3 |
| 这是面条 | guide/this-is-noodle.mp3 |
| 这是饼干 | guide/this-is-cookie.mp3 |
| 这是果汁 | guide/this-is-juice.mp3 |
| 这是巧克力 | guide/this-is-chocolate.mp3 |
| 这是眼睛 | guide/this-is-eye.mp3 |
| 这是鼻子 | guide/this-is-nose.mp3 |
| 这是嘴巴 | guide/this-is-mouth.mp3 |
| 这是耳朵 | guide/this-is-ear.mp3 |
| 这是手 | guide/this-is-hand.mp3 |
| 这是脚 | guide/this-is-foot.mp3 |
| 这是头 | guide/this-is-head.mp3 |
| 这是头发 | guide/this-is-hair.mp3 |
| 这是牙齿 | guide/this-is-tooth.mp3 |
| 这是肩膀 | guide/this-is-shoulder.mp3 |
| 这是一 | guide/this-is-one.mp3 |
| 这是二 | guide/this-is-two.mp3 |
| 这是三 | guide/this-is-three.mp3 |
| 这是四 | guide/this-is-four.mp3 |
| 这是五 | guide/this-is-five.mp3 |
| 这是六 | guide/this-is-six.mp3 |
| 这是七 | guide/this-is-seven.mp3 |
| 这是八 | guide/this-is-eight.mp3 |
| 这是九 | guide/this-is-nine.mp3 |
| 这是十 | guide/this-is-ten.mp3 |
| 这是妈妈 | guide/this-is-mom.mp3 |
| 这是爸爸 | guide/this-is-dad.mp3 |
| 这是宝宝 | guide/this-is-baby.mp3 |
| 这是姐姐/妹妹 | guide/this-is-sister.mp3 |
| 这是哥哥/弟弟 | guide/this-is-brother.mp3 |
| 这是奶奶/姥姥 | guide/this-is-grandma.mp3 |
| 这是爷爷/姥爷 | guide/this-is-grandpa.mp3 |
| 这是家庭 | guide/this-is-family.mp3 |
| 这是家 | guide/this-is-home.mp3 |
| 这是爱 | guide/this-is-love.mp3 |
| 这是汽车 | guide/this-is-car.mp3 |
| 这是公交车 | guide/this-is-bus.mp3 |
| 这是自行车 | guide/this-is-bike.mp3 |
| 这是火车 | guide/this-is-train.mp3 |
| 这是船 | guide/this-is-boat.mp3 |
| 这是飞机 | guide/this-is-plane.mp3 |
| 这是卡车 | guide/this-is-truck.mp3 |
| 这是出租车 | guide/this-is-taxi.mp3 |
| 这是地铁 | guide/this-is-subway.mp3 |
| 这是直升机 | guide/this-is-helicopter.mp3 |
| 这是太阳 | guide/this-is-sun.mp3 |
| 这是雨 | guide/this-is-rain.mp3 |
| 这是云 | guide/this-is-cloud.mp3 |
| 这是雪 | guide/this-is-snow.mp3 |
| 这是风 | guide/this-is-wind.mp3 |
| 这是热 | guide/this-is-hot.mp3 |
| 这是冷 | guide/this-is-cold.mp3 |
| 这是星星 | guide/this-is-star.mp3 |
| 这是月亮 | guide/this-is-moon.mp3 |
| 这是雷 | guide/this-is-thunder.mp3 |
| 这是衬衫 | guide/this-is-shirt.mp3 |
| 这是裤子 | guide/this-is-pants.mp3 |
| 这是鞋子 | guide/this-is-shoes.mp3 |
| 这是帽子 | guide/this-is-hat.mp3 |
| 这是袜子 | guide/this-is-socks.mp3 |
| 这是裙子 | guide/this-is-dress.mp3 |
| 这是外套 | guide/this-is-coat.mp3 |
| 这是围巾 | guide/this-is-scarf.mp3 |
| 这是手套 | guide/this-is-gloves.mp3 |
| 这是太阳镜 | guide/this-is-sunglasses.mp3 |
| 这是书 | guide/this-is-book.mp3 |
| 这是笔 | guide/this-is-pen.mp3 |
| 这是书包 | guide/this-is-bag.mp3 |
| 这是桌子 | guide/this-is-desk.mp3 |
| 这是老师 | guide/this-is-teacher.mp3 |
| 这是朋友 | guide/this-is-friend.mp3 |
| 这是蜡笔 | guide/this-is-crayon.mp3 |
| 这是纸 | guide/this-is-paper.mp3 |
| 这是钟 | guide/this-is-clock.mp3 |
| 这是作业 | guide/this-is-homework.mp3 |
| 这是球 | guide/this-is-ball.mp3 |
| 这是树 | guide/this-is-tree.mp3 |
| 这是花 | guide/this-is-flower.mp3 |
| 这是秋千 | guide/this-is-swing.mp3 |
| 这是滑梯 | guide/this-is-slide.mp3 |
| 这是风筝 | guide/this-is-kite.mp3 |
| 这是鸟 | guide/this-is-bird.mp3 |
| 这是蝴蝶 | guide/this-is-butterfly.mp3 |
| 这是气球 | guide/this-is-balloon.mp3 |
| 这是瓢虫 | guide/this-is-ladybug.mp3 |
| 这是鱼 | guide/this-is-fish.mp3 |
| 这是贝壳 | guide/this-is-shell.mp3 |
| 这是水 | guide/this-is-water.mp3 |
| 这是鲸鱼 | guide/this-is-whale.mp3 |
| 这是螃蟹 | guide/this-is-crab.mp3 |
| 这是鲨鱼 | guide/this-is-shark.mp3 |
| 这是海龟 | guide/this-is-turtle.mp3 |
| 这是海豚 | guide/this-is-dolphin.mp3 |
| 这是海星 | guide/this-is-starfish.mp3 |
| 这是章鱼 | guide/this-is-octopus.mp3 |
| 这是火箭 | guide/this-is-rocket.mp3 |
| 这是地球 | guide/this-is-earth.mp3 |
| 这是天空 | guide/this-is-sky.mp3 |
| 这是星球 | guide/this-is-planet.mp3 |
| 这是机器人 | guide/this-is-robot.mp3 |
| 这是外星人 | guide/this-is-alien.mp3 |
| 这是卫星 | guide/this-is-satellite.mp3 |
| 这是彗星 | guide/this-is-comet.mp3 |
| 这是望远镜 | guide/this-is-telescope.mp3 |
| 这是宇航员 | guide/this-is-astronaut.mp3 |
| 这是跑 | guide/this-is-run.mp3 |
| 这是跳 | guide/this-is-jump.mp3 |
| 这是游泳 | guide/this-is-swim.mp3 |
| 这是踢 | guide/this-is-kick.mp3 |
| 这是接住 | guide/this-is-catch.mp3 |
| 这是扔 | guide/this-is-throw.mp3 |
| 这是跳舞 | guide/this-is-dance.mp3 |
| 这是爬 | guide/this-is-climb.mp3 |
| 这是比赛 | guide/this-is-race.mp3 |
| 这是冠军 | guide/this-is-champion.mp3 |
| 这是开心 | guide/this-is-happy.mp3 |
| 这是唱歌 | guide/this-is-sing.mp3 |
| 这是礼物 | guide/this-is-gift.mp3 |
| 这是蜡烛 | guide/this-is-candle.mp3 |
| 这是糖果 | guide/this-is-candy.mp3 |
| 这是冰淇淋 | guide/this-is-ice cream.mp3 |
| 这是音乐 | guide/this-is-music.mp3 |
| 这是小丑 | guide/this-is-clown.mp3 |
| 这是烟花 | guide/this-is-fireworks.mp3 |
| 这是生日 | guide/this-is-birthday.mp3 |

### 2.4 scene-quiz.js（2条，去重后新增）

| 文本 | 文件 |
|------|------|
| 你太厉害了！ | guide/super-awesome.mp3 |

### 2.5 scene-complete.js（5条）

| 文本 | 文件 |
|------|------|
| 满分！你是最棒的！ | guide/full-score.mp3 |
| 很不错，再接再厉 | guide/keep-it-up.mp3 |
| 加油，下次一定更好 | guide/next-time.mp3 |
| 真不错！ | guide/nice.mp3 |
| 加油加油！ | guide/go-go.mp3 |

### 2.6 scene-select.js（2条）

| 文本 | 文件 |
|------|------|
| 新的冒险等着你呢 | guide/new-adventure.mp3 |
| 欢迎回来，小探险家 | guide/welcome-back.mp3 |

### 2.7 card-reveal.js（5条）

| 文本 | 文件 |
|------|------|
| 获得了一张普通卡片 | guide/card-normal.mp3 |
| 哇，稀有卡片！ | guide/card-rare.mp3 |
| 太棒了！史诗卡片！ | guide/card-epic.mp3 |
| 天哪！传说卡片！ | guide/card-legendary.mp3 |
| 不可思议！彩虹传说！ | guide/card-ultimate.mp3 |

### 2.8 review.js（去重后新增2条）

| 文本 | 文件 |
|------|------|
| 记忆力真好！ | guide/good-memory.mp3 |
| 完美！ | guide/perfect-cn.mp3 |
| 继续保持！ | guide/keep-up.mp3 |
| 很棒！ | guide/very-good.mp3 |

## 三、音频统计

| 类别 | 数量 |
|------|------|
| 英文单词 | 160 |
| 中文释义 | 160 |
| 英文例句 | 160 |
| 引导语/鼓励语 | 200 |
| **总计** | **680** |

## 四、生成脚本要求

1. 读取 scenes.js 提取 160 词数据
2. 英文音频（单词+例句）：火山引擎 BV700_V2_streaming，语速 0.9
3. 中文音频（释义+引导语+鼓励语）：火山引擎 BV700_V2_streaming，语速 0.9
4. 输出 mp3 到本地目录，按 words/ chinese/ sentences/ guide/ 分目录
5. 上传到 Cloudflare Pages CDN (kidstart-assets 项目)
6. 修改 audio.js：从在线 TTS API 改为播放 CDN 静态文件

## 五、audio.js 改造要点

- playWord(word) → `https://cdn.onemilelab.com/audio/words/{word}.mp3`
- playSentence(sentence) → 按 word 查找 `audio/sentences/{word}.mp3`
- playGuide(key) → 先查 guide/{key}.mp3，支持 fallback
- 需要新增 playChinese(word) → `audio/chinese/{word}.mp3`
