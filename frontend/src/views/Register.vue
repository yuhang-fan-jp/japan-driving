<template>
  <div class="page">
    <div class="card">
      <h1 class="title">注册账号</h1>
      <p class="subtitle">创建一个新账号开始练习</p>

      <input
        v-model="email"
        type="email"
        placeholder="邮箱"
        class="input"
      />

      <input
        v-model="password"
        type="password"
        placeholder="密码（至少 6 位）"
        class="input"
      />

      <input
        v-model="confirm"
        type="password"
        placeholder="确认密码"
        class="input"
      />

      <button class="btn primary" :disabled="loading" @click="register">
        {{ loading ? "注册中..." : "注册" }}
      </button>

      <p class="error" v-if="error">{{ error }}</p>

      <div class="footer">
        <span>已有账号？</span>
        <button class="link" @click="goLogin">去登录</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import http from "../api/http";

const router = useRouter();

const email = ref("");
const password = ref("");
const confirm = ref("");
const loading = ref(false);
const error = ref("");

const register = async () => {
  if (!email.value || !password.value || !confirm.value) {
    error.value = "请填写完整信息";
    return;
  }

  if (password.value.length < 6) {
    error.value = "密码至少 6 位";
    return;
  }

  if (password.value !== confirm.value) {
    error.value = "两次密码不一致";
    return;
  }

  error.value = "";
  loading.value = true;

  try {
    await http.post("/register", {
      email: email.value,
      password: password.value,
    });

    alert("注册成功，请登录");
    router.push("/login");
  } catch (e: any) {
    error.value =
      e?.response?.data?.detail || "注册失败，邮箱可能已存在";
  } finally {
    loading.value = false;
  }
};

const goLogin = () => {
  router.push("/login");
};
</script>

<style scoped>
/* 和 Login.vue 完全一致，保证风格统一 */
* {
  box-sizing: border-box;
}
.page {
  min-height: 100vh;
  background: #f5f7fa;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px;
}

.card {
  width: 100%;
  max-width: 360px;
  background: #fff;
  border-radius: 20px;
  padding: 32px 24px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}

.title {
  text-align: center;
  margin-bottom: 4px;
}

.subtitle {
  text-align: center;
  color: #888;
  font-size: 14px;
  margin-bottom: 24px;
}

.input {
  width: 100%;
  padding: 14px 16px;
  margin-bottom: 16px;
  border-radius: 12px;
  border: 1px solid #ddd;
  font-size: 15px;
}

.input:focus {
  outline: none;
  border-color: #1677ff;
}

.btn {
  width: 100%;
  padding: 14px;
  border-radius: 14px;
  border: none;
  font-size: 16px;
  cursor: pointer;
}

.btn.primary {
  background: #1677ff;
  color: #fff;
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.error {
  margin-top: 12px;
  color: #cf1322;
  text-align: center;
  font-size: 14px;
}

.footer {
  margin-top: 24px;
  text-align: center;
  font-size: 14px;
  color: #666;
}

.link {
  background: none;
  border: none;
  color: #1677ff;
  cursor: pointer;
  margin-left: 4px;
}
</style>
