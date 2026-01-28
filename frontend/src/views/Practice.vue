<template>
  <div class="container">
    <!-- 题目卡片 -->
    <div class="card">
      <div class="title">第 {{ index + 1 }} 题</div>
      <p class="question">{{ current.content }}</p>
    </div>

    <!-- 图片（可选） -->
    <div v-if="current.image_url" class="image-card">
      <img :src="current.image_url" />
    </div>

    <!-- 对 / 错 -->
    <div class="answer-buttons">
      <button
        class="btn true"
        :class="{ active: answers[current.id] === true }"
        @click="choose(true)"
      >
        对
      </button>

      <button
        class="btn false"
        :class="{ active: answers[current.id] === false }"
        @click="choose(false)"
      >
        错
      </button>
    </div>

    <!-- 上 / 下题 -->
    <div class="controls">
      <button class="btn ghost" @click="prev">上一题</button>
      <span>{{ index + 1 }} / {{ total }}</span>
      <button class="btn ghost" @click="next">下一题</button>
    </div>

    <!-- 底部 -->
    <div class="bottom">
      <button class="btn ghost" @click="goHome">返回首页</button>
      <span class="time">累计时间 {{ time }}</span>
      <button class="btn primary" @click="submit">交卷</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from "vue";
import { useRouter } from "vue-router";
import http from "../api/http";

const router = useRouter();

const questions = ref<any[]>([]);
const index = ref(0);
const answers = ref<Record<number, boolean>>({});

const total = computed(() => questions.value.length);
const current = computed(() => questions.value[index.value] || {});

// 计时
const seconds = ref(0);
const time = computed(() => {
  const m = String(Math.floor(seconds.value / 60)).padStart(2, "0");
  const s = String(seconds.value % 60).padStart(2, "0");
  return `${m}:${s}`;
});

let timer: number;

const fetchQuestions = async () => {
  const res = await http.get("/quiz/questions?limit=50");
  questions.value = res.data;
};

const choose = (value: boolean) => {
  answers.value[current.value.id] = value;
  if (index.value < total.value - 1) index.value++;
};

const prev = () => {
  if (index.value > 0) index.value--;
};

const next = () => {
  if (index.value < total.value - 1) index.value++;
};

const submit = async () => {
  const payload = {
    answers: Object.entries(answers.value).map(([qid, ans]) => ({
      question_id: Number(qid),
      answer: ans,
    })),
  };

  const res = await http.post("/quiz/submit", payload);
  router.push({ path: "/result", query: { score: res.data.score } });
};

const goHome = () => router.push("/home");

onMounted(() => {
  fetchQuestions();
  timer = window.setInterval(() => seconds.value++, 1000);
});

onUnmounted(() => {
  clearInterval(timer);
});
</script>

<style scoped>
.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 24px;
}

/* 卡片 */
.card,
.image-card {
  background: #fff;
  border-radius: 16px;
  padding: 24px;
  margin-bottom: 16px;
}

.title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 12px;
}

.question {
  font-size: 20px;
  line-height: 1.6;
}

.image-card img {
  width: 100%;
  border-radius: 12px;
}

/* 对 / 错 */
.answer-buttons {
  display: flex;
  gap: 16px;
  margin-top: 16px;
}

/* 控制区 */
.controls,
.bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
}

.time {
  font-weight: bold;
}

/* ===== 统一按钮系统 ===== */

.btn {
  padding: 14px 20px;
  font-size: 16px;
  border-radius: 14px;
  border: 2px solid transparent;
  cursor: pointer;
  transition: all 0.2s ease;
}

/* 判断题 */
.true {
  background: #f0f7ff;
  color: #0958d9;
}

.false {
  background: #fff1f0;
  color: #cf1322;
}

.btn.active {
  border-color: #1677ff;
  box-shadow: 0 0 0 3px rgba(22, 119, 255, 0.15);
}

.btn:hover {
  transform: translateY(-1px);
}

/* 其它按钮 */
.ghost {
  background: #fafafa;
  border: 1px solid #ddd;
}

.primary {
  background: #1677ff;
  color: #fff;
}
</style>