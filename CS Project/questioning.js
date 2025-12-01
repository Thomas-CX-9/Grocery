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
const questionKeysOfLV1 = Object.keys(questionsOfLV1);
console.log(questionKeysOfLV1);