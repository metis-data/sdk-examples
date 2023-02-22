import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ArticlesModule } from './articles/articles.module';
import { PgModule } from './pg/pg.module';

@Module({
  imports: [ArticlesModule, PgModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
