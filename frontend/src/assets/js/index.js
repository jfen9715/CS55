function checkAgent() {
  let agent = navigator.userAgent;
  if(/Mobile|Android|webOS|iPhone|iPad|Phone/i.test(agent)) {
    console.log('is mobile, true')
    return true;
  } else {
    console.log('is mobile, false')
    return false;
  }
}
export const isMobile = checkAgent();
