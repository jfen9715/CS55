<template>
  <section class="module">
    <div class="extra" v-if="!isMobile">
      <p>{{userName}}</p>
      <el-button type="primary" @click="toSave">Save</el-button>
    </div>
    <el-tabs :tab-position="tabPos" v-model="currentTab">
      <el-tab-pane name="module0">
        <span slot="label"><i v-if="finished[0]" class="el-icon-success"></i>Before you start</span>
         <section class="tab_content tab_content_0">
          <div class="tab_main tab_main_after">
            <h3>Before you start</h3>
            <p>Please answer a few short questions:</p>
            <el-form label-position="top" :model="formData.before">
              <el-form-item label="What is your gender?">
                <el-radio-group v-model="formData.before.gender">
                  <el-radio label="male">Male</el-radio>
                  <el-radio label="female">Female</el-radio>
                </el-radio-group>
              </el-form-item>
              <el-form-item label="What is your age?">
                <el-input v-model="formData.before.age" size="small"></el-input>
              </el-form-item>
            </el-form>
            <section class="btn">
              <el-button type="primary" @click="toNext(0)">Start<i class="el-icon-arrow-right el-icon--right"></i></el-button>
            </section>
          </div>
         </section>
      </el-tab-pane>
      <el-tab-pane name="module1" :disabled="!finished[0]">
        <span slot="label"><i v-if="finished[1]" class="el-icon-success"></i>1.Advantages and obstacles of telling</span>
        <section class="tab_content tab_content_1">
          <div class="tab_main tab_main_before" v-show="showModule!==1">
            <h3>Advantages and obstacles of telling</h3>
            <p>In this first section, you will use a list of possible advantages and obstacles to help you decide if you should tell someone at work or not. This list includes a number of options and will give you space to list some of your own. </p>
            <p>Disability discrimination law says that employers should make 'reasonable adjustments' for a person who is disabled by a mental health condition may need to do their job, such as changes to hours or parts of your job. Employers are only required to make these changes if they are made aware of your condition.</p>
            <section class="btn">
              <el-button type="primary" @click="toAnswer(1)">Answer Now<i class="el-icon-arrow-right el-icon--right"></i></el-button>
            </section>
          </div>
          <div class="tab_main tab_main_after" v-show="showModule===1">
            <h4>Below is a list of advantages and obstacles of telling people at work about your mental health condition. Please choose which advantages and obstacles are important, only select those that matter to you:</h4>
            <el-form label-position="top" :model="formData.module1">
              <el-form-item class="dialog" v-for="(value, key) in module1.choices" v-if="!checkChoice(key)" :key="key" :label="value">
                <el-radio-group v-model="AdvNObs[key]" @change="(res) => module1Change(res, key)">
                  <el-radio :label="1">Advantage</el-radio>
                  <el-radio :label="2">Obstacle</el-radio>
                </el-radio-group>
              </el-form-item>
              <el-table :data="formData.module1.advantages"  border style="width: 100%; margin: 20px 0">
                <el-table-column label="Advantages">
                  <template slot-scope="scope">
                    {{module1.choices[scope.row]}}
                  </template>
                </el-table-column>
                <el-table-column align="center" width="80px">
                  <template slot-scope="scope">
                    <el-button type="text" @click="deleteAdv(scope.$index)">delete</el-button>
                  </template>
                </el-table-column>
              </el-table>
              <el-table :data="formData.module1.obstacles"  border style="width: 100%; margin: 20px 0">
                <el-table-column label="Obstacles">
                  <template slot-scope="scope">
                    {{module1.choices[scope.row]}}
                  </template>
                </el-table-column>
                <el-table-column align="center" width="80px">
                  <template slot-scope="scope">
                    <el-button type="text" @click="deleteObs(scope.$index)">delete</el-button>
                  </template>
                </el-table-column>
              </el-table>
              <el-form-item label="Add my own advantages and obstacles">
                <el-input type="textarea" v-model="formData.module1.other"></el-input>
              </el-form-item>
            </el-form>
            <section class="btn tab_main_btn">
              <div v-if="isMobile" class="btn_div">
                <div class="btn_tip">
                  Save before you leave if you won't continue.<i class="el-icon-thumb"></i>
                </div>
                <el-button type="primary" @click="toSave">Save</el-button>
              </div>
              <el-button type="primary" @click="toNext(1)">Next<i class="el-icon-arrow-right el-icon--right"></i></el-button>
            </section>
          </div>
        </section>
      </el-tab-pane>
      <el-tab-pane name="module2" :disabled="!finished[1]">
        <span slot="label"><i v-if="finished[2]" class="el-icon-success"></i>2.'Needs' at work</span>
        <section class="tab_content tab_content_2">
          <div class="tab_main tab_main_before" v-show="showModule!==2">
            <h3>'Needs' at work</h3>
            <p>This section will focus on what you need at work in order to do your job well and stay healthy. Some people decide to tell people at work about their mental health condition to allow them to meet these needs.</p>
            <p>Thinking about your needs at work can be a helpful way to help make the decision to tell people at work. </p>
            <section class="btn">
              <el-button type="primary" @click="toAnswer(2)">Answer Now<i class="el-icon-arrow-right el-icon--right"></i></el-button>
            </section>
          </div>
          <div class="tab_main tab_main_after" v-show="showModule===2">
            <h4>Select how important these 'needs' are at work:</h4>
            <el-form label-position="top" :model="formData.module2">
              <el-form-item v-for="(value,key,index) in module2" :key="index" :label="value">
                <el-slider v-model="formData.module2[key]" :show-tooltip="false" :min="0" :max="4" :marks="needRadio" show-stops></el-slider>
              </el-form-item>
              <el-form-item>
                <el-checkbox label="others">Add my own needs</el-checkbox>
                <el-input type="textarea" v-model="formData.module2.otherNeeds"></el-input>
              </el-form-item>
            </el-form>
            <section class="btn tab_main_btn">
              <div v-if="isMobile" class="btn_div">
                <div class="btn_tip">
                  Save before you leave if you won't continue.<i class="el-icon-thumb"></i>
                </div>
                <el-button type="primary" @click="toSave">Save</el-button>
              </div>
              <el-button type="primary" @click="toNext(2)">Next<i class="el-icon-arrow-right el-icon--right"></i></el-button>
            </section>
          </div>
        </section>
      </el-tab-pane>
      <el-tab-pane name="module3" :disabled="!finished[2]">
        <span slot="label"><i v-if="finished[3]" class="el-icon-success"></i>3.'Values' at work</span>
        <section class="tab_content tab_content_3">
          <div class="tab_main tab_main_before" v-show="showModule!==3">
            <h3>'Values' at work</h3>
            <p>This section describes some values (traits or qualities) which a person considers important. Your values can play an important role in your decision to tell people at work about your mental health.</p>
            <p>Thinking about your values can be a helpful way to help make the decision to tell people at work.</p>
            <section class="btn">
              <el-button type="primary" @click="toAnswer(3)">Answer Now<i class="el-icon-arrow-right el-icon--right"></i></el-button>
            </section>
          </div>
          <div class="tab_main tab_main_after" v-show="showModule===3">
            <h4>Slide the scale along to select what you value more at work if neither are important place the scale in the middle:</h4>
            <el-form label-position="top" :model="formData.module3">
              <el-form-item v-for="(value,key,index) in module3" :key="index">
                <div class="slider-label">
                  <div><p>{{module3[key]['1']}}</p></div>
                  <div><p>{{module3[key]['5']}}</p></div>
                </div>
                <el-slider v-model="formData.module3[key]" :show-tooltip="false" :min="1" :max="5" show-stops></el-slider>
              </el-form-item>
              <el-form-item>
                <el-checkbox label="others">Add my own values</el-checkbox>
                <el-input type="textarea" v-model="formData.module3.otherValues"></el-input>
              </el-form-item>
            </el-form>
            <section class="btn tab_main_btn">
              <div v-if="isMobile" class="btn_div">
                <div class="btn_tip">
                  Save before you leave if you won't continue.<i class="el-icon-thumb"></i>
                </div>
                <el-button type="primary" @click="toSave">Save</el-button>
              </div>
              <el-button type="primary" @click="toNext(3)">Next<i class="el-icon-arrow-right el-icon--right"></i></el-button>
            </section>
          </div>
        </section>
      </el-tab-pane>
      <el-tab-pane name="module4" :disabled="!finished[3]">
        <span slot="label"><i v-if="finished[4]" class="el-icon-success"></i>4.When is the best time to tell?</span>
        <section class="tab_content tab_content_4">
          <div class="tab_main tab_main_before" v-show="showModule!==4">
            <h3>When is the best time to tell?</h3>
            <p>It is important to think about if you should tell people at work about your mental health, it is also important to decide when the best time to tell people is.</p>
            <p>In this section you will be provided some advantages and obstacles about telling people at work at different time points.</p>
            <section class="btn">
              <el-button type="primary" @click="toAnswer(4)">Answer Now<i class="el-icon-arrow-right el-icon--right"></i></el-button>
            </section>
          </div>
          <div class="tab_main tab_main_after" v-show="showModule===4">
            <el-form label-position="top" :model="formData.module4">
              <el-form-item label="First, please select when you think is the best time to tell, select as many as you like:">
                <el-checkbox-group v-model="formData.module4.whenBefore">
                  <el-checkbox v-for="(value, key) in module4" :key="key" :label="key">{{value}}</el-checkbox>
                </el-checkbox-group>
              </el-form-item>
              <label class="el-form-item__label">Now, here are some advantages and disadvantages to each:</label>
              <el-table :data="module4Table" border style="width: 100%; margin: 20px 0">
                <el-table-column prop="when" label="When?" align="center"></el-table-column>
                <el-table-column label="Advantage" align="center">
                  <template slot-scope="scope">
                    <p v-for="(item, index) in scope.row.advantage" :key="index">
                      <i class="el-icon-position"></i><span>{{item}}</span>
                    </p>
                  </template>
                </el-table-column>
                <el-table-column label="Obstacle" align="center">
                  <template slot-scope="scope">
                    <p v-for="(item, index) in scope.row.obstacle" :key="index+100">
                      <i class="el-icon-position"></i><span>{{item}}</span>
                    </p>
                  </template>
                </el-table-column>
              </el-table>
              <el-form-item label="Now that you have been given some advantages and obstacles of each scenario, please select when you think is the best time to tell, select as many as you like:">
                <el-checkbox-group v-model="formData.module4.whenAfter">
                  <el-checkbox v-for="(value, key) in module4" :key="key" :label="key">{{value}}</el-checkbox>
                </el-checkbox-group>
              </el-form-item>
            </el-form>
            <section class="btn tab_main_btn">
              <div v-if="isMobile" class="btn_div">
                <div class="btn_tip">
                  Save before you leave if you won't continue.<i class="el-icon-thumb"></i>
                </div>
                <el-button type="primary" @click="toSave">Save</el-button>
              </div>
              <el-button type="primary" @click="toNext(4)">Next<i class="el-icon-arrow-right el-icon--right"></i></el-button>
            </section>
          </div>
        </section>
      </el-tab-pane>
      <el-tab-pane name="module5" :disabled="!finished[4]">
        <span slot="label"><i v-if="finished[5]" class="el-icon-success"></i>5.Who have you told in the past?</span>
        <section class="tab_content tab_content_5">
          <div class="tab_main tab_main_before" v-show="showModule!==5">
            <h4>Who have you told in the past?</h4>
            <p>Some people decide not to tell anyone, some decide to tell only their boss. Others may tell the whole office or certain trusted co-workers or teams.</p>
            <p>First, think about some times that you may have told a family member or a friend or even a previous employer or co-worker and how that experience was for you.</p>
            <section class="btn">
              <el-button type="primary" @click="toAnswer(5)">Answer Now<i class="el-icon-arrow-right el-icon--right"></i></el-button>
            </section>
          </div>
          <div class="tab_main tab_main_after" v-show="showModule===5">
            <el-form label-position="top" :model="formData.module5">
              <el-form-item label="Please select who you have told in your personal life in the past?">
                <el-checkbox-group v-model="formData.module5.personal">
                  <section v-for="(value, key) in module5.personal" :key="key">
                    <el-checkbox :label="key">{{value}}</el-checkbox>
                    <el-form-item  v-if="keyIsChecked(key,'personal')" class="dialog" label="The experience is:">
                      <el-radio-group v-model="formData.module5.perEffect[key]">
                        <el-radio :label="0">Positive</el-radio>
                        <el-radio :label="1">Negative</el-radio>
                      </el-radio-group>
                    </el-form-item>
                  </section>
                </el-checkbox-group>
              </el-form-item>
              <el-form-item label="Please select who you have told in your work place in the past?">
                <el-checkbox-group v-model="formData.module5.work">
                  <section v-for="(value, key) in module5.work" :key="key">
                    <el-checkbox :label="key">{{value}}</el-checkbox>
                    <el-form-item v-if="keyIsChecked(key,'work')" class="dialog" label="The experience is:">
                      <el-radio-group v-model="formData.module5.workEffect[key]">
                        <el-radio :label="0">Positive</el-radio>
                        <el-radio :label="1">Negative</el-radio>
                      </el-radio-group>
                    </el-form-item>
                  </section>
                </el-checkbox-group>
              </el-form-item>
            </el-form>
            <section class="btn tab_main_btn">
              <div v-if="isMobile" class="btn_div">
                <div class="btn_tip">
                  Save before you leave if you won't continue.<i class="el-icon-thumb"></i>
                </div>
                <el-button type="primary" @click="toSave">Save</el-button>
              </div>
              <el-button type="primary" @click="toNext(5)">Next<i class="el-icon-arrow-right el-icon--right"></i></el-button>
            </section>
          </div>
        </section>
      </el-tab-pane>
      <el-tab-pane name="module6" :disabled="!finished[5]">
        <span slot="label"><i v-if="finished[6]" class="el-icon-success"></i>6.Who should you tell?</span>
        <section class="tab_content tab_content_6">
          <div class="tab_main tab_main_before" v-show="showModule!==6">
            <h4>Who should you tell?</h4>
            <p>The next thing to think about is who to tell. Below is a table of some different ways to tell people at work. Please read the pros and cons and select which way would be best for you to decide who to tell and what the best way is for you.</p>
            <section class="btn">
              <el-button type="primary" @click="toAnswer(6)">Answer Now<i class="el-icon-arrow-right el-icon--right"></i></el-button>
            </section>
          </div>
          <div class="tab_main tab_main_after" v-show="showModule===6">
            <el-table :data="module6Table" border style="width: 100%; margin: 20px 0">
              <el-table-column label="Type" align="center">
                <template slot-scope="scope">
                  <span class="strong">{{scope.row.type.key}}</span>
                  {{scope.row.type.value}}
                </template>
              </el-table-column>
              <el-table-column label="Advantage" align="center">
                <template slot-scope="scope">
                  <p v-for="(item, index) in scope.row.advantage" :key="index">
                    <i class="el-icon-position"></i><span>{{item}}</span>
                  </p>
                </template>
              </el-table-column>
              <el-table-column label="Obstacle" align="center">
                <template slot-scope="scope">
                  <p v-for="(item, index) in scope.row.obstacle" :key="index+100">
                    <i class="el-icon-position"></i><span>{{item}}</span>
                  </p>
                </template>
              </el-table-column>
            </el-table>
            <el-form label-position="top" :model="formData.module6">
              <el-form-item label="After looking at the table, Please select which you think is the best way to tell?">
                <el-checkbox-group v-model="formData.module6.way">
                  <el-checkbox v-for="(value, key) in module6" :key="key" :label="key">{{value}}</el-checkbox>
                </el-checkbox-group>
              </el-form-item>
            </el-form>
            <section class="btn tab_main_btn">
              <div v-if="isMobile" class="btn_div">
                <div class="btn_tip">
                  Save before you leave if you won't continue.<i class="el-icon-thumb"></i>
                </div>
                <el-button type="primary" @click="toSave">Save</el-button>
              </div>
              <el-button type="primary" @click="toNext(6)">Next<i class="el-icon-arrow-right el-icon--right"></i></el-button>
            </section>
          </div>
        </section>
      </el-tab-pane>
      <el-tab-pane name="module7" :disabled="!finished[6]">
        <span slot="label"><i v-if="finished[7]" class="el-icon-success"></i>7.Making the decision</span>
        <section class="tab_content tab_content_7">
          <div class="tab_main tab_main_after" v-show="showModule!==7">
            <h4>Making the decision</h4>
            <p class="list_title">{{topics[0]}}</p>
            <div class="list_ctx">
              <p class="strong">Advantages:</p>
              <p v-for="(item, index) in formData.module1.advantages" :key="index">{{module1.choices[item]}}</p>
            </div>
            <div class="list_ctx">
              <p class="strong">Obstacles:</p>
              <p v-for="(item, index) in formData.module1.obstacles" :key="index">{{module1.choices[item]}}</p>
            </div>
            <div class="list_ctx" v-if="formData.module1.other">
              <p class="strong">Other:</p>
              <p>{{formData.module1.other}}</p>
            </div>
            <p class="list_title">{{topics[1]}}</p>
            <div class="list_ctx">
              <template v-for="(value, key) in module2" v-if="formData.module2[key] > 1">
                <p :key="key">{{value}}: <span class="strong">{{needInfo[formData.module2[key]]}}</span></p>
              </template>
              <p v-if="formData.module2.otherNeeds"><span class="strong">Ohters: </span>{{formData.module2.otherNeeds}}</p>
            </div>
            <p class="list_title">{{topics[2]}}</p>
            <div class="list_ctx">
              <p v-for="(value, key) in module3" :key="key" v-if="formData.module3[key] != 3">
                {{formData.module3[key] < 3 ? module3[key]['1'] : module3[key]['5']}}
              </p>
            </div>
            <p class="list_title">{{topics[3]}}</p>
            <div class="list_ctx">
              <p v-for="(item, index) in formData.module4.whenAfter" :key="index">{{module4[item]}}</p>
            </div>
            <p class="list_title">{{topics[4]}}</p>
            <div class="list_ctx">
              <p class="strong">In your personal life:</p>
              <p v-for="(item, index) in formData.module5.personal" :key="index">
                {{module5.personal[item]}}: <span class="strong">{{module5.dialog[formData.module5.perEffect[item]]}}</span>
              </p>
            </div>
            <div class="list_ctx">
              <p class="strong">In your work place:</p>
              <p v-for="(item, index) in formData.module5.work" :key="index">
                {{module5.work[item]}}: <span class="strong">{{module5.dialog[formData.module5.workEffect[item]]}}</span>
              </p>
            </div>
            <p class="list_title">{{topics[5]}}</p>
            <div class="list_ctx">
              <p v-for="(item, index) in formData.module6.way" :key="index">{{module6[item]}}</p>
            </div>
            <section class="btn">
              <el-button type="primary" @click="toNext(7)">Next<i class="el-icon-arrow-right el-icon--right"></i></el-button>
            </section>
          </div>
        </section>
      </el-tab-pane>
      <el-tab-pane name="module8" :disabled="!finished[7]">
        <span slot="label"><i v-if="finished[8]" class="el-icon-success"></i>After doing the modules</span>
        <section class="tab_content tab_content_9">
          <div class="tab_main tab_main_after">
            <h3>After doing the modules</h3>
            <p>Please answer a few short questions:</p>
            <el-form label-position="top" :model="formData.after">
              <el-form-item label="Did you find this tool useful?">
                <el-radio-group v-model="formData.after.useful">
                  <el-radio :label="0">No</el-radio>
                  <el-radio :label="1">Unsure</el-radio>
                  <el-radio :label="2">Yes</el-radio>
                </el-radio-group>
              </el-form-item>
              <el-form-item label="Would you recommend this tool to a co-worker?">
                <el-radio-group v-model="formData.after.recommend">
                  <el-radio :label="0">No</el-radio>
                  <el-radio :label="1">Unsure</el-radio>
                  <el-radio :label="2">Yes</el-radio>
                </el-radio-group>
              </el-form-item>
              <el-form-item label="Any other feedback you would like to provide?">
                <el-input type="textarea" v-model="formData.after.provide"></el-input>
              </el-form-item>
            </el-form>
            <section class="btn">
              <el-button type="primary" @click="toNext(8)">Next<i class="el-icon-arrow-right el-icon--right"></i></el-button>
            </section>
          </div>
         </section>
      </el-tab-pane>
      <el-tab-pane name="module9" :disabled="!finished[8]">
        <span slot="label"><i v-if="finished[9]" class="el-icon-success"></i>Finished</span>
        <section class="tab_content tab_content_8">
          <div class="tab_main tab_main_before">
            <h3>Thank you!</h3>
            <p>{{suggestion}}</p>
            <section class="btn">
              <el-button type="primary" @click="toSave">Submit</el-button>
            </section>
          </div>
         </section>
      </el-tab-pane>
    </el-tabs>
  </section>
