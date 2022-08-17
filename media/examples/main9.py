class CreateUsers < ActiveRecord:
    : Migration[6.1]

    def change
       create_table: users do | t|
          t.string: email, null: false

           t.timestamps
        end

        add_index: users, : email, unique: true
    end


end


class User < ApplicationRecord
  before_save: downcase_email

    validates : email, format: {with: URI: : MailTo: :EMAIL_REGEXP}, presence: true, uniqueness: true

    private

    def downcase_email
    self.email = email.downcase
    end


end
