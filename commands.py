from cmd import Cmd


class MyPrompt(Cmd):
    prompt = 'zammad> '
    intro = "Hallo! Schreiben Sie bitte 'help' um Befehle zu listen"


    def do_exit(self, inp):
        print("Aufwiedersehen!")
        return True

    def do_ruby_on_rails(self, inp2):
        print("Ein grosser Teil der Befehle von Ruby on Rails wird hier zusammengefasst.")
        print("Weitere Informationen finden Sie in der Technischen Dokumentation unten:")
        print("Unterabschnitt 3.2.1 und Abschnitt 6\n")
        print("Um auf die Befehle zuzugreifen, fuehren Sie den folgenden Befehl auf diesem Terminal aus:")
        print("help ruby_on_rails\n")

    def help_ruby_on_rails(self):
        print("\n")

        print("-> Zugang zu Zammad")
        print("$ sudo zammad run rails c")
        print("\n")

        print("-Waehlen Sie bitte ein Objekttyp!-\n")

        print(" --------------------------------------")
        print(" |             TICKET: 1              |")
        print(" --------------------------------------")
        print(" --------------------------------------")
        print(" |              USER: 2               |")
        print(" --------------------------------------")
        print(" --------------------------------------")
        print(" |          ORGANISATION: 3           |")
        print(" --------------------------------------")
        print(" --------------------------------------")
        print(" |              GROUP: 4              |")
        print(" --------------------------------------")
        print("\n")
        thema_choice=int(input("Eingeben = "))
        print("***************************************\n")

        # TICKET
        if thema_choice == 1:
            print("Waehlen Sie bitte eine Option \n")
            print("---------------------------------------")
            print("-> Ticket/s suchen: 1")
            print("---------------------------------------")
            print("-> Ticket/s loeschen: 2")
            print("---------------------------------------")
            print("-> Infos ueber Ticket/s: 3")
            print("---------------------------------------")
            print("-> Ticket erstellen: 4")
            print("---------------------------------------")
            print("-> Ticket updaten: 5")
            print("---------------------------------------")
            print("\n")
            ticket_suboption_choice=int(input("Eingeben = "))
            print("***************************************\n")

            # Ticket/s suchen
            if ticket_suboption_choice == 1:
                print(">> Ticket.find(id)")
                print(">> Ticket.find_by(number: 'ticket.number')")
                print(">> Ticket.where(title: 'ticket.title')")
                print(">> Ticket.where(number: 'ticket_number')")
                print(">> Ticket.where(state_id: ticket.state_id)")
                print(">> Ticket.where(organisation_id: ticket.organisation.id)")
                print(">> Ticket.where(customer_id: ticket.customer_id)")
                print(">> Ticket.where(ip_adresse: ticket.ip_adresse)")

            # Tickets/s loeschen
            elif ticket_suboption_choice == 2:
                print(">> Ticket.find(id).destroy")
                print(">> Ticket.where(state_id: ticket.state_id).destroy_all")
                print(">> Ticket.find_by(number: 'ticket.number').destroy\n")
                print(">> tickets_to_delete = [500..600].to_a")
                print(">> Ticket.where(id: tickets_to_delete).destroy_all\n")

            # Infos ueber Tickets
            elif ticket_suboption_choice == 3:
                print(">> Ticket.find(id).customer_id")
                print(">> Ticket.find_by(title: ticket.title).owner.email\n")
                print(">> Ticket.find_by(title: ticket.title).customer_id")
                print(">> User.find(customer_id)\n")
                print(">> Ticket.where(id: ticket.id).pluck(:created_by_id, :created_at)")
                print(">> User.find(created_by_id)\n")
                print(">> Ticket.find(id).close_at")
                print(">> Ticket.where(id: ticket.id).pluck(:rueckrufnummer, :pc_name, :mac_adresse)")
                print(">> Ticket.find(id).last_contact_at")
                print(">> Ticket.find(id).first_response_diff_in_min")
                print(">> Ticket.find(id).state.name")
                print(">> Ticket.find(id).customer.email")

            # Ticket erstellen
            elif ticket_suboption_choice == 4:
                print(">> Ticket.create!(customer_id: ticket.customer.id, group_id: ticket.group_id, title: ticket.title, created_by_id: ticket.created_by_id, updated_by_id: ticket.created_by_id, rueckruf_nummer: ticket.rueckruf_nummer, pc_name: ticket.pc_name)")

            # Ticket updaten
            elif ticket_suboption_choice == 5:
                print(">> t = Ticket.find(id)")
                print(">> t.title = neue_titel")
                print(">> t.save!\n")
                print(">> t = Ticket.find(id)")
                print(">> t.customer_id = customer_id_neu")
                print(">> t.save!\n")
                print(">> Ticket.where(customer_id: ticket.customer_id).update_all(owner_id: owner_id_neu)")

            else:
                pass

        # USER
        if thema_choice == 2:
            print("Waehlen Sie bitte eine Option \n")
            print("---------------------------------------")
            print("-> User suchen: 1")
            print("---------------------------------------")
            print("-> User (customer) loeschen: 2")
            print("---------------------------------------")
            print("-> Infos ueber User 3")
            print("---------------------------------------")
            print("-> User erstellen: 4")
            print("---------------------------------------")
            print("-> User updaten: 5")
            print("---------------------------------------")
            print("-> User Passwort zuruecksetzen: 6")
            print("---------------------------------------")
            print("-> User Zugangsdaten freischalten: 7 \n")
            user_suboption_choice=int(input("Eingeben = "))
            print("***************************************\n")

            # User suchen
            if user_suboption_choice == 1:
                print(">> User.find(id)")
                print("User.find_by(email: user.email)")

            # User (customer) loeschen
            elif user_suboption_choice == 2:
                print("* Erste Schritt")
                print("---------------------------------------")
                print(">> customer_emails = %w[customer@example.com customer@example.org")
                print("customers = User.joins(roles: :permissions).where(email: customer_emails, roles: { active: true }, permissions: { name: 'ticket.customer', active: true }).where.not(id: 1)\n")
                print("* Zweite Schritt")
                print("---------------------------------------")
                print("puts customers.map { |user| <<~PREVIEW }.join(\ n)")
                print("  Customer #{user.fullname}/#{user.id}/#{user.email} hat #{Ticket.where(customer_id: user.id).count} tickets #{Ticket.where(customer_id: user.id).pluck(:number)}")
                print(">> customers.find_each do |user|")
                print("   puts %{Loeschung des Kunden vorbereiten '#{user.fullname}' (und #{Ticket.where(customer_id: user.id).count} zugehoerigen Tickets}")
                print("   Ticket.where(customer: user).find_each do |ticket|")
                print("   ticket.destroy")
                print("end\n")
                print("* Dritte Schritt")
                print("---------------------------------------")
                print("puts 'Referenzen-Entfernung von #{user.email}...' ")
                print("ActivityStream.where(created_by_id: user.id).update_all(created_by_id: 1)")
                print("History.where(created_by_id: user.id).update_all(created_by_id: 1)")
                print("Ticket::Article.where(created_by_id: user.id).update_all(created_by_id: 1)")
                print("Ticket::Article.where(updated_by_id: user.id).update_all(updated_by_id: 1)")
                print("Store.where(created_by_id: user.id).update_all(created_by_id: 1)")
                print("StatsStore.where(created_by_id: user.id).update_all(created_by_id: 1)")
                print("Tag.where(created_by_id: user.id).update_all(created_by_id: 1)")
                print("OnlineNotification.find_by(user_id: user.id)&.destroy!")
                print("puts '  Entfernung von #{user.fullname}...' ")
                print("user.destroy")
                print("end")

            # Infos ueber User
            elif user_suboption_choice == 3:

                print(">> User.find(id).roles.pluck(:name)")
                print(">> User.find(id).login")
                print(">> User.find_by(email: user.email).out_of_office")
                print(">> User.find_by(email: user.email).out_of_office_start")
                print(">> User.find_by(email: user.email).out_of_office_end")
                print(">> User.find(id).pluck(:firstname, :lastname, :address)\n")
                print(">> User.find(id).organisation.name")
                print(">> User.where(email: user.email).pluck(:tickets_closed, :tickets_open")

            # User erstellen
            elif user_suboption_choice == 4:
                print("User.create!(created_by_id: user.id, updated_by_id: user_id, firstname: user.name, lastname: user.lastname, email: user.lastname)")

            # User erstellen
            elif user_suboption_choice == 5:
                print(">> User.find(id).update(email: neu_user.email)\n")
                print(">> u = User.find(id)")
                print(">> u.email = neu_user.email")
                print(">> u.firstname = neu_user.firstname")
                print(">> u.lastname = neu_user.lastname")
                print(">> u.phone = neu_user.phone")
                print(">> u.save!")

            elif user_suboption_choice == 6:
                print("User.find_by(email: user.email).update!(password: 'new_password' ")
            # User Zugangsdaten freischalten
            elif user_suboption_choice == 7:
                print(">> u = user.find(id)")
                print(">> u.login_failed = 0")
                print(">> u.save!")

            else:
                pass

        # ORGANISATION
        if thema_choice==3:
            print("---------------------------------------")
            print("-> Organisation/s suchen: 1")
            print("---------------------------------------")
            print("-> Organisation erstellen: 2")
            print("---------------------------------------")
            print("-> Organisation loschen: 3")
            print("---------------------------------------")
            print("-> Organisation updaten: 4\n")
            organization_suboption_choice=int(input("Eingeben = "))
            print("***************************************\n")

            # Organisation suchen
            if organization_suboption_choice == 1:
                print(">> Organization.find(id)")
                print(">> Organization.where(active: boolean)")
                print(">> Organisation.find_by(name: 'organization.name')")

            # Organisation erstellen
            elif organization_suboption_choice == 2:
                print(">> Organisation.create!(name: organisation.name, created_by_id: user_id, active: boolean)")

            # Organisation loeschen
            elif organization_suboption_choice == 3:
                print("* Erste Schritt")
                print("---------------------------------------")
                print(">> organizations = Organization.where(name: organisation.name)\n")
                print("* Zweite Schritt")
                print("---------------------------------------")
                print(">> puts organizations.map { |org| 'ORGANIZATION #{org.name}'' }.join('\ n')\n")
                print("* Dritte Schritt")
                print("---------------------------------------")
                print(">> organizations.each do |org|")
                print("puts %{Vorbereitung der Loeschung der Organisation '#{org.name}'...}")
                print("org.members.each do |member|")
                print("puts '  Removing #{member.fullname} from organization...' ")
                print("member.update!(organization_id: nil)")
                print("end")
                print(" puts '  Loeschung #{org.name}...' ")
                print("org.destroy")
                print("end")

            # Organisation updaten
            elif organization_suboption_choice == 4:
                print(">> Organisation.find(id).update(active: boolean)")
                print(">> org = Organisation.find_by(name: organisation.name).update(name: neu_organisation.name)")

            else:
                pass

        # GROUP
        elif thema_choice == 4:
            print("---------------------------------------")
            print("-> Group suchen: 1")
            print("---------------------------------------")
            print("-> Group erstellen: 2")
            print("---------------------------------------")
            print("-> Group aktualisieren: 3")
            print("---------------------------------------")
            print("-> Group deaktivieren: 4")
            print("---------------------------------------")
            print("\n")
            group_suboption_choice=int(input("Eingeben = "))
            print("***************************************\n")

            # Group suchen
            if group_suboption_choice == 1:
                print("Group.find_by(name: group.name)")

            # Group erstellen
            elif group_suboption_choice == 2:
                print("Group.create!(created_by_id: user.id, updated_by_id: user.id, name: group.name, active: boolean)")

            elif group_suboption_choice == 3:
                print("Group.update!(name: 'new_name')")

            # Group deaktivieren
            elif group_suboption_choice == 4:
                print("Group.update!(name: false)")

            else:
                pass


    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)

if __name__ == '__main__':
    MyPrompt().cmdloop()