</template>

<script>
import { moduleData } from '@/assets/js/data.js'
import { isMobile } from '@/assets/js/index.js'

export default {
  data () {
    return {
      userName: 'Anonymous',
      isMobile: isMobile,
      tabPos: 'left',
      showModule: 0,
      currentTab: 'module0',
      finished: [],
      ...moduleData,
      suggestion: "If you have any question, please click the 'Need Help?' button to contact us!",
      AdvNObs: {},
      formData: {
        before: {
          gender: '',
          age: ''
        },
        module1: {
          advantages: [],
          obstacles: [],
          other: ''
        },
        module2: {
          needs1: 0,
          needs2: 0,
          needs3: 0,
          needs4: 0,
          needs5: 0,
          needs6: 0,
          needs7: 0,
          needs8: 0,
          otherNeeds: ''
        },
        module3: {
          value1: 1,
          value2: 1,
          value3: 1,
          value4: 1,
          value5: 1,
          value6: 1,
          otherValues: ''
        },
        module4: {
          whenBefore: [],
          whenAfter: []
        },
        module5: {
          personal: [],
          perEffect: {
            0: '',
            1: '',
            2: '',
            3: '',
            4: ''
          },
          work: [],
          workEffect: {
            0: '',
            1: '',
            2: ''
          }
        },
        module6: {
          way: []
        },
        after: {
          useful: '',
          recommend: '',
          provide: ''
        }
      }
    }
  },
  created () {
    for (let i = 0; i < 10; i++) {
      this.finished[i] = false
    }
    if (this.isMobile) {
      this.tabPos = 'top'
    }
  },
  mounted () {
    let _this = this
    if (sessionStorage.getItem('user_email') !== null) {
      this.userName = sessionStorage.getItem('user_email')
      if (sessionStorage.getItem('continue') === 'true') {
        let data = new URLSearchParams()
        data.append('user_email', sessionStorage.getItem('user_email'))
        _this.$axios.post('/login/data/', data)
          .then(function (response) {
            let rd = response.data
            let before = rd.before_test.split(',')
            _this.formData.before.age = before[0]
            _this.formData.before.gender = before[1]
            if (rd.module1_advantages.length > 0) {
              _this.formData.module1.advantages = rd.module1_advantages.split(',')
            }
            if (rd.module1_obstacles.length > 0) {
              _this.formData.module1.obstacles = rd.module1_obstacles.split(',')
            }
            _this.formData.module1.other = rd.module1_extra
            let module2Selections = rd.module2_selections.split(',')
            _this.formData.module2.needs1 = parseInt(module2Selections[0])
            _this.formData.module2.needs2 = parseInt(module2Selections[1])
            _this.formData.module2.needs3 = parseInt(module2Selections[2])
            _this.formData.module2.needs4 = parseInt(module2Selections[3])
            _this.formData.module2.needs5 = parseInt(module2Selections[4])
            _this.formData.module2.needs6 = parseInt(module2Selections[5])
            _this.formData.module2.needs7 = parseInt(module2Selections[6])
            _this.formData.module2.needs8 = parseInt(module2Selections[7])
            _this.formData.module2.otherNeeds = rd.module2_extra_need
            let module3Selections = rd.module3_selections.split(',')
            _this.formData.module3.value1 = parseInt(module3Selections[0])
            _this.formData.module3.value2 = parseInt(module3Selections[1])
            _this.formData.module3.value3 = parseInt(module3Selections[2])
            _this.formData.module3.value4 = parseInt(module3Selections[3])
            _this.formData.module3.value5 = parseInt(module3Selections[4])
            _this.formData.module3.value6 = parseInt(module3Selections[5])
            _this.formData.module3.otherValues = rd.module3_extra_value
            if (rd.module4_selections_1.length > 0) { _this.formData.module4.whenBefore = rd.module4_selections_1.split(',') }
            if (rd.module4_selections_2.length > 0) { _this.formData.module4.whenAfter = rd.module4_selections_2.split(',') }
            if (rd.module5_personal_selections.length > 0) {
              _this.formData.module5.personal = rd.module5_personal_selections.split(',')
              for (let i = 0; i < 5; i++) {
                if (rd.module5_personal.split(',')[i] !== '') {
                  _this.formData.module5.perEffect[i.toString()] = parseInt(rd.module5_personal.split(',')[i])
                }
              }
            }
            if (rd.module5_work_selections.length > 0) {
              _this.formData.module5.work = rd.module5_work_selections.split(',')
              for (let i = 0; i < 3; i++) {
                if (rd.module5_work.split(',')[i] !== '') {
                  _this.formData.module5.workEffect[i.toString()] = parseInt(rd.module5_work.split(',')[i])
                }
              }
            }
          })
      }
    }
  },
  methods: {
    toAnswer (index) {
      this.showModule = index
    },
    toNext (index) {
      let _this = this
      let validation = true
      switch (index) {
        case 1:
          if (_this.formData.module1.advantages.length === 0 && _this.formData.module1.obstacles.length === 0) {
            validation = false
          }
          break
        case 4:
          if (_this.formData.module4.whenBefore.length === 0) {
            validation = false
          } else if (_this.formData.module4.whenAfter.length === 0) {
            validation = false
          }
          break
        case 5:
          if (_this.formData.module5.personal.length === 0 && _this.formData.module5.work.length === 0) {
            validation = false
          }
          break
        case 6:
          if (_this.formData.module6.way.length === 0) {
            validation = false
          }
          break
      }
      if (validation) {
        this.finished[index] = true
        this.currentTab = `module${index + 1}`
      } else {
        alert('Please select something before go to the next module!')
      }
    },
    checkChoice (key) {
      return this.formData.module1.advantages.includes(key) || this.formData.module1.obstacles.includes(key)
    },
    module1Change (value, key) {
      if (+value === 1) {
        this.formData.module1.advantages.push(key)
      } else {
        this.formData.module1.obstacles.push(key)
      }
    },
    deleteAdv (index) {
      let key = this.formData.module1.advantages[index]
      this.formData.module1.advantages.splice(index, 1)
      this.AdvNObs[key] = 0
    },
    deleteObs (index) {
      let key = this.formData.module1.obstacles[index]
      this.formData.module1.obstacles.splice(index, 1)
      this.AdvNObs[key] = 0
    },
    keyIsChecked (key, form) {
      return this.formData.module5[form].includes(key)
    },
    toSave () {
      // Rename data
      sessionStorage.setItem('current', this.showModule)
      sessionStorage.setItem('finished', this.finished)
      sessionStorage.setItem('before_test', this.formData.before.age + ',' + this.formData.before.gender)
      sessionStorage.setItem('module1_advantages', this.formData.module1.advantages)
      sessionStorage.setItem('module1_obstacles', this.formData.module1.obstacles)
      sessionStorage.setItem('module1_extra', this.formData.module1.other)
      sessionStorage.setItem('module2_selections', this.formData.module2.needs1.toString() + ',' +
        this.formData.module2.needs2.toString() + ',' + this.formData.module2.needs3.toString() + ',' +
        this.formData.module2.needs4.toString() + ',' + this.formData.module2.needs5.toString() + ',' +
        this.formData.module2.needs6.toString() + ',' + this.formData.module2.needs7.toString() + ',' +
        this.formData.module2.needs8.toString())
      sessionStorage.setItem('module2_extra_need', this.formData.module2.otherNeeds)
      sessionStorage.setItem('module3_selections', this.formData.module3.value1.toString() + ',' +
        this.formData.module3.value2.toString() + ',' + this.formData.module3.value3.toString() + ',' +
        this.formData.module3.value4.toString() + ',' + this.formData.module3.value5.toString() + ',' +
        this.formData.module3.value6.toString())
      sessionStorage.setItem('module3_extra_value', this.formData.module3.otherValues)
      sessionStorage.setItem('module4_selections_1', this.formData.module4.whenBefore)
      sessionStorage.setItem('module4_selections_2', this.formData.module4.whenAfter)
      sessionStorage.setItem('module5_personal', this.formData.module5.perEffect[0].toString() + ',' +
        this.formData.module5.perEffect[1].toString() + ',' + this.formData.module5.perEffect[2].toString() + ',' +
        this.formData.module5.perEffect[3].toString() + ',' + this.formData.module5.perEffect[4].toString())
      sessionStorage.setItem('module5_personal_selections', this.formData.module5.personal)
      sessionStorage.setItem('module5_work', this.formData.module5.workEffect[0] + ',' +
        this.formData.module5.workEffect[1] + ',' + this.formData.module5.workEffect[2])
      sessionStorage.setItem('module5_work_selections', this.formData.module5.work)
      sessionStorage.setItem('module6_selections', this.formData.module6.way)
      sessionStorage.setItem('after_test', this.formData.after.useful + ',' + this.formData.after.recommend + ',' +
        this.formData.after.provide)
      // Save
      let _this = this
      if (sessionStorage.getItem('user_email') !== null) {
        let data = new URLSearchParams()
        data.append('user_email', sessionStorage.getItem('user_email'))
        data.append('current', sessionStorage.getItem('current'))
        data.append('finished', sessionStorage.getItem('finished'))
        data.append('before_test', sessionStorage.getItem('before_test'))
        data.append('module1_advantages', sessionStorage.getItem('module1_advantages'))
        data.append('module1_obstacles', sessionStorage.getItem('module1_obstacles'))
        data.append('module1_extra', sessionStorage.getItem('module1_extra'))
        data.append('module2_selections', sessionStorage.getItem('module2_selections'))
        data.append('module2_extra_need', sessionStorage.getItem('module2_extra_need'))
        data.append('module3_selections', sessionStorage.getItem('module3_selections'))
        data.append('module3_extra_value', sessionStorage.getItem('module3_extra_value'))
        data.append('module4_selections_1', sessionStorage.getItem('module4_selections_1'))
        data.append('module4_selections_2', sessionStorage.getItem('module4_selections_2'))
        data.append('module5_personal', sessionStorage.getItem('module5_personal'))
        data.append('module5_work', sessionStorage.getItem('module5_work'))
        data.append('module5_personal_selections', sessionStorage.getItem('module5_personal_selections'))
        data.append('module5_work_selections', sessionStorage.getItem('module5_work_selections'))
        data.append('module6_selections', sessionStorage.getItem('module6_selections'))
        data.append('after_test', sessionStorage.getItem('after_test'))
        data.append('continue', sessionStorage.getItem('continue'))
        this.$axios.post('/login/save/', data)
          .then(function (response) {
            if (response.data.status === 0) {
              // logout
              sessionStorage.clear()
              alert('Submit Successfully!')
              _this.$router.push('/')
            } else {
              _this.$router.push('/login')
            }
          })
          .catch(function (error) {
            console.log(error)
          })
        _this.$router.push('/')
      }
    }
  }
}
</script>
<style scoped>
  .module {
    width: 100%;
    height: calc(100vh - 61px);
    position: fixed;
    margin-top: 61px;
  }
  .extra {
    position: absolute;
    width: 290px;
    left: 0;
    bottom: 20px;
    text-align: center;
    z-index: 9;
  }
  .extra .el-button {
    font-size: 20px;
  }
  .el-tabs {
    height: 100%;
  }
  .el-tabs /deep/ .el-tabs__header.is-left {
    width: 285px;
    margin-right: 0;
  }
  .el-icon-success, .el-icon-position {
    color: #e89c2c;
  }
  .tab_content {
    width: calc(100vw - 285px);
    height: calc(100vh - 61px);
    position: fixed;
    display: flex;
    background-repeat: no-repeat;
    background-size: 100% auto;
    background-position: bottom;
  }
  .tab_content_0 {
    background-image: url('../assets/img/before.jpg');
  }
  .tab_content_1 {
    background-image: url('../assets/img/module1.jpg');
  }
  .tab_content_2 {
    background-image: url('../assets/img/module2.jpg');
  }
  .tab_content_3 {
    background-image: url('../assets/img/module3.jpg');
  }
  .tab_content_4 {
    background-image: url('../assets/img/module4.jpg');
    background-size: 100% 100%;
  }
  .tab_content_5 {
    background-image: url('../assets/img/module5.jpg');
    background-position: top;
  }
  .tab_content_6 {
    background-image: url('../assets/img/module6.jpg');
  }
  .tab_content_7 {
    background-image: url('../assets/img/module7.jpg');
  }
  .tab_content_8 {
    background-image: url('../assets/img/after.jpg');
  }
  .tab_content_9 {
    background-image: url('../assets/img/thanks.jpg');
  }
  .tab_main {
    width: 100%;
    min-height: calc(100% - 61px);
    overflow-y: auto;
    background-color: rgba(0,0,0,0.7);
    font-size: 20px;
    color: #ffffff;
    padding: 30px;
  }
  .tab_main_before {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }

  .btn {
    margin: 20px auto;
    text-align: right;
  }
  .btn .btn_div {
    display: inline-block;
  }
  .btn_tip {
    display: inline-block;
    height: 50px;
    line-height: 50px;
    color: #e89c2c;
  }
  .list_title {
    margin: 40px 0 20px;
    font-weight: 600;
  }
  .list_ctx {
    margin: 20px 0;
  }
  .list_ctx p{
    font-size: 18px;
    margin: 10px 0;
  }
  .list_ctx .strong {
    color: #e89c2c;
  }
  @keyframes move {
    0%, 100% {
      margin-left: 10px;
      margin-right: 20px;
    }
    50% {
      margin-left: 20px;
      margin-right: 10px;
    }
  }
  .btn_tip .el-icon-thumb {
    color: #e89c2c;
    transform: rotate(90deg);
    -ms-transform: rotate(90deg);
    animation: move 1s ease infinite;
  }
  .btn .el-button{
    height: 50px;
    width: auto;
    font-size: 20px;
    margin: 10px;
  }
  .tab_main_after {
    text-align: left;
  }
  .el-form /deep/ .el-form-item__label {
    font-weight: 600;
    font-size: 18px;
  }
  .tab_content_5 .dialog {
    margin-left: 30px;
  }
  .el-form /deep/ .el-form-item.dialog .el-form-item__label {
    font-weight: 400;
    font-size: 14px;
    display: inline;
  }
  .el-form .el-checkbox {
    display: block;
  }
  .tab_main_after /deep/ .el-radio {
    display: block;
    margin: 20px 0;
  }
  .tab_main_after .dialog .el-radio, .dialog_label {
    display: inline;
    margin: 0 20px;
  }
  .tab_main_after /deep/ .el-form--label-top .el-form-item__label,
  .tab_main_after /deep/ .el-radio {
    color: #ffffff;
  }
  .tab_main_after /deep/ .el-checkbox__label {
    line-height: 22px;
    color: #ffffff;
    display: inline-grid;
    white-space: pre-line;
    overflow: hidden;
    word-break: break-word;
  }
  .module /deep/ .el-slider__stop {
    top: 50%;
    width: 10px;
    height: 10px;
    transform: translate(-50%,-50%);
  }
  .tab_content:not(.tab_content_2):not(.tab_content_3) .el-slider {
    margin-top: 20px;
  }
  .tab_content_3 .el-slider {
    margin-bottom: 20px;
  }
  .tab_content_2 .el-form-item {
    margin-top: 20px;
    float: left;
    width: 100%;
  }
  .slider-label {
    display: flex;
    justify-content: space-between;
  }
  .slider-label div {
    display: flex;
    align-items: flex-end;
    width: 25%;
    height: auto;
    line-height: 20px;
    margin: 0;
  }
  .slider-label div:last-child{
    text-align: right;
  }
  .slider-label div p{
    display: inline-block;
    width: 100%;
    margin: 0;
  }
  .module /deep/ .el-slider__marks-text:first-child {
    transform: translate(0px);
  }
  .module /deep/ .el-slider__marks-text:last-child {
    left: 85% !important;
    width: 35%;
    right: 0;
    text-align: right;
  }
  .tab_main_before /deep/ .el-slider__marks-text {
    font-size: 20px;
  }
  .el-table p {
    margin: 10px 0;
  }
  .el-table p span {
    padding-left: 10px;
  }
  .strong {
    font-weight: 600;
  }
  @media screen and (max-width: 1125px) {
    .tab_content_0, .tab_content_2, .tab_content_3, .tab_content_6, .tab_content_8 {
      background-size: auto 100%;
    }
  }
  @media screen and (max-width: 800px) {
    .login {
      display: none;
    }
    .el-tabs /deep/ .el-tabs__header.is-top {
      margin-bottom: 0;
    }
    .el-tabs /deep/ .el-tabs__nav-scroll {
      overflow: auto;
    }
    .tab_content {
      width: 100%;
      height: calc(100vh - 141px);
      padding-bottom: 40px;
      background-size: auto 100%;
    }
     .tab_main {
      min-height: calc(100vh - 221px);
      width: calc(100% - 40px);
      padding: 40px 20px 80px;
    }
    .tab_main_before p {
      text-align: left;
    }
    .tab_main_before /deep/ .el-slider__marks-text {
      font-size: 16px;
    }
    .btn_tip {
      width: 60%;
      font-size: 14px;
      line-height: 1;
    }
  }
  .tab_content_0 /deep/ .el-input{
      width: 350px;
    }
  .el-table /deep/ .cell{
    word-wrap: break-word;
    word-break: normal;
  }
</style>
