export const indexData = {
  title: `Should you tell people at work about your Mental Health Condition?`,
  context: [
    `There is no right or wrong answer when it comes to telling people about your mental health. Each decision is different, and it is important that you think carefully about your options and the affect that it may have on your work and home life.`,
    `This is a tool that will help inform you about the decision to tell people in your workplace about your mental health condition and help you decide what the best outcome will be for you.`,
    `At the end you will get a summary of your answers. That may be helpful in making your decision to tell people at work or not.`
  ]
}

export const loginData = [
  `Welcome to READY? The decision aid tool.`,
  `You have two options,`,
  `1) if you would like to register so that you can sign back in and use the tool as many times as you need please register. Our team will not contact you unless you provide permission after you use the tool.`,
  `2) if you would just like to use the tool without signing up, please select anonymously continue.`
]

export const moduleData = {
  topics: [
    `1.Advantages and obstacles of telling`,
    `2.'Needs' at work`,
    `3.'Values' at work`,
    `4.When is the best time to tell?`,
    `5.Who have I told in the past?`,
    `6.Who should you tell?`
  ],
  confusion: {
    0: `little confused`,
    4: `very confused`
  },
  module1: {
    choices: {
      0: `We can talk about options to my working hours.`,
      1: `They will be more understanding if I need to have time off to see my doctor / health professionals.`,
      2: `I will feel relief as I don't have to hide my struggles from co-workers.`,
      3: `I may be helping others to be honest about their mental health.`,
      4: `People in my workplace may be more understanding if I am not keeping on top of my work.`,
      5: `It may be helpful for future performance reviews.`,
      6: `I don't have to worry about being talked about behind my back when I'm having trouble.`,
      8: `I am worried that I won't be able to keep my job.`,
      9: `I am worried that I won't get a promotion or have to work twice as hard to prove myself.`,
      10: `I am worried that it won't be confidential.`,
      11: `My boss may not trust me with important jobs.`,
      12: `I am worried my boss might think I will claim for workers compensation.`,
      13: `I am worried if I have a bad day work co-workers may think it is because of my mental health.`,
      14: `I am worried about stigma or discrimination.`
    }
  },
  module2: {
    needs1: `to make changes to my hours because of my mental health condition`,
    needs2: `to have more flexible hours so I can attend health care appointments`,
    needs3: `to make changes to my current role as I feel like I can't do certain jobs`,
    needs4: `to make changes to my role so I can do certain parts of my job properly`,
    needs5: `to have a plan at work in case I suddenly become ill`,
    needs6: `to teach someone my role so that I do not feel guilty or stressed if I need to take time off work`,
    needs7: `to meet with my boss more often to make sure that I am doing my job right`,
    needs8: `I need to have some time-outs during the day when I'm not feeling so good`
  },
  needInfo: {
    0: `Unimportant`,
    1: `Of Little Importance`,
    2: `Moderately Important`,
    3: `Important`,
    4: `Very Important`
  },
  needRadio: {
    0: `Unimportant`,
    2: `Moderately Important`,
    4: `Very Important`
  },
  module3: {
    value1: {
      1: `being open and honest`,
      5: `keeping private`
    },
    value2:  {
      1: `being treated the same`,
      5: `support and flexibility`
    },
    value3:  {
      1: `positive attitudes`,
      5: `openness, even if they have negative attitudes`
    },
    value4:  {
      1: `teaching others about mental health`,
      5: `teaching others is not important to me`
    },
    value5:  {
      1: `not being pitied or people feeling sorry for me`,
      5: `Empathy about my mental health condition`
    },
    value6:  {
      1: `being myself at work even if that means people disapprove`,
      5: `approval even if that means I can't be myself at work`
    }
  },
  module4:{
    when1: `in a on-on-one  meeting`,
    when2: `in a chat at work, in the pub or social event`,
    when3: `in my review`,
    when4: `after I have a good bond with my boss or co-workers`,
    when5: `never`
  },
  module4Table: [{
    when: `In a one-on-one meeting`,
    advantage: [
      `Honesty / piece of mind`,
      `Gives you a chance to talk about it in a formal setting`,
      `Gives you a chance to respond in person to any issues or questions`,
      `They may not be negative while you are there in person`
    ],
    obstacle: [
      `Puts pressure on you to answer some hard questions about your mental health`,
      `They may look at your mental illness as more of a problem `
    ]
  }, {
    when: `In a chat at work, at the pub, or a social event`,
    advantage: [
      `Honesty / piece of mind`,
      `Give you a chance to respond in person to any issues or questions`,
      `They may not be negative while you are there in person`,
      `You can keep a casual approach your mental health condition, which may help your boss to feel more positive going forward`
    ],
    obstacle: [
      `Employer might lose trust in you and believe you should have told them earlier`,
      `May harm the working relationship`,
      `All questions may not be asked / answered as your boss may not have enough time to think about the situation`,
      `Chat may not be confidential`
    ]
  }, {
    when: `In my review`,
    advantage: [
      `Gives you a chance to learn the role and meet everyone first`,
      `Give you an chance to discuss your condition in a formal setting in a one on one situation`
    ],
    obstacle: [
      `Your employer could say you gave a false application or not telling earlier and waiting for a formal review`
    ]
  }, {
    when: `After I have a good bond with my boss or co-workers`,
    advantage: [
      `People will get to know you as a person and see parts of your personality`,
      `You may build relationships and trust`,
      `You get to know your employer and co-workers and see if they will judge you`,
      `Gives you a chance to learn the role and meet everyone first`
    ],
    obstacle: [
      `being nervous or fearful of having an episode or accident on the job`,
      `Could change interaction with co-workers`
    ]
  }, {
    when: `Never`,
    advantage: [
      `You don't have to be concerned about being treated differently or judged in your workplace`
    ],
    obstacle: [
      `Stress of having an episode and no one will know how to react`
    ]
  }],
  module5:{
    personal: {
      0: `A spouse`,
      1: `A parent`,
      2: `Another family member`,
      3: `A friend or a group of friends`,
      4: `No one`
    },
    work: {
      0: `A co-worker`,
      1: `Your boss`,
      2: `No one`
    },
    dialog: {
      0: `Positive`,
      1: `Negative`
    }
  },
  module6Table: [{
    type: {
      key: `Keep it a secret:`,
      value: `Don't tell anyone at work about your mental health`
    },
    advantage: [
      `Nobody can use this information to hurt you`,
      `You are treated the same as everybody else`
    ],
    obstacle: [
      `You may feel anxious or guilty about keeping a secret`,
      `You won't get help or be able to make changes that you need`,
      `You may lose your job if it comes out later`
    ]
  }, {
    type: {
      key: `Only tell trusted people:`,
      value:`Tell some people who you believe will be supportive about your mental health`
    },
    advantage: [
      `You find a small group of people who will understand your problems and give you support`,
      `You can get help and make changes needed in your role`
    ],
    obstacle: [
      `You may tell some people that don't react well or who may hurt you later with the information`,
      `You may have a hard time keeping track of who you have told and who you haven't`
    ]
  }, {
    type: {
      key: `Tell anyone:`,
      value:`Aren't concerned about who knows about your mental illness. Happy to tell anyone you encounter`
    },
    advantage: [
      `You won't worry about who knows about your mental health condition`,
      `You are likely to find some people that will help you and provide support`
    ],
    obstacle: [
      `You may tell some people that don't react well or who may hurt you later with the information`
    ]
  }, {
    type: {
      key: `Tell everyone:`,
      value:`Tell others about your experiences or make an announcement to a group or the whole office`
    },
    advantage: [
      `You won't worry about who knows about your mental health condition`,
      `You may feel empowered`,
      `You may help other to tell about their situation`,
      `You are helping to combat stigma and negative attitudes`
    ],
    obstacle: [
      `You may come across people who react badly or try to hurt you with the information`,
      `You may find that you are often called upon to give your opinion on mental health  and this might create further stress`
    ]
  }],
  module6: {
    0: `Keep it a secret`,
    1: `Only tell trusted people`,
    2: `Tell anyone`,
    3: `Tell everyon`,
    4: `Tell no-one`
  }
}

