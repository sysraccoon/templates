import { logStackTrace } from "./utils/stacktrace.js"

Java.perform(() => {
    logStackTrace();
});
