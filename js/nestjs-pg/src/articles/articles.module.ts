import { Module } from '@nestjs/common';
import { ArticlesService } from './articles.service';
import { ArticlesController } from './articles.controller';
import { PgModule } from '../pg/pg.module';

@Module({
  controllers: [ArticlesController],
  providers: [ArticlesService],
  imports: [PgModule],
})
export class ArticlesModule {}