export const helpData = {
  title: `We would like to provide you with some resources should you ever have concerns about your mental health.`,
  context: [{
    title: `Here are some phone lines if you need to get help, get a referral or just talk to someone:`,
    items: [{
      title: `Lifeline 13 11 14:`,
      context: `counselling, professional support and local referrals (24 hours)`
    }, {
      title: `Beyondblue 1300 22 4636:`,
      context: `mental health info line`
    }, {
      title: `Salvo Care Line NSW 1300 36 36 22:`,
      context: `volunteers providing support and referral in crisis`
    }, {
      title: `NSW Health Mental Health Information Line on 1800 794 991:`,
      context: `for referral to local services including professionals and self help and support groups`
    }, {
      title: `SANE Australia Helpline 1800 817 263:`,
      context: `An information and referral service (Monday to Friday 9am to 5pm)`
    }]
  }, {
    title: `You can ask your GP to make an appointment with a mental health professional, or find a psychologist in your local area:`,
    items: [{
      context: `The 'Find a Psychologist' page on the Australian Psychological Society (APS) website allows you to search for a private psychologist in your area: http://www.psychology.org.au/FindaPsychologist. Note this does not need a GP referral.`
    }]
  }, {
    title: `Another option is to get support online:`,
    items: [{
      title: `SANE Australia,`,
      context: `http://www.sane.org. Factsheets and other information about a range of mental health issues.`
    }, {
      title: `Beyondblue,`,
      context: `http://www.beyondblue.org.au. Information about a range of mental health issues.`
    }]
  }]
}
