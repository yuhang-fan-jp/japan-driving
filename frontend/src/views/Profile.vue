<template>
  <div class="page">
    <div class="card">
      <h1 class="title">个人设置</h1>

      <!-- 昵称 -->
      <label class="label">昵称</label>
      <input
        v-model="form.nickname"
        class="input"
        placeholder="最多20个汉字"
        maxlength="20"
      />

      <!-- 考试地区 -->
      <label class="label">考试地区</label>
      <select v-model="form.exam_region" class="input">
        <option value="">请选择地区</option>
        <option v-for="r in regions" :key="r" :value="r">
          {{ r }}
        </option>
      </select>

      <!-- 保存 -->
      <button class="btn primary" :disabled="loading" @click="saveProfile">
        {{ loading ? "保存中..." : "保存信息" }}
      </button>

      <div class="divider"></div>

      <!-- 修改密码 -->
      <label class="label">修改密码</label>
      <input
        v-model="password.old"
        type="password"
        class="input"
        placeholder="当前密码"
      />
      <input
        v-model="password.new"
        type="password"
        class="input"
        placeholder="新密码（至少6位）"
      />

      <button class="btn" @click="changePassword">
        修改密码
      </button>

      <div class="divider"></div>

      <!-- 退出登录 -->
      <button class="btn danger" @click="logout">
        退出登录
      </button>

      <p class="error" v-if="error">{{ error }}</p>
      <p class="success" v-if="success">{{ success }}</p>
    </div>
  </div>
</template>
<script setup lang="ts">
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";
import http from "../api/http";
console.log("Profile 页面加载了");//1月31日晚测试
const router = useRouter();
const loading = ref(false);
const error = ref("");
const success = ref("");

const regions = [
  "东京",
  "神奈川",
  "大阪",
  "爱知",
  "埼玉",
  "千叶",
  "北海道",
  "福冈",
  "其他",
];

const form = reactive({
  nickname: "",
  exam_region: "",
});

const password = reactive({
  old: "",
  new: "",
});

const saveProfile = async () => {
  if (!form.nickname || !form.exam_region) {
    error.value = "昵称和考试地区不能为空";
    return;
  }

  loading.value = true;
  error.value = "";
  success.value = "";

  try {
    await http.post("/user/profile", form);
    success.value = "保存成功";
  } catch {
    error.value = "保存失败";
  } finally {
    loading.value = false;
  }
};

const changePassword = async () => {
  if (!password.old || password.new.length < 6) {
    error.value = "密码填写不正确";
    return;
  }

  error.value = "";
  success.value = "";

  try {
    await http.post("/user/change-password", password);
    success.value = "密码修改成功";
    password.old = "";
    password.new = "";
  } catch {
    error.value = "密码修改失败";
  }
};

const logout = () => {
  localStorage.removeItem("token");
  router.push("/login");
};
</script>
<style scoped>
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
  margin-bottom: 24px;
}

.label {
  font-size: 13px;
  color: #555;
  margin-bottom: 6px;
  display: block;
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
  font-size: 15px;
  cursor: pointer;
  margin-bottom: 12px;
}

.btn.primary {
  background: #1677ff;
  color: #fff;
}

.btn.danger {
  background: #ff4d4f;
  color: #fff;
}

.divider {
  height: 1px;
  background: #eee;
  margin: 20px 0;
}

.error {
  color: #cf1322;
  text-align: center;
  font-size: 14px;
}

.success {
  color: #52c41a;
  text-align: center;
  font-size: 14px;
}
</style>
