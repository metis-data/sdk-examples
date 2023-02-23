import { Injectable, Inject } from '@nestjs/common';
import { CreateArticleDto } from './dto/create-article.dto';
import { UpdateArticleDto } from './dto/update-article.dto';
import { PG_CONNECTION } from '../pg/pg.consts';
import { Pool } from 'pg';

@Injectable()
export class ArticlesService {
  constructor(@Inject(PG_CONNECTION) private pg: Pool) {}

  async create(createArticleDto: CreateArticleDto) {
    return this.pg.query(
`INSERT INTO article (title, description, body, published) 
                 VALUES (
                   '${createArticleDto.title}', 
                   ${createArticleDto.description ? `'${createArticleDto.description}'` : null}, 
                   '${createArticleDto.body}', 
                   ${createArticleDto.published}
                 )`
    );
  }

  async findDrafts() {
    const res = await this.pg.query('SELECT * FROM article WHERE published = false');
    return res.rows;
  }

  async findAll() {
    const res = await this.pg.query('SELECT * FROM article');
    return res.rows;
  }

  async findOne(id: number) {
    const res = await this.pg.query(`SELECT * FROM article WHERE id = ${id}`);
    return res.rows;
  }

  async update(id: number, updateArticleDto: UpdateArticleDto) {
    const stmts = Object.entries(updateArticleDto).map(([k, v]) => `${k} = '${v}'`);
    if (updateArticleDto.published !== undefined) stmts['published'] = updateArticleDto.published;
    if (updateArticleDto.description === null) stmts['description'] = null;
    return this.pg.query(`UPDATE article SET ${stmts.join(',')} WHERE id = ${id}`);
  }

  async remove(id: number) {
    return this.pg.query(`DELETE FROM article WHERE id = ${id}`)
  }
}
