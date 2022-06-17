move_ids = self.env['account.move'].search([('state', '=', 'draft')])
for index, move_id in enumerate(move_ids):
    move_id.action_post()
    if index % 50 == 0:
        self.env.cr.commit()
self.env.cr.commit()
