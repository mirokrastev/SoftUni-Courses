function solve() {
    class Figure {
        constructor(unit='cm') {
            this.unit = unit;
        }

        changeUnits(unit) {
            this.unit = unit;
        }
    }

    class Circle extends Figure {
        constructor(radius, unit='cm') {
            super(unit);
            this.radius = radius;
            this.changeUnits(unit=this.unit,'cm');
        }

        changeUnits(unit, toConvertFrom=this.unit) {
            this.radius = (() => ({
                'cm': {
                    'mm': this.radius * 10,
                    'cm': this.radius * 1,
                    'm': this.radius / 100
                },
                'mm': {
                    'mm': this.radius * 1,
                    'cm': this.radius / 10,
                    'm': this.radius / 1000
                },
                'm': {
                    'mm': this.radius * 1000,
                    'cm': this.radius * 100,
                    'm': this.radius * 1
                }
            }))()[toConvertFrom][unit];
            super.changeUnits(unit);
        }

        get area() {
            return Math.PI * this.radius * this.radius;
        }

        toString() {
            return `Figures units: ${this.unit} Area: ${this.area} - radius: ${this.radius}`;
        }
    }

    class Rectangle extends Figure {
        constructor(width, height, unit='cm') {
            super(unit);
            this.width = width;
            this.height = height;
            this.changeUnits(this.unit, 'cm');
        }

        changeUnits(unit, toConvertFrom=this.unit) {
            [this.width, this.height] = ({
                'cm': {
                    'mm': [this.width * 10, this.height * 10],
                    'cm': [this.width * 1, this.height * 1],
                    'm': [this.width / 100, this.height / 100]
                },
                'mm': {
                    'mm': [this.width * 1, this.height * 1],
                    'cm': [this.width / 10, this.height / 10],
                    'm': [this.width / 1000, this.height / 1000]
                },
                'm': {
                    'mm': [this.width * 1000, this.height * 1000],
                    'cm': [this.width * 100, this.height * 100],
                    'm': [this.width * 1, this.height * 1]
                }
            })[toConvertFrom][unit];
            super.changeUnits(unit);
        }

        get area() {
            return this.width * this.height;
        }

        toString() {
            return `Figures units: ${this.unit} Area: ${this.area} - width: ${this.width}, height: ${this.height}`;
        }
    }

    return {
        Figure,
        Circle,
        Rectangle
    }
}