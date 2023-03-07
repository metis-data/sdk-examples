import opentelemetry from '@opentelemetry/api';
import { registerInstrumentations } from '@opentelemetry/instrumentation';
import { Resource } from '@opentelemetry/resources';
import {
  BasicTracerProvider,
  BatchSpanProcessor,
  ConsoleSpanExporter,
  SimpleSpanProcessor,
} from '@opentelemetry/sdk-trace-base';
import { SemanticResourceAttributes } from '@opentelemetry/semantic-conventions';
import { AsyncHooksContextManager } from '@opentelemetry/context-async-hooks';
import { getPrismaInstrumentation, getMetisExporter, MetisHttpInstrumentation } from '@metis-data/prisma-interceptor';

export const startMetisInstrumentation = () => {
  const tracerProvider = new BasicTracerProvider({
    resource: new Resource({
      [SemanticResourceAttributes.SERVICE_NAME]: process.env.METIS_SERVICE_NAME,
      [SemanticResourceAttributes.SERVICE_VERSION]: process.env.METIS_SERVICE_VERSION,
    }),
  });

  const metisExporter = getMetisExporter(process.env.METIS_API_KEY);

  tracerProvider.addSpanProcessor(new BatchSpanProcessor(metisExporter));

  if (process.env.OTEL_DEBUG) {
    tracerProvider.addSpanProcessor(new SimpleSpanProcessor(new ConsoleSpanExporter()));
  }

  const contextManager = new AsyncHooksContextManager().enable();
  opentelemetry.context.setGlobalContextManager(contextManager);

  tracerProvider.register();

  const excludeUrls = [/favicon.ico/];
  registerInstrumentations({
    instrumentations: [new MetisHttpInstrumentation(excludeUrls), getPrismaInstrumentation()],
  });
};
