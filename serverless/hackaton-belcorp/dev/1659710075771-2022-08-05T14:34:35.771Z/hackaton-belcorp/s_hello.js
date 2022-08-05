
var serverlessSDK = require('./serverless_sdk/index.js');
serverlessSDK = new serverlessSDK({
  orgId: 'atorresl',
  applicationName: 'hackaton-belcorp',
  appUid: 'xBGNCPsH6dfGQZCVKX',
  orgUid: 'bfe6877c-1278-4c22-8a87-92378a6c9aa5',
  deploymentUid: '8f1ab3c7-c0cc-4867-880e-0b139dc1db5d',
  serviceName: 'hackaton-belcorp',
  shouldLogMeta: true,
  shouldCompressLogs: true,
  disableAwsSpans: false,
  disableHttpSpans: false,
  stageName: 'dev',
  serverlessPlatformStage: 'prod',
  devModeEnabled: false,
  accessKey: null,
  pluginVersion: '6.2.2',
  disableFrameworksInstrumentation: false
});

const handlerWrapperArgs = { functionName: 'hackaton-belcorp-dev-hello', timeout: 6 };

try {
  const userHandler = require('./handler.js');
  module.exports.handler = serverlessSDK.handler(userHandler.hello, handlerWrapperArgs);
} catch (error) {
  module.exports.handler = serverlessSDK.handler(() => { throw error }, handlerWrapperArgs);
}