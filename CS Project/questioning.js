function shuttleArray(array){
    for (let i = 0; i < 10; i++){
        let randomIndex = Math.floor(Math.random() * array.length);
        let temp = array[i];
        array[i] = array[randomIndex];
        array[randomIndex] = temp;
    }
    return array;
}
const questionsOfLV1 = {
    中國發射的第一顆人造衛星是 : {
        correct : "東方紅一號",
        incorrect : ["天宮一號", "神舟一號", "嫦娥一號"]
    },
    中國首位進入太空的航天員是誰 : {
        correct : "楊利偉",
        incorrect : ["翟志剛", "景海鵬", "聶海勝"]
    },
    中國的探月工程被命名為什麼 : {
        correct : "嫦娥工程",
        incorrect : ["天問工程", "后羿工程", "織女工程"]
    },
    中國主要的運載火箭系列名稱是 : {
        correct : "長征系列",
        incorrect : ["先鋒", "勝利者", "開拓者"]
    },
    中國自主研發的全球衛星導航系統是 : {
        correct : "北斗",
        incorrect : ["GPS", "格洛納斯", "伽利略"]
    }
}
const questionsOfLV2 = {
    神舟飛船與天宮目標飛行器間的對接方式是 : {
        correct : "自動對接",
        incorrect : ["剛性對接", "手動對接", "軟性對接"]
    },
    首次實現月球軟著陸及巡視探測的任務是 : {
        correct : "嫦娥三號",
        incorrect : ["嫦娥一號", "嫦娥二號", "嫦娥四號" ]
    },
    天問一號在火星實現了哪三個目標 : {
        correct : "繞、落、探",
        incorrect : ["飛、繞、回", "探、建、返", "繞、落、建"]
    },
    中國空間站的正式名稱是 : {
        correct : "天宮",
        incorrect : ["東方之星", "崑崙", "華夏"]
    },
    執行載人任務的長征火箭型號通常是 : {
        correct : "長征二號",
        incorrect : ["長征七號", "長征十號", "長征五號"]
    }
}
const questionsOfLV3 = {
    中國首個貨運飛船的名稱是 : {
        correct : "天舟一號",
        incorrect : ["神舟八號", "嫦娥五號", "北斗三號"]
    },
    人類首次在月球背面軟著陸的任務是 : {
        correct : "嫦娥四號",
        incorrect : ["嫦娥三號", "嫦娥五號", "嫦娥二號"]
    },
    長征五號系列火箭的暱稱是 : {
        correct : "胖五",
        incorrect : ['擎天柱', '大力士', '巨龍']
    },
    北斗系統實現高精度定位的基礎是 : {
        correct : "時頻同步",
        incorrect : ["姿態控制", "激光測距", "太陽帆板"]
    },
    神舟飛船返回艙在返回時採用何種降落方式 : {
        correct : "氣動減速傘降",
        incorrect : ["水面迫降", "軌道制動降落", "彈道式降落"]
    }
}
const questionsOfLV4 = {
    中國規劃中的可重複使用火箭採用哪種技術 : {
        correct : "垂直起降",
        incorrect : ["水平降落", "水平起飛", "垂直回收"]
    },
    負責將空間站核心艙送入軌道的重型火箭是 : {
        correct : "長征五號",
        incorrect : ["長征七號", "長征八號", "長征三號"]
    },
    天問一號探測器成功著陸火星的區域是 : {
        correct : "烏托邦平原",
        incorrect : ["祝融平原", "火星北極", "勇氣平原"]
    },
    中國空間站的哪個艙段是核心艙 : {
        correct : "天和",
        incorrect : ["問天", "夢天", "載和"]
    },
    嫦娥五號從月球採樣返回的關鍵技術是 : {
        correct : "三者皆是",
        incorrect : ["月面鑽取", "軌道無人交會", "高速再入"]
    }
}

const questionKeysOfLV1 = shuttleArray(Object.keys(questionsOfLV1));
const questionKeysOfLV2 = shuttleArray(Object.keys(questionsOfLV2));
const questionKeysOfLV3 = shuttleArray(Object.keys(questionsOfLV3));
const questionKeysOfLV4 = shuttleArray(Object.keys(questionsOfLV4));